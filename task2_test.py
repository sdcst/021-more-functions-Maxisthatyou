#! python3

import task2

def test1():
  assert task2.largest([0,10,3,8]) == 10

def test2():
    assert task2.largest([10,50,100,3000.1]) == 3000.1
