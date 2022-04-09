from flask import Flask
from flask_cors import CORS
from flask import request
import pandas as pd
import psycopg2
from psycopg2 import OperationalError

from multiprocessing import connection
import json

app = Flask(__name__)
CORS(app)
DEBUG = True


@app.route('/question', methods=['GET', 'POST'])
def index():

    # Split out countries and question ID from request
    country = request.args.get('country').split(',')
    qid = int(request.args.get('qid'))
    response = ask_many_questions(qid, country)
    country_data = print_country_data(country)

    if DEBUG:
        print(f"Request args: {request.args}, countries: {country}, question ID: {qid}")
        print(response)

    return response, 200


@app.route('/cross', methods=['GET', 'POST'])
def cross():

    country = request.args.get('country')
    qids = list(map(lambda a: int(a), (request.args.get('qid')).split(',')))
    print(qids)
    response = cross_questions(qids[0], qids[1], country)
    country_data = print_country_data(country)

    if DEBUG:
        print(f"Request args: {request.args}, countries: {country}, question ID: {qid}")
        print(response)

    return response, 200


if __name__ == '__main__':
    app.run(debug=True)

# Dictionary to convert from number (from responses) to column names in answer legend (couldn't be plain numbers)
answer_dict = {'-5': 'alt_op_5', '-4': 'alt_op_4', '-3': 'alt_op_3', '-2': 'alt_op_2', '-1': 'alt_op_1', '1': 'op_1',
               '2': 'op_2', '3': 'op_3', '4': 'op_4', '5': 'op_5', '6': 'op_6', '7': 'op_7', '8': 'op_8', '9': 'op_9', '10': 'op_10'}

# Create connection to generic PSQL database using psycopg2


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Setup connection to database


def question_setup():
    global connection
    connection = create_connection(
        "country_app", "postgres", "", "127.0.0.1", "5432"
    )
    return connection

# Convert list to string that can be added to SQL query


def list_to_sql_string(country_alpha):

    question_str = ""
    for c in country_alpha:
        question_str += "'"+c+"',"

    return question_str[:-1]


def print_country_data(country_alpha):
    # Convert country list to string
    country_str = list_to_sql_string(country_alpha)

    query = f"""
    SELECT f.country, wpc.gdp_per_cap, f.fertility as GDP FROM world_gdp_per_cap as wpc INNER JOIN world_fertility as f ON f.iso_code = wpc.iso_code WHERE f.iso_code IN ({country_str})
    """

    results = PSQL_execute(query)
    print(results)


def PSQL_execute(query):
    # Use context to avoid having failed queries brake the connection
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
    return results


def ask_many_questions(question_nr, country_alpha):
    connection = question_setup()

    country_alpha = list_to_sql_string(country_alpha)

    # Getting response frequencies
    select_question_answers = f"""
            SELECT "B_COUNTRY_ALPHA","Q{question_nr}", COUNT("Q{question_nr}") FROM QUESTIONS WHERE "B_COUNTRY_ALPHA" IN ({country_alpha}) GROUP BY "B_COUNTRY_ALPHA","Q{question_nr}" ORDER BY "B_COUNTRY_ALPHA"
        """

    # Get results of SQL query
    results = PSQL_execute(select_question_answers)

    # Create empty dataframe for storing results
    res_df = pd.DataFrame()

    # For each result row add the response code (option) and frequency to the corresponding country row in results df
    for r in results:
        country = r[0]
        response_code = r[1]
        resp_frequency = r[2]

        res_df.loc[country, response_code] = resp_frequency

    # Replace NA values and sort response options in order
    res_df.fillna(0, inplace=True)
    res_df.sort_index(axis=1, inplace=True)

    # Getting the answers

    # Get the set of response_codes that were possible in the answers, can be different for different countries
    nr_columns = list(set(map(lambda a: a[1], results)))

    # Convert the numeric response codes in the answer to text response codes in database
    #text_columns = ",".join(list(map(lambda a: answer_dict[a], nr_columns)))
    text_columns = []
    for a in nr_columns:
        if a in answer_dict.keys():
            text_columns.append(answer_dict[a])

    text_columns = ",".join(text_columns)

    # Answers query
    select_answers = f"""
    SELECT q,theme,subtheme,{text_columns} FROM answers WHERE "q" = '{question_nr}.0' 
    """
    # Store legend for mapping response code to text, e.g. 5 => "Agree strongly"
    question_legend = PSQL_execute(select_answers)[0]

    # Split out theme, subtheme and response options
    theme = question_legend[1]
    subtheme = question_legend[2]
    response_options = question_legend[3:]

    # Create dictionary with translation between resopnse code and text to allow for swapping column names of results dataframe from above
    resp_dict = {}
    for i, response in enumerate(response_options):
        resp_dict[nr_columns[i]] = response

    # Rename column names from results df
    res_df.rename(columns=resp_dict, inplace=True)

    # Summarize total number of respondents for question and write to new column
    res_df['Answers'] = res_df.sum(axis=1)
    # Convert all answers option frequencies from absolute numbers to percentages by dividing with total from ['Answers]
    res_df.iloc[:, :-1] = res_df.iloc[:, :-1].div(res_df['Answers'], axis=0).round(3)

    # Convert data frame to dictionary to allow for easy adding to larger dictionary (to be converted to JSON format)
    res_dict = res_df.iloc[:, :].to_dict(orient='split')

    response = {"question_nr": question_nr, "theme": theme, "subtheme": subtheme,
                "headers": res_dict['columns'], "countries": res_dict['index'], "rows": res_dict['data']}

    # Convert dict to JSON before returning
    return json.dumps(response)


