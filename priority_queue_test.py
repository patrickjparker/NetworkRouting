import pytest
from HeapPriorityQueue import *
from ArrayPriorityQueue import *

def pytest_generate_tests(metafunc):
    if "queue" in metafunc.fixturenames:
        metafunc.parametrize("queue", ["array", "heap"])

def set_up_queue(queue, nodes):
    if (queue == "heap"):
        return HeapPriorityQueue(nodes)
    else:
        return ArrayPriorityQueue(nodes)

def test_single_index(queue):
    array = [ 3.0, 2.0, 2.5, 4.0 ]
    queue = set_up_queue(queue, len(array))
    queue.decrease_key(1, 4)
    assert(queue.delete_min() == 1)

def test_multiple_changes(queue):
    queue = set_up_queue(queue, 8)
    queue.decrease_key(0, 4)
    queue.decrease_key(2, 7)
    queue.decrease_key(1, 10)
    queue.decrease_key(5, 3)
    assert(queue.delete_min() == 5)
    assert(queue.delete_min() == 0)
    assert(queue.delete_min() == 2)
    assert(queue.delete_min() == 1)

def test_change_existing_value(queue):
    queue = set_up_queue(queue, 8)
    queue.decrease_key(1, 5)
    queue.decrease_key(3, 4)
    queue.decrease_key(1, 2)
    assert(queue.delete_min() == 1)
    assert(queue.delete_min() == 3)

def test_insert(queue):
    queue = set_up_queue(queue, 8)
    queue.insert(3, 74)
    assert(queue.delete_min() == 3)