'''
Steps to Extract Data from a JSON File
Import the json module.
Open the JSON file using Python's open() function.
Use json.load() to parse the JSON file into a Python dictionary or list.
Access the data using keys or indices.
'''
import json

with open('books.json') as file:
    books = json.load(file)

print("\n|--- Select what you want to do with the file ---|\n")
print('1. Add a new book 📙')
print('2. Read the content of the json 📃')
print('3. Edit properties of a book ✏️')
print('4. Remove a book 🗑️')

choice = input('\nEnter your choice (1-4): ')

match choice:
    case "1":
        # Create
        print("\n--- You can now add a new book 📙---\n")
        id = input('Enter the ID for the new book: ')
        title = input('Enter the title: ')
        author = input('Enter the author: ')
        genre = input('Enter the genre: ')
        
        new_book = {"id": id, "title": title, "author": author, "genre": genre}
        books.append(new_book)
        
        with open('books.json', 'w') as file:
            json.dump(books, file, indent = 4)
            
        print("\nThe book has been successfully added ✅\n")
    
    case '2': 
        # Read
        print("\n--- List of books in the file 📙 ---\n")
        for book in books:
            print(f" ID: {book.get('id')} | Title: {book['title']}📖 | Author: {book['author']} | Genre: {book['genre']}")
            
    case '3':
        # Update
        print("\n--- You can edit the properties of a book ✏️ ---")
        book_to_update = input('Enter the ID of the book you want to update: ')
        for book in books:
            if book['id'] == book_to_update:
                new_title = input('Enter the new title for the book: ')
                new_author = input('Enter the name of the new author: ')
                new_genre = input('Enter the genre of the book: ')
                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_genre:
                    book['genre'] = new_genre
                print('\nChanges updated successfully!\n')
                break
            
        else:
            print('Book not found!')
        
        with open('books.json', 'w') as file:
            json.dump(books, file, indent = 4)
            
    case '4':
        # Delete
        
        print("\n--- You are now deleting a book 🗑️ ---\n")
        
        for book in books:
            print(f"ID: {book['id']} | Title: {book['title']} 📖 | Author: {book['author']} | Genre: {book['genre']}")
            
        book_to_delete = input("\nEnter the ID of the book to delete: ")
        
        books = [book for book in books if book["id"] != book_to_delete]
        
        print("\nThe book has been removed successfully! ✅\n")

        with open('books.json', 'w') as file:
            json.dump(books, file, indent=4)
        
    case _:
        print("\nEnter one of the choices from above 👆\n")
            
        
                