from typing import Optional


class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.storage = []

    def __str__(self) -> str:
        return '\n'.join([item.data for item in self.storage])

    def enqueue(self, data) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if len(self.storage) > 0:
            self.storage[-1].next_node = node
        self.storage.append(node)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if len(self.storage) == 0:
            return None
        item = self.storage.pop(0)
        return item.data

    @property
    def head(self) -> Optional[Node]:
        if len(self.storage) > 0:
            return self.storage[0]
        return None

    @property
    def tail(self):
        if len(self.storage) > 0:
            return self.storage[-1]
        return None
