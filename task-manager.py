


def parser(text):
    if text == "q":
        return ("q")
    elif len(text) > 0 and text[0] == "+":
        description = text[2:]
        return ("+", description)
    elif len(text) > 0 and text[0] in ["-", "x", "o"]:
        operator = text[0]
        index = int(text[2:])
        return (operator, index)
        

class TaskList:

    def __init__(self) -> None:
        self.list = []

    def add(self, str):
        self.list.append((str, False))

    def get(self):
        return self.list

    def remove(self, index):
        real_index = index - 1
        del self.list[real_index]

    def check_task(self, index):
        real_index = index - 1
        description = self.list[real_index][0]
        self.list[real_index] = (description, True)

    def uncheck_task(self, index):
        real_index = index - 1
        description = self.list[real_index][0]
        self.list[real_index] = (description, False)

    def fun(self, console):
        if len(self.list) == 0:
            console.print("No task yet")
        else:
            for i in range(len(self.list)):
                number = i + 1
                status = self.list[i][1]
                description = self.list[i][0]
                if(status):
                    console.print("%s [x] %s" % (number, description))
                else:
                    console.print("%s [ ] %s" % (number, description))


class ConsoleInterface():

    def __init__(self) -> None:
        self.output = []

    def print(self, str):
        self.output.append(str)

##########
###TEST###
##########


def test_parse_input_add():
    expected = ("+", "test test")
    actual = parser("+ test test")
    assert expected == actual

def test_parse_input_remove():
    expected = ("-", 1)
    actual = parser("- 1")
    assert expected == actual

def test_parse_input_quit():
    expected = ("q")
    actual = parser("q")
    assert expected == actual

def test_add_task():
    tasklist = TaskList()
    tasklist.add("task")
    expected = [("task", False)]
    assert expected == tasklist.get()

def test_remove_task():
    tasklist = TaskList()
    tasklist.add("task")
    tasklist.remove(1)
    expected = []
    assert expected == tasklist.get()

def test_check_task():
    tasklist = TaskList()
    tasklist.add("task")
    tasklist.check_task(1)
    expected = [("task", True)]
    assert expected == tasklist.get()

def test_uncheck_task():
    tasklist = TaskList()
    tasklist.add("task")
    tasklist.check_task(1)
    tasklist.uncheck_task(1)
    expected = [("task", False)]
    assert expected == tasklist.get()

def test_display_list():
    console = ConsoleInterface()
    tasklist = TaskList()
    tasklist.fun(console)
    tasklist.add("Learn Python")
    tasklist.fun(console)
    expected = ["No task yet", "1 [ ] Learn Python"]
    assert expected == console.output
