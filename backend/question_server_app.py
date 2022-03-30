import question_server as qs
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


@app.route('/question', methods=['GET', 'POST'])
def index():
    # try:
    print(request.args)
    country = request.args.get('country').split(',')
    print(country)
    qid = int(request.args.get('qid'))
    print(qid)
    response = ask_many_questions(qid, country)
    country_data = print_country_data(country)
    # except BaseException:
    #    country = 'IRQ'
    #    qid = 2
    #    response = ask_question(qid, country)

    print("BACK IN INDEX")
    print(response)
    return response, 200


if __name__ == '__main__':
    qs.question_setup()
    app.run(debug=True)


answer_dict = {'-5': 'alt_op_5', '-4': 'alt_op_4', '-3': 'alt_op_3', '-2': 'alt_op_2', '-1': 'alt_op_1', '1': 'op_1',
               '2': 'op_2', '3': 'op_3', '4': 'op_4', '5': 'op_5', '6': 'op_6', '7': 'op_7', '8': 'op_8', '9': 'op_9', '10': 'op_10'}


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


def question_setup():
    global connection
    connection = create_connection(
        "country_app", "postgres", "", "127.0.0.1", "5432"
    )
    return connection


def list_to_sql_string(country_alpha):

    question_str = ""
    for c in country_alpha:
        print(c)
        question_str += "'"+c+"',"

    return question_str[:-1]


def print_country_data(country_alpha):

    country_str = ''

    for c in country_alpha:
        country_str += "'"+c+"',"

    country_str = country_str[:-1]
    print(country_str)

    query = f"""
    SELECT f.country, wpc.gdp_per_cap, f.fertility as GDP FROM world_gdp_per_cap as wpc INNER JOIN world_fertility as f ON f.iso_code = wpc.iso_code WHERE f.iso_code IN ({country_str})
    """

    connection = question_setup()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    print("IN COUNTRY DATA!")

    for r in results:
        print("In print:")
        print(r)


def PSQL_execute(query):
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

    results = PSQL_execute(select_question_answers)

    res_df = pd.DataFrame()

    for r in results:
        country = r[0]
        response_code = r[1]
        resp_frequency = r[2]

        res_df.loc[country, response_code] = resp_frequency

    res_df.fillna(0, inplace=True)
    res_df.sort_index(axis=1, inplace=True)

    # Getting the answers

    # Get the set of response_codes that were possible in the answers, can be different for different countries
    nr_columns = list(set(map(lambda a: a[1], results)))

    # Convert the numeric response codes in the answer to text response codes in database
    text_columns = ",".join(list(map(lambda a: answer_dict[a], nr_columns)))

    # Answers query
    select_answers = f"""
    SELECT q,theme,subtheme,{text_columns} FROM answers WHERE "q" = '{question_nr}.0' 
    """
    question_legend = PSQL_execute(select_answers)[0]

    theme = question_legend[1]
    subtheme = question_legend[2]
    response_options = question_legend[3:]

    resp_dict = {}
    for i, response in enumerate(response_options):
        resp_dict[nr_columns[i]] = response

    res_df.rename(columns=resp_dict, inplace=True)

    res_df['Answers'] = res_df.sum(axis=1)
    res_df.iloc[:, :-1] = res_df.iloc[:, :-1].div(res_df['Answers'], axis=0).round(3)

    # display(res_df)
    res_dict = res_df.iloc[:, :].to_dict(orient='split')

    response = {"question_nr": question_nr, "theme": theme, "subtheme": subtheme,
                "headers": res_dict['columns'], "countries": res_dict['index'], "rows": res_dict['data']}
    return json.dumps(response)
