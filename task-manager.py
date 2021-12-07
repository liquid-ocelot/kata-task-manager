


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

    def display(self, console):
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


class FakeConsole:

    def __init__(self, *args) -> None:
        self.output = []
        self.input = list(args)
        self.current_input = 0

    def print(self, str):
        self.output.append(str)

    def get_input(self):
        self.current_input += 1
        return self.input[self.current_input - 1]

class Console:

    def print(self, str):
        print(str)

    def get_input(self):
        return input()


def run(console):
    tasklist = TaskList()
    while(True):
        tasklist.display(console)
        user_input = parser(console.get_input())
        if user_input == "q":
            break
        elif user_input[0] == "+":
            tasklist.add(user_input[1])
        elif user_input[0] == "-":
            tasklist.remove(user_input[1])
        elif user_input[0] == "x":
            tasklist.check_task(user_input[1])
        elif user_input[0] == "o":
            tasklist.uncheck_task(user_input[1])
    console.print("Bye !")

if __name__ == "__main__":
    run(Console())


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
    console = FakeConsole()
    tasklist = TaskList()
    tasklist.display(console)
    tasklist.add("Learn Python")
    tasklist.display(console)
    expected = ["No task yet", "1 [ ] Learn Python"]
    assert expected == console.output


def test_run_loop():
    console = FakeConsole("+ Learn Python", "x 1", "q")
    run(console)
    expected = ["No task yet", "1 [ ] Learn Python", "1 [x] Learn Python", "Bye !"]
    assert expected == console.output