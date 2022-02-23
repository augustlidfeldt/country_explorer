import question_server as qs
from flask import Flask
from flask_cors import CORS
import json
from multiprocessing import connection
import pandas as pd
import psycopg2
from psycopg2 import OperationalError
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    response = ask_question(26, 'JPN')
    print("BACK IN INDEX")
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
        "sm_app", "postgres", "", "127.0.0.1", "5432"
    )
    return connection


def ask_question(question_nr, country_alpha):
    select_question_answers = f"""
        SELECT "Q{question_nr}", COUNT("Q{question_nr}") FROM QUESTIONS WHERE "B_COUNTRY_ALPHA" = '{country_alpha}' GROUP BY "Q{question_nr}" ORDER BY "Q{question_nr}"
    """

    connection = question_setup()
    cursor = connection.cursor()
    cursor.execute(select_question_answers)
    results = cursor.fetchall()

    cols = ''
    freq = []
    for r in results:
        cols += (answer_dict[str(r[0])])+','
        freq.append(r[1])

    # Calculate share
    sum = 0
    for opt in freq:
        sum += int(opt)
    freq = list(map(lambda a: round((a/sum), 4)*100, freq))

    select_answers = f"""SELECT q,theme,subtheme,{cols[:-1]} FROM ANSWERS_2 WHERE "q" = '{question_nr}.0'"""
    select_columns = """SELECT column_name, ordinal_position FROM information_schema.columns WHERE table_name = 'answers_2'"""

    def get_selection(query):
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        return results

    question_details = get_selection(select_answers)[0]
    freq = list(map(lambda a: str(round(a, 4))+"%", freq))  # add percentages, but string
    data = [country_alpha, *list(question_details[0:3]), *freq, sum]

    columns = [*["Country", "Question", "Theme", "Subtheme"], *question_details[3:], *['Answers']]
    df = pd.DataFrame([data], columns=columns)
    if df["Subtheme"][0] == '0':
        print("No subtheme!!!")
        df.drop(labels="Subtheme", axis=1, inplace=True)

    print(country_alpha)

    print("hello")
    response = {"headers": list(df.columns), "rows": list(df.iloc[0])}
    response = str(response).replace("'", '"')
    print(type(response))
    return str(response)
