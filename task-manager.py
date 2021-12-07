



##########
###TEST###
##########


def test_parse_input_add():
    expected = ("+", "test test")
    actual = fun("+ test test")
    assert expected == actual

def test_parse_input_remove():
    expected = ("-", 1)
    actual = fun("- 1")
    assert expected == actual

def test_parse_input_quit():
    expected = ("q")
    actual = fun("q")
    assert expected == actual