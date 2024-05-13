from flask import Flask, render_template, request, redirect, url_for
import random
from questions import questions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', questions=questions, title="Home")

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    question = next((q for q in questions if q["id"] == question_id), None)
    if question is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        user_choice = request.form.get('user_choice')
        correct = request.form['correct']
        return render_template('result.html', question=question, user_choice=user_choice, correct=correct, title="Result")

    response_type = random.choice(['friend', 'llm'])
    response = question[response_type]
    return render_template('question.html', question=question, response=response, response_type=response_type, title="Question")

if __name__ == '__main__':
    app.run(debug=True)
