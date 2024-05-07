#! python3

import problem1

def test1():
    assert problem1.convertTemp(10,'C') == 50


def test2():
    assert problem1.convertTemp(32,'F') == 0
