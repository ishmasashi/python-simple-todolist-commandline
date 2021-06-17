import datetime

class List:
    """Represents a list in todo list. Store todo and due date
    if due date is not passed, then set the due date to 7 days from 
    today"""

    def __init__(self, todo, due_date=0):
        """Initialize a list with todo and the duedate"""

        self.todo = todo
        self.creation_date = datetime.date.today()
        if not due_date:
            self.due_date = self.creation_date + datetime.timedelta(days=7)
        else:
            self.due_date = due_date
        

    # def show(self):
    #     print("Todo({}):".format(self.id), self.todo)
    #     print("    Due:", self.due_date)
