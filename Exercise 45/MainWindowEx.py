from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.books = []  # Store book data as a list of dictionaries
        self.selected_book = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Additional UI Setup for Books Section
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)

        # Connect Buttons to Their Functions
        self.pushButton_save.clicked.connect(self.create)
        self.pushButton_remove.clicked.connect(self.remove_book)
        self.pushButton_search_title.clicked.connect(self.search_by_title)
        self.pushButton_filter_year.clicked.connect(self.filter_by_year)
        self.pushButton_filter_publisher.clicked.connect(self.filter_by_publisher)
        self.pushButton_search_ISBN.clicked.connect(self.search_by_ISBN)


    def create(self):
        isbn = self.lineEdit_ISBN.text().strip()
        title = self.lineEdit_title.text()
        author = self.lineEdit_author.text()
        year = self.lineEdit_year.text()
        publisher = self.lineEdit_publisher.text()

        if not isbn:
            QMessageBox.warning(self.MainWindow, "Error", "ISBN cannot be empty!")
            return

        # Update if ISBN already exists
        for book in self.books:
            if book['ISBN'] == isbn:
                book.update({'Title': title, 'Author': author, 'Year': year, 'Publisher': publisher})
                QMessageBox.information(self.MainWindow, "Updated", "Book updated successfully!")
                self.clear_details()
                return

        # Add new book
        new_book = {'ISBN': isbn, 'Title': title, 'Author': author, 'Year': year, 'Publisher': publisher}
        self.books.append(new_book)
        self.add_book_button(new_book)
        QMessageBox.information(self.MainWindow, "Đã Lưu", "Sách đã được thêm thành công!")
        self.clear_details()

    def add_book_button(self, book):
        display_text = f"ISBN:{book['ISBN']}, {book['Title']}, {book['Year']}, {book['Publisher']}"
        btn = QPushButton(display_text)
        btn.clicked.connect(lambda: self.display_book_details(book['Title']))
        self.verticalLayout.addWidget(btn)

    def display_book_details(self, title):
        for book in self.books:
            if book['Title'] == title:
                self.lineEdit_ISBN.setText(book['ISBN'])
                self.lineEdit_title.setText(book['Title'])
                self.lineEdit_author.setText(book['Author'])
                self.lineEdit_year.setText(book['Year'])
                self.lineEdit_publisher.setText(book['Publisher'])
                self.selected_book = book
                break

    def remove_book(self):
        if not self.selected_book:
            QMessageBox.warning(self.MainWindow, "Error", "No book selected!")
            return

        # Remove the corresponding button
        for i in range(self.verticalLayout.count()):
            button = self.verticalLayout.itemAt(i).widget()
            if button.text() == self.selected_book['Title']:
                self.verticalLayout.removeWidget(button)
                button.deleteLater()
                break

        # Remove book from list
        self.books.remove(self.selected_book)
        self.selected_book = None
        self.clear_details()
        QMessageBox.information(self.MainWindow, "Removed", "Book removed successfully!")

    def clear_details(self):
        self.lineEdit_ISBN.clear()
        self.lineEdit_title.clear()
        self.lineEdit_author.clear()
        self.lineEdit_year.clear()
        self.lineEdit_publisher.clear()

    def search_by_title(self):
        search_title = self.lineEdit_title.text().strip()
        results = [book for book in self.books if search_title.lower() in book['Title'].lower()]
        if results:
            QMessageBox.information(self.MainWindow, "Found", f"Found {len(results)} book(s) matching '{search_title}'")
        else:
            QMessageBox.warning(self.MainWindow, "Not Found", "No books match your search.")

    def search_by_ISBN(self):
        search_isbn = self.lineEdit_ISBN.text().strip()
        results = [book for book in self.books if search_isbn == book['ISBN']]
        if results:
            QMessageBox.information(self.MainWindow, "Found", f"Found {len(results)} book(s) matching ISBN '{search_isbn}'")
        else:
            QMessageBox.warning(self.MainWindow, "Not Found", "No books match your search.")

    def filter_by_year(self):
        year = self.lineEdit_year.text().strip()
        results = [book for book in self.books if book['Year'] == year]
        if results:
            QMessageBox.information(self.MainWindow, "Found", f"Found {len(results)} book(s) published in {year}")
        else:
            QMessageBox.warning(self.MainWindow, "Not Found", "No books match your filter.")

    def filter_by_publisher(self):
        publisher = self.lineEdit_publisher.text().strip()
        results = [book for book in self.books if publisher.lower() in book['Publisher'].lower()]
        if results:
            QMessageBox.information(self.MainWindow, "Found", f"Found {len(results)} book(s) by publisher '{publisher}'")
        else:
            QMessageBox.warning(self.MainWindow, "Not Found", "No books match your filter.")

    def show(self):
        self.MainWindow.show()
