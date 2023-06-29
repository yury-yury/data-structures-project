from unittest import TestCase, main
from src.linked_list import Node, LinkedList


class TestLinkedList(TestCase):

    def test_node(self):
        n1 = Node({'id': 1}, None)
        n2 = Node({'id': 2}, n1)
        self.assertEqual(n1.data, {'id': 1})
        self.assertEqual(n2.data, {'id': 2})
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, n1.data)


    def test_slice(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        linked_list.insert_at_end({'id': 2})
        linked_list.insert_at_end({'id': 3})
        linked_list.insert_beginning({'id': 0})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.head.next_node.data, {'id': 1})
        self.assertEqual(linked_list.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(linked_list.head.next_node.next_node.next_node.data, {'id': 3})
        self.assertEqual(linked_list.head.next_node.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            res = linked_list.head.next_node.next_node.next_node.next_node.data

    def test_insert_beginning(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        self.assertEqual(linked_list.head.data, {'id': 1})
        self.assertEqual(linked_list.head.next_node, None)
        linked_list.insert_beginning({'id': 0})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.head.next_node, linked_list.storage[1])
        self.assertEqual(linked_list.head.next_node.data, {'id': 1})
        self.assertEqual(linked_list.head.next_node.next_node, None)


    def test_insert_at_end(self):
        linked_list = LinkedList()
        linked_list.insert_at_end({'id': 0})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.head.next_node, None)
        linked_list.insert_at_end({'id': 1})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.head.next_node, linked_list.storage[1])
        self.assertEqual(linked_list.head.next_node.data, {'id': 1})
        self.assertEqual(linked_list.head.next_node.next_node, None)

    def test_str(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        linked_list.insert_at_end({'id': 2})
        linked_list.insert_at_end({'id': 3})
        linked_list.insert_beginning({'id': 0})
        self.assertEqual(str(linked_list), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


if __name__ == '__main__':
    main()

