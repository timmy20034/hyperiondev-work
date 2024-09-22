import sqlite3

def create_connection():
    # Creating the database called ebookstore
    db = sqlite3.connect("ebookstore")

    cursor = db.cursor()

    return db, cursor

def add_new_book(db, cursor):
   
    # Inputing the information for the new book
    book_id = int(input("Please enter the books id:"))
    book_name = input("Please enter the new books title: ")
    book_author = input("Please enter the author of the book:")
    book_qty = int(input("How many of the book do we have?:"))
    
    # Iserting the information into the table
    cursor.execute('''INSERT INTO book(id, title, author, qty)
                   VALUES(:id, :title, :author, :qty)''',
                   {'id':book_id, 'title':book_name, 'author':book_author,
                     'qty':book_qty})
    db.commit()
    return

def update_book_info(db, cursor):
   
    # Asking for information for the new book
    id = int(input("Please enter the id of the book you want to update:"))
    book = input("Please enter the books title:")
    author = input("Please enter the author:")
    qty = int(input("Please enter the number of books we have:"))
    
    # Inputting information into table
    cursor.execute('''UPDATE book SET title = ? WHERE id = ?''', (book, id))
    cursor.execute('''UPDATE book SET author = ? WHERE id = ?''', (author, id))
    cursor.execute('''UPDATE book SET qty = ? WHERE id = ?''', (qty, id))
    
    db.commit()
    return

def delete_book(db, cursor):

    # Asking for the information for what to delete
    book_id = int(input("Please enter the id of the book you want to Delete:"))

    # Deleting the information from the table
    cursor.execute('''DELETE FROM book WHERE id = ?''', (book_id))

    db.commit()
    return

def search_book(cursor):

    # Asking for the id to search for the book
    search_id = int(input("Please enter the id of the book you want to find:"))

    # Searching the table for the book
    cursor.execute('''SELECT title, author, qty FROM book WHERE id=?''',
                    (search_id,))
    book_search = cursor.fetchone()

    # Printing the results of the search
    if book_search:
        print(book_search)
    else:
        print("Book not found.")

    return 

menu = True
db, cursor = create_connection()

# Creating the table called book
cursor.execute('''
                CREATE TABLE book(id INTEGER PRIMARY KEY, title TEXT,
                author TEXT, qty INTEGER)
                ''')

 # Setting up the information for the table
book_info = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
             (3002, "Harry Potter and the Philosopher's Stone",
              "J.K. Rowling", 40),
             (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
             (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
             (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

# Inputting the information into the table 
cursor.executemany(''' INSERT INTO book(id, title,
                   author, qty) VALUES(?,?,?,?)''', book_info)

db.commit()

# Menu to direct you to what you want to do
while True:
    choice = int(input('''\n What would you like to do?
    1. Enter book
    2. Update book
    3. Delete book
    4. Search book
    0. Exit
    '''))

    if choice == 1:
        add_new_book(db, cursor)

    elif choice == 2:
        update_book_info(db, cursor)

    elif choice == 3:
        delete_book(db, cursor)

    elif choice == 4:
        search_book(cursor)

    elif choice == 0:
        print("Exiting Application...")
        db.close()
        break

    else:
        print("Incorrect Input, please try again.")
