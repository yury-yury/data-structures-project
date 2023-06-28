from typing import Optional


class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        """Конструктор класса Stack"""
        self.storage = []

    def __str__(self) -> str:
        return '\n'.join([item.data for item in self.storage])
        # return f"{self.__class__.__name__}"

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.storage) == 0:
            previous = None
        else:
            previous = self.storage[-1]
        current_value = Node(data, previous)
        self.storage.append(current_value)

    def pop(self) -> Node:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        deleted = self.storage.pop()
        return deleted

    @property
    def top(self) -> Optional[Node]:
        if len(self.storage) > 0:
            return self.storage[-1]
        elif len(self.storage) == 0:
            return None

