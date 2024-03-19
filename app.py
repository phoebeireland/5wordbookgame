from flask import Flask, render_template, request, jsonify
import csv
import random

app = Flask(__name__)

def load_books_from_csv(file_path):
    books = {'easy': [], 'medium': [], 'hard': []}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            difficulty = row['Difficulty'].lower()
            alternate_answers = [answer.strip() for answer in row.get('Alternate Answers', '').split(',')]
            books[difficulty].append({'title': row['Book Title'], 'clue': row['Clue'], 'alternate_answers': alternate_answers})
    return books

def get_random_book(books, difficulty, selected_books):
    available_books = [book for book in books[difficulty] if book['title'] not in selected_books]
    return random.choice(available_books)

def update_score(score, is_correct):
    if is_correct:
        return score + 1
    else:
        return score

def check_answer(user_guess, correct_answers):
    user_guess_lower = user_guess.lower()
    for answer in correct_answers:
        if user_guess_lower == answer.lower():
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    difficulty = data['difficulty']
    selected_books = set(data['selected_books'])
    books = load_books_from_csv('books.csv')
    max_score = 5
    score = 0
    responses = []

    for _ in range(max_score):
        book = get_random_book(books, difficulty, selected_books)
        selected_books.add(book['title'])
        book_title = book['title']
        clue = book['clue']
        correct_answers = [book_title] + book['alternate_answers']
        responses.append({'clue': clue, 'score': score})

    return jsonify(responses)

if __name__ == "__main__":
    app.run(debug=True)