def convert_response_code_to_text(question_nr, question_position, results):
    # Get the set of response_codes that were possible in the answers, can be different for different countries
    nr_columns = list(set(map(lambda a: a[question_position], results)))
    # print(results)
    # print(nr_columns)

    if int(question_nr) == 289:
        for i in range(len(nr_columns)):
            if int(nr_columns[i]) == 0:
                nr_columns[i] = '10'

    # Convert the numeric response codes in the answer to text response codes in database

    text_columns = []
    for a in nr_columns:
        if a in answer_dict.keys():
            text_columns.append(answer_dict[a])

    text_columns = ",".join(text_columns)
    # print(text_columns)

    # Answers query
    select_answers = f"""
    SELECT q,theme,subtheme,{text_columns} FROM answers WHERE "q" = '{question_nr}.0' 
    """

    question_legend = PSQL_execute(select_answers)[0]

    # Split out theme, subtheme and response options from question legend
    theme = question_legend[1]
    subtheme = question_legend[2]
    response_options = question_legend[3:]

    resp_dict = {}
    for i, response in enumerate(response_options):
        resp_dict[nr_columns[i]] = response

    return resp_dict, theme, subtheme


def cross_questions(question_nr_1, question_nr_2, country):
    # Query for selecting two questions, with count of second and grouping by questions
    select_cross_questions = f"""SELECT "B_COUNTRY_ALPHA", "Q{question_nr_1}","Q{question_nr_2}", COUNT("Q{question_nr_2}") FROM questions_large WHERE "B_COUNTRY_ALPHA" = '{country}' GROUP BY "B_COUNTRY_ALPHA", "Q{question_nr_1}","Q{question_nr_2}" LIMIT 40;
    """
    results = PSQL_execute(select_cross_questions)
    res_df = pd.DataFrame()

    # Adding response to dataframe
    for r in results:
        res_df.loc[r[1], r[2]] = float(r[3])

    res_df.fillna(value=0, inplace=True)
    res_df.sort_index(axis=0, inplace=True)

    # Split out index labels, theme, subtheme for each questions
    index_text, theme_1, subtheme_1 = convert_response_code_to_text(question_nr_1, 1, results)
    column_text, theme_2, subtheme_2 = convert_response_code_to_text(question_nr_2, 2, results)

    if DEBUG:
        print('Index question (Q1) - ' + theme_1 + ': ' + subtheme_1 + ' ' + str(index_text))
        print('Column question (Q2) - ' + theme_2 + ': ' + subtheme_2 + ' ' + str(column_text))

    # Rename index and column
    res_df.rename(index_text, axis=0, inplace=True)
    res_df.rename(column_text, axis=1, inplace=True)

    # Add total column and convert others two percentages
    totals = res_df.sum(axis=1)
    res_df = res_df.div(res_df.sum(axis=1), axis=0)  # .style.format("{:.2%}")
    res_df['Respondents'] = totals

    # display(res_df.iloc[:,:])#-1].style.format("{:.2%}"))

    # Convert data frame to dictionary to allow for easy adding to larger dictionary (to be converted to JSON format)
    res_dict = res_df.iloc[:, :].to_dict(orient='split')

    response = {"question_nr": [question_nr_1, question_nr_2], "theme": [theme_1, theme_2], "subtheme": [subtheme_1, subtheme_2],
                "headers": res_dict['columns'], "cross_categories": res_dict['index'], "rows": res_dict['data']}

    # Convert dict to JSON before returning
    return json.dumps(response)
