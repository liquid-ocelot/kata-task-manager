
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
        

class taskClass:

    def __init__(self) -> None:
        self.list = []

    def add(self, str):
        self.list.append((str, False))

    def get(self):
        return self.list

    def remove(self, index):
        real_index = index - 1
        del self.list[real_index]

    def fun(self, index):
        real_index = index - 1
        description = self.list[real_index][0]
        self.list[real_index] = (description, True)

    def fun2(self, index):
        real_index = index - 1
        description = self.list[real_index][0]
        self.list[real_index] = (description, False)



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
    tasklist = taskClass()
    tasklist.add("task")
    expected = [("task", False)]
    assert expected == tasklist.get()

def test_remove_task():
    tasklist = taskClass()
    tasklist.add("task")
    tasklist.remove(1)
    expected = []
    assert expected == tasklist.get()

def test_check_task():
    tasklist = taskClass()
    tasklist.add("task")
    tasklist.fun(1)
    expected = [("task", True)]
    assert expected == tasklist.get()

def test_uncheck_task():
    tasklist = taskClass()
    tasklist.add("task")
    tasklist.fun(1)
    tasklist.fun2(1)
    expected = [("task", False)]
    assert expected == tasklist.get()
