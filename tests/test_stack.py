from unittest import TestCase, main
from src.stack import Node, Stack


class TestStack(TestCase):

    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, "a")
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, n1.data)


    def test_slice(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        stack.push('data4')
        self.assertEqual(stack.top.data, "data4")
        self.assertEqual(stack.pop().data, "data4")
        self.assertEqual(stack.top.data, "data3")
        self.assertEqual(stack.top.next_node.data, "data2")
        self.assertEqual(stack.top.next_node.next_node.data, "data1")
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError) as e:
            res = stack.top.next_node.next_node.next_node.data

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        stack.push('data4')
        self.assertEqual(stack.pop().data, "data4")
        self.assertEqual(stack.pop().data, "data3")
        self.assertEqual(stack.pop().data, "data2")
        self.assertEqual(stack.pop().data, "data1")
        with self.assertRaises(IndexError) as e:
            stack.pop()

    def test_top(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')
        stack.pop()
        self.assertEqual(stack.top, None)


if __name__ == '__main__':
    main()
