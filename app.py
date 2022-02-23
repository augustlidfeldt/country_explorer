import question_server as qs
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    response = qs.ask_question(49, 'IRQ')
    print("BACK IN INDEX")
    print("Adding new print")
    return response, 200


if __name__ == '__main__':
    qs.question_setup()
    app.run(debug=True)
