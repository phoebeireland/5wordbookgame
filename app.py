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

def get_random_book(books, difficulty):
    return random.choice(books[difficulty])

def main():
    # Load books from CSV
    books = load_books_from_csv('books.csv')

    # Allow user to choose difficulty level
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Validate user input
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    # Select a random book and its corresponding clue
    book = get_random_book(books, difficulty)
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
    else:
        print(f"Sorry, the correct answer was: {book_title}")

if __name__ == "__main__":
    main()