# main.py
from flask import Flask, render_template, request
from app.qna import ask_question
from app.weather import get_weather

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    domain = 'technology'
    answer = ask_question(question, domain)
    return render_template('index.html', question=question, answer=answer)


@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    units = request.form['units']
    weather_data = get_weather(location, units)
    temperature = weather_data['main']['temp']
    return render_template('index.html', location=location, temperature=temperature)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
