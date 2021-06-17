from list import List
import datetime

def dueDate(aList):
    return aList.due_date

class TodoList:
    "Represents a collection of todo lists"
    
    def __init__(self):
        "Initilize the todolist with an empty list"
        self.lists = []
        self.list_count = 0

    def new_list(self):
        "Create a new list and added to the todolist"
        todo = input("Enter the todo: ")
        print("Would you like to set a due date? If not, the due date will be")
        choice = input("set it in 7 days. (y/n): ")
        if choice == 'y' or choice == 'Y':
            year = int(input("Year? "))
            month = int(input("Month? "))
            day = int(input("Day? "))
            due_date = datetime.date(year, month, day)
            self.lists.append(List(todo, due_date))
        else:
            self.lists.append(List(todo))
        self.list_count += 1

    # def _find_list(self, list_id):
    #     "Locate the list with the given id"
    #     for list in self.lists:
    #         if str(list.id) == str(list_id):
    #             return list
    #     return None

    def _check_input_id(self, list_id):
        "Check if the id given by user is valid"
        return 0 < list_id and list_id <= self.list_count

    def check_list(self):
        "Check off the list with index given by user"
        list_id = int(input("Which list would you like to check off (number)? "))
        if not self._check_input_id(list_id):
            print("Invalid index")
            return
        del self.lists[list_id - 1]
        

    def modify_todo(self, list_id, todo):
        "Modify the list with the given id"
        if not self._check_input_id(list_id):
            print("Invalid index!")
            return
        self.lists[list_id - 1].todo = todo

    def modify_due_date(self, list_id, due_date):
        "Modify the due date with the given id"
        if not self._check_input_id(list_id):
            print("Invalid index!")
            return
        self.list[list_id - 1].due_date = due_date

    def modify_list(self):
        id = int(input("Enter a list id: "))
        if not self._check_input_id(id):
            print("Invalid index!")
            return
        todo = input("Enter new todo: ")
        year = int(input("Enter new due year: "))
        month = int(input("Month: "))
        date = int(input("Day: "))
        new_due = datetime.date(year, month, date)
        self.lists[id - 1].todo = todo
        self.list[id - 1].due_date = new_due

    def is_empty(self):
        return 0 == self.list_count

    def sort_list(self):
        if not self.is_empty():
            self.lists.sort(key=dueDate)

    def show_list(self):
        "Show all lists in the todo list"
        print("Current list: ")
        if self.is_empty():
            print("Nothing is on the todolist")
        else:
            for i, list in enumerate(self.lists):
                print("Todo #{}:".format(i + 1), list.todo)
                print("Due date:", list.due_date)
                

    