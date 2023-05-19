class Tower:

    def __init__(self, value=None, name=None):
        if value is None:
            value = []
        self.__name = name
        self.__items = value

    def push(self, item):
        if len(self.__items) > 0 and self.__items[-1] <= item:
            raise ValueError(f'На вершине {self.__items[-1]}. Нельзя положить {item}')
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            raise KeyError('stack is empty')
        return self.__items.pop()

    def empty(self):
        return len(self.__items) == 0

    def print_level(self, level_value=None):
        if not level_value:
            return '      |'
        return f'{(max(self.__items) - level_value) * " "}{level_value * 2 * str(level_value)}'

    def __str__(self):

        nl = '\n'
        return f"{nl}{nl.join([self.print_level(item) for item in reversed(self.__items)] + [self.__name])}"


class Node:
    def __init__(self, level, next_item=None):
        self.level = level
        self.next_item = next_item

    @staticmethod
    def __move_1(start, end):
        end.push(start.pop())

    def execute(self, start, end, buffer):
        self.__move_1(start, buffer) if self.level <= 1 else self.next_item.execute(start, buffer, end)
        if self.level > 0:
            self.__move_1(start, end)
        self.__move_1(buffer, end) if self.level <= 1 else self.next_item.execute(buffer, end, start)


if __name__ == '__main__':
    n = 10
    tower_value = [item for item in range(1, n + 1)]
    tower_value.reverse()
    tower_a = Tower(tower_value, name='tower_a')
    tower_b = Tower(name='tower_b')
    tower_c = Tower(name='tower_c')

    node_prev = None
    node = None
    for level in range(n):
        node = Node(level, node_prev)
        node_prev = node

    print(tower_a)
    if node:
        node.execute(tower_a, tower_c, tower_b)
    print(tower_c)
