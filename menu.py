import sys
from todolist import TodoList
from list import List

class Menu:
    "Display a menu and do the choice a user enters"

    def __init__(self):
        self.todolist = TodoList()
        self.choices = {
            "1": self.todolist.new_list,
            "2": self.todolist.check_list,
            "3": self.todolist.modify_list,
            "4": self.todolist.sort_list,
            "5": self.quit
        }

    def display_menu(self):
        print("\nTodo list menu\n")
        print("1: Add list")
        print("2: Check list")
        print("3: Modify list")
        print("4: Sort lists")
        print("5: Quit")

    def run(self):
        "Dispaly menu and get a user choice and run"
        while True:
            print("**********************************")
            print("Todo list")
            print("**********************************\n")
            self.todolist.show_list()
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("Thank you for using your todo today")
        sys.exit()


if __name__ == "__main__":
    Menu().run()