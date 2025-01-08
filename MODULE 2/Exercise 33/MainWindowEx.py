import random
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = None
        self.array = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Connect the "Random Array" button to its function
        self.pushButton_random.clicked.connect(self.random_array)
        self.pushButton_sum.clicked.connect(self.sum_of_array)
        self.pushButton_find.clicked.connect(self.find_smallest_element)
        self.pushButton_increment.clicked.connect(self.increment_double_values)
        self.pushButton_count.clicked.connect(self.count_odd_elements)
        self.pushButton_sum_odd.clicked.connect(self.sum_of_odd_elements)
        self.pushButton_sort_ascend.clicked.connect(self.sort_ascending)
        self.pushButton_sort_descend.clicked.connect(self.sort_descending)

    def random_array(self):
        self.array = [random.randint(1, 100) for _ in range(10)]
        array_string = ', '.join(map(str, self.array))
        self.lineEdit_array.setText(array_string)
        self.lineEdit_result.setText("Random array generated.")

    def sum_of_array(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        total_sum = sum(self.array)
        self.lineEdit_result.setText(f"Sum of array: {total_sum}")

    def find_smallest_element(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        smallest = min(self.array)
        self.lineEdit_result.setText(f"Smallest element: {smallest}")

    def increment_double_values(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        self.array = [num + 1 if num % 2 == 0 else num for num in self.array]
        array_string = ', '.join(map(str, self.array))
        self.lineEdit_array.setText(array_string)
        self.lineEdit_result.setText("Even values incremented by 1.")

    def count_odd_elements(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        odd_count = sum(1 for num in self.array if num % 2 != 0)
        self.lineEdit_result.setText(f"Odd elements count: {odd_count}")

    def sum_of_odd_elements(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        odd_sum = sum(num for num in self.array if num % 2 != 0)
        self.lineEdit_result.setText(f"Sum of odd elements: {odd_sum}")

    def sort_ascending(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        self.array.sort()
        array_string = ', '.join(map(str, self.array))
        self.lineEdit_array.setText(array_string)
        self.lineEdit_result.setText("Array sorted in ascending order.")

    def sort_descending(self):
        if not self.array:
            self.lineEdit_result.setText("No array generated. Please click 'Random Array' first.")
            return

        self.array.sort(reverse=True)
        array_string = ', '.join(map(str, self.array))
        self.lineEdit_array.setText(array_string)
        self.lineEdit_result.setText("Array sorted in descending order.")

    def show(self):
        self.MainWindow.show()