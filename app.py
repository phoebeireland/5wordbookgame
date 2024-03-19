import csv
import random

def load_books_from_csv(file_path):
    books = {'easy': [], 'medium': [], 'hard': []}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            difficulty = row['Difficulty'].lower()
            books[difficulty].append({'title': row['Book Title'], 'clue': row['Clue']})
    return books

def get_random_book(books, difficulty, selected_books):
    available_books = [book for book in books[difficulty] if book['title'] not in selected_books]
    return random.choice(available_books)

def update_score(score, is_correct):
    if is_correct:
        return score + 1
    else:
        return score

def main():
    score = 0
    max_score = 5  # Define maximum score achievable
    selected_books = set()

    # Load books from CSV
    books = load_books_from_csv('books.csv')

    # Allow user to choose difficulty level
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Validate user input
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Main loop for the game
    for _ in range(max_score):  # Play until the maximum score is reached
        # Select a random book that hasn't been selected before
        book = get_random_book(books, difficulty, selected_books)
        selected_books.add(book['title'])
        
        book_title = book['title']
        clue = book['clue']

        # Display the clue to the user
        print("Here's your clue:")
        print(clue)

        # Get user input
        user_guess = input("Enter the name of the book: ")

        # Check if the user's guess matches the correct book title
        if user_guess.lower() == book_title.lower():
            print("Congratulations! You guessed correctly.")
            score = update_score(score, True)
        else:
            print(f"Sorry, the correct answer was: {book_title}")
            score = update_score(score, False)

        print(f"Current Score: {score}/{max_score}")

    print("Game Over. Your final score:", score)

if __name__ == "__main__":
    main()
