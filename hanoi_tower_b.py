from hanoi_tower import Tower


class Node:
    def __init__(self, code, next_item=None):
        self.code = code
        self.next_item = next_item


class Worker:
    def __init__(self, level):
        node1 = Node((level, 'start', 'end', 'buffer'))
        self.__code = None
        if level > 0:
            self.__code = Node((0, 'start', 'start', 'buffer'), node1)
            self.__create_code()

    def __create_code(self):
        code_item = self.__code
        prev_item = None
        while code_item:
            stop = True
            if code_item.code[0] > 1:
                stop = False
                value = self.__decode(code_item, *code_item.code)
                prev_item.next_item = value
            prev_item = code_item
            code_item = code_item.next_item
            if code_item is None and not stop:
                code_item = self.__code

    @staticmethod
    def __decode(code_item, level, start, end, buffer):
        if level > 1:
            step_1 = Node((level - 1, buffer, end, start), code_item.next_item)
            step_2 = Node((1, start, end, buffer), step_1)
            return Node((level - 1, start, buffer, end), step_2)
        return code_item

    @staticmethod
    def __move_1(start, end):
        end.push(start.pop())

    def solve(self, start, end, buffer):
        step = self.__code
        while step:
            self.__move_1(locals()[step.code[1]], locals()[step.code[2]])
            step = step.next_item


if __name__ == '__main__':
    n = 10
    tower_value = [item for item in range(1, n + 1)]
    tower_value.reverse()
    tower_a = Tower(tower_value, name='tower_a')
    tower_b = Tower(name='tower_b')
    tower_c = Tower(name='tower_c')

    puzzle = Worker(n)

    print(tower_a)
    puzzle.solve(tower_a, tower_c, tower_b)
    print(tower_c)
