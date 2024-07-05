import os
import tkinter as tk
import pandas as pd

class BookSearchApp:
    def __init__(self, books_df):
        self.books = books_df
        self.create_gui()

    def search_books(self):
        title = self.title_entry.get().lower()
        author = self.author_entry.get().lower()
        publisher = self.publisher_entry.get().lower()

        results = self.books[
            (self.books['title'].str.lower().str.contains(title)) &
            (self.books['authors'].str.lower().str.contains(author)) &
            (self.books['publisher'].str.lower().str.contains(publisher))
        ]

        self.display_books(results)

    def display_books(self, books):
        self.result_text.delete('1.0', tk.END)  # Clear previous results
        if len(books) == 0:
            self.result_text.insert(tk.END, "\n No books found.\n")
        else:
            for index, book in books.iterrows():
                self.result_text.insert(tk.END, f"Title: {book['title']}\n")
                self.result_text.insert(tk.END, f"Author: {book['authors']}\n")
                self.result_text.insert(tk.END, f"Average Rating: {book['average_rating']}\n")
                self.result_text.insert(tk.END, f"ISBN: {book['isbn']}\n")
                self.result_text.insert(tk.END, f"ISBN13: {book['isbn13']}\n")
                self.result_text.insert(tk.END, f"Language: {book['language_code']}\n")
                if 'num_pages' in book: self.result_text.insert(tk.END, f"Number of Pages: {book['num_pages']}\n")
                self.result_text.insert(tk.END, f"Ratings Count: {book['ratings_count']}\n")
                self.result_text.insert(tk.END, f"Text Reviews Count: {book['text_reviews_count']}\n")
                self.result_text.insert(tk.END, f"Publication Date: {book['publication_date']}\n")
                self.result_text.insert(tk.END, f"Publisher: {book['publisher']}\n")
                self.result_text.insert(tk.END, "-------------------------------------------------\n")  # Divider line

        self.result_text.insert(tk.END, f'Total Books Found: {len(books)}\n')

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Book Recommendation Program")
        self.root.attributes('-fullscreen', True)  # Full screen

        # Create left frame for input fields
        left_frame = tk.Frame(self.root, padx=20, pady=20)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create input fields
        tk.Label(left_frame, text="Book Title:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.title_entry = tk.Entry(left_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(left_frame, text="Author:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.author_entry = tk.Entry(left_frame, width=40)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(left_frame, text="Publisher:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.publisher_entry = tk.Entry(left_frame, width=40)
        self.publisher_entry.grid(row=2, column=1, padx=10, pady=5)

        # Search button
        search_button = tk.Button(left_frame, text="Search", command=self.search_books)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create right frame for results display
        right_frame = tk.Frame(self.root, padx=20, pady=20)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Results display area
        self.result_text = tk.Text(right_frame, width=80, height=20)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbars for results text widget
        scrollbar = tk.Scrollbar(right_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Start the GUI main loop
        self.root.mainloop()

# Construct the file path to books.csv
csv_file_path = r'C:\sampleproj\internshipJUNE2024\New folder\projects\project4\books.csv'

# Load the CSV file
try:
    books_df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")

# Create the GUI application instance if the file was loaded successfully
if 'books_df' in locals():
    app = BookSearchApp(books_df)
