#!python

from stack import Stack
import unittest


class StackTest(unittest.TestCase):

    def test_init(self):
        s = Stack()
        assert s.peek() is None
        assert s.length() == 0
        assert s.is_empty() is True

    def test_init_with_list(self):
        s = Stack([1, 2, 3])
        assert s.peek() == 3
        assert s.length() == 3
        assert s.is_empty() is False
        # s = Stack(['A', 'B', 'C'])
        # assert s.peek() == 'C'
        # assert s.length() == 3
        # assert s.is_empty() is False

    def test_length(self):
        s = Stack()
        assert s.length() == 0
        s.push(1)
        # s.push('A')
        assert s.length() == 1
        s.push(2)
        # s.push('B')
        assert s.length() == 2
        s.pop()
        assert s.length() == 1
        s.pop()
        assert s.length() == 0

    def test_push(self):
        #changes to make compatible with new min fxnality
        s = Stack()
        s.push(1)
        assert s.peek() == 1
        assert s.length() == 1
        s.push(2)
        assert s.peek() == 2
        assert s.length() == 2
        s.push(3)
        assert s.peek() == 3
        assert s.length() == 3
        assert s.is_empty() is False
        # s = Stack()
        # s.push('A')
        # assert s.peek() == 'A'
        # assert s.length() == 1
        # s.push('B')
        # assert s.peek() == 'B'
        # assert s.length() == 2
        # s.push('C')
        # assert s.peek() == 'C'
        # assert s.length() == 3
        # assert s.is_empty() is False

    def test_peek(self):
        s = Stack()
        assert s.peek() is None
        s.push(1)
        assert s.peek() == 1
        s.push(2)
        assert s.peek() == 2
        s.pop()
        assert s.peek() == 1
        s.pop()
        assert s.peek() is None
        # s = Stack()
        # assert s.peek() is None
        # s.push('A')
        # assert s.peek() == 'A'
        # s.push('B')
        # assert s.peek() == 'B'
        # s.pop()
        # assert s.peek() == 'A'
        # s.pop()
        # assert s.peek() is None

    def test_pop(self):
        s = Stack([1, 2, 3])
        assert s.pop() == 3
        assert s.length() == 2
        assert s.pop() == 2
        assert s.length() == 1
        assert s.pop() == 1
        assert s.length() == 0
        # assert s.is_empty() is False #forced to fail the test
        assert s.is_empty() is True
        with self.assertRaises(ValueError):
            s.pop()
        # s = Stack(['A', 'B', 'C'])
        # assert s.pop() == 'C'
        # assert s.length() == 2
        # assert s.pop() == 'B'
        # assert s.length() == 1
        # assert s.pop() == 'A'
        # assert s.length() == 0
        # # assert s.is_empty() is False #forced to fail the test
        # assert s.is_empty() is True
        # with self.assertRaises(ValueError):
        #     s.pop()

    def test_min(self):
        s = Stack([17, 5, 8])
        assert s.length() == 3
        assert s.min() == 5
        assert s.lowest == 5
        s.push(1)
        assert s.length() == 4
        assert s.lowest == 1
        assert s.min() == 1

if __name__ == '__main__':
    unittest.main()
