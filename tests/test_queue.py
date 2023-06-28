from unittest import TestCase, main
from src.queue import Node, Queue


class TestQueue(TestCase):

    def test_node(self) -> None:
        n1: Node = Node(5)
        n2: Node = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, "a")
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, n1.data)


    def test_slice(self) -> None:
        queue: Queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)
        with self.assertRaises(AttributeError) as e:
            res = queue.tail.next_node.data

    def test_head(self) -> None:
        queue: Queue = Queue()
        self.assertEqual(queue.head, None)
        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node, None)
        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertNotEqual(queue.head.next_node, None)

    def test_tail(self) -> None:
        queue: Queue = Queue()
        self.assertEqual(queue.tail, None)
        queue.enqueue('data1')
        self.assertEqual(queue.tail.data, 'data1')
        self.assertEqual(queue.tail.next_node, None)
        queue.enqueue('data2')
        self.assertEqual(queue.tail.data, 'data2')
        self.assertEqual(queue.tail.next_node, None)

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), '')
        queue.enqueue('test1')
        self.assertEqual(str(queue), 'test1')
        queue.enqueue('test2')
        self.assertEqual(str(queue), 'test1\ntest2')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)


if __name__ == '__main__':
    main()

