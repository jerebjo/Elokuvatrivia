from flask import Flask, render_template, request, redirect, url_for, session
import random
import socket
import os

app = Flask(__name__)
app.secret_key = 'secret-key'

questions = [
    {"question": "Mikä elokuva voitti parhaan elokuvan Oscarin vuonna 1994?",
     "choices": ["Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", "Four Weddings and a Funeral"],
     "answer": "Forrest Gump"},
    {"question": "Kuka ohjasi elokuvan Inception?",
     "choices": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Ridley Scott"],
     "answer": "Christopher Nolan"},
    {"question": "Missä elokuvassa esiintyy hahmo nimeltä Jack Sparrow?",
     "choices": ["Indiana Jones", "Harry Potter", "Pirates of the Caribbean", "The Mummy"],
     "answer": "Pirates of the Caribbean"},
    {"question": "Kuka näytteli Jokeria elokuvassa The Dark Knight (2008)?",
     "choices": ["Joaquin Phoenix", "Heath Ledger", "Jared Leto", "Jack Nicholson"],
     "answer": "Heath Ledger"},
    {"question": "Mikä elokuva alkaa repliikillä 'A long time ago in a galaxy far, far away'?",
     "choices": ["Star Wars", "Star Trek", "Guardians of the Galaxy", "Interstellar"],
     "answer": "Star Wars"},
    {"question": "Kuka ohjasi elokuvan Titanic?",
     "choices": ["James Cameron", "Peter Jackson", "Martin Scorsese", "Quentin Tarantino"],
     "answer": "James Cameron"},
    {"question": "Mikä elokuva sisältää lainin 'I’ll be back'?",
     "choices": ["Die Hard", "The Matrix", "Predator", "The Terminator"],
     "answer": "The Terminator"},
    {"question": "Mikä on Studio Ghiblin tunnettu elokuva?",
     "choices": ["Your Name", "Howl's Moving Castle", "Akira", "Ghost in the Shell"],
     "answer": "Howl's Moving Castle"},
    {"question": "Kuka näytteli pääosaa elokuvassa Gladiator (2000)?",
     "choices": ["Brad Pitt", "Russell Crowe", "Mel Gibson", "Tom Cruise"],
     "answer": "Russell Crowe"},
    {"question": "Missä elokuvassa esiintyy hahmo nimeltä Neo?",
     "choices": ["Blade Runner", "The Matrix", "Equilibrium", "Minority Report"],
     "answer": "The Matrix"}
]

@app.route('/')
def index():
    session['order'] = random.sample(range(len(questions)), len(questions))
    session['current'] = 0
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'order' not in session or 'current' not in session:
        return redirect(url_for('index'))

    if session['current'] >= len(session['order']):
        return redirect(url_for('result'))

    q_index = session['order'][session['current']]
    question = questions[q_index]

    if request.method == 'POST':
        selected = request.form.get('answer')
        session['selected'] = selected
        session['correct'] = question['answer']
        if selected == question['answer']:
            session['score'] += 1
        session['current'] += 1
        return redirect(url_for('feedback'))

    return render_template('quiz.html', question=question)

@app.route('/feedback')
def feedback():
    selected = session.get('selected')
    correct = session.get('correct')

    if not selected or not correct:
        return redirect(url_for('quiz'))

    result = selected == correct
    return render_template("feedback.html", user=selected, correct=correct, result=result)

@app.route('/result')
def result():
    player = socket.gethostname()
    score = session.get('score', 0)
    total = len(session.get('order', []))
    score_line = f"{player}: {score}/{total}\n"
    score_file = "/home/vagrant/shared/scores.txt"

    try:
        with open(score_file, 'a') as f:
            f.write(score_line)
    except Exception as e:
        print(f"Virhe tuloksen tallennuksessa: {e}")

    results = []
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            results = f.readlines()

    return render_template('result.html', score=score, total=total, results=results)
