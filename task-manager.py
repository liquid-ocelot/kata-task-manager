
def parser(str):
    if str == "q":
        return ("q")
    elif len(str) > 0:
        if str[0] == "+":
            return (str[0], str[2:])
        elif str[0] in ["-", "x", "o"]:
            return (str[0], int(str[2:]))
        



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
