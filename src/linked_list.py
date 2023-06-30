class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data: dict = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.storage = []

    @property
    def head(self):
        if not self.storage:
            return None
        else:
            return self.storage[0]

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        next_node = None
        if self.storage:
            next_node = self.storage[0]
        self.storage.insert(0, Node(data=data, next_node=next_node))


    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node: Node = Node(data=data)
        if self.storage:
            self.storage[-1].next_node = node
        self.storage.append(node)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node: Node = self.head
        if node is None:
            return str(None)

        ll_string: str = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self) -> list:
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next_node
        return result

    def get_data_by_id(self, search_id: int) -> dict:
        node: Node = self.head
        while node:
            # if isinstance(node.data, dict):
            try:
                if ('id', search_id) in node.data.items():
                    return node.data
            except Exception:
                print('The value is not a dictionary.')

            node = node.next_node

