from collections import namedtuple, OrderedDict
import random


MenuItem = namedtuple('MenuItem', ('parent', 'id', 'name'))
items = (
    MenuItem(0, 1, 'Первый'),

    MenuItem(1, 11, 'Первый вложенный 1'),
    MenuItem(11, 111, 'Первый вложенный 1 вложенный 1'),
    MenuItem(11, 112, 'Первый вложенный 1 вложенный 2'),
    MenuItem(11, 113, 'Первый вложенный 1 вложенный 3'),

    MenuItem(1, 12, 'Первый вложенный 2'),
    MenuItem(12, 121, 'Первый вложенный 2 вложенный 1'),
    MenuItem(12, 122, 'Первый вложенный 2 вложенный 2'),
    MenuItem(12, 123, 'Первый вложенный 2 вложенный 3'),

    MenuItem(1, 13, 'Первый вложенный 3'),
    MenuItem(13, 131, 'Первый вложенный 3 вложенный 1'),
    MenuItem(13, 132, 'Первый вложенный 3 вложенный 2'),
    MenuItem(13, 133, 'Первый вложенный 3 вложенный 3'),

    MenuItem(0, 2, 'Второй'),

    MenuItem(2, 21, 'Второй вложенный 1'),
    MenuItem(21, 211, 'Второй вложенный 1 вложенный 1'),
    MenuItem(21, 212, 'Второй вложенный 1 вложенный 2'),
    MenuItem(21, 213, 'Второй вложенный 1 вложенный 3'),

    MenuItem(2, 22, 'Второй вложенный 2'),
    MenuItem(22, 221, 'Второй вложенный 2 вложенный 1'),
    MenuItem(22, 222, 'Второй вложенный 2 вложенный 2'),
    MenuItem(22, 223, 'Второй вложенный 2 вложенный 3'),

    MenuItem(2, 23, 'Второй вложенный 3'),
    MenuItem(23, 231, 'Второй вложенный 3 вложенный 1'),
    MenuItem(23, 232, 'Второй вложенный 3 вложенный 2'),
    MenuItem(23, 233, 'Второй вложенный 3 вложенный 3'),

    MenuItem(0, 3, 'Третий'),

    MenuItem(3, 31, 'Третий вложенный 1'),
    MenuItem(31, 311, 'Третий вложенный 1 вложенный 1'),
    MenuItem(31, 312, 'Третий вложенный 1 вложенный 2'),
    MenuItem(31, 313, 'Третий вложенный 1 вложенный 3'),

    MenuItem(3, 32, 'Третий вложенный 2'),
    MenuItem(32, 321, 'Третий вложенный 2 вложенный 1'),
    MenuItem(32, 322, 'Третий вложенный 2 вложенный 2'),
    MenuItem(32, 323, 'Третий вложенный 2 вложенный 3'),

    MenuItem(3, 33, 'Третий вложенный 3'),
    MenuItem(33, 331, 'Третий вложенный 3 вложенный 1'),
    MenuItem(33, 332, 'Третий вложенный 3 вложенный 2'),
    MenuItem(33, 333, 'Третий вложенный 3 вложенный 3'),
)
randomized = list(items)
random.shuffle(randomized)


def collect_children(menu_items: list[MenuItem], parent=0) -> OrderedDict:
    if not isinstance(menu_items, list):
        menu_items = list(menu_items)

    children = [item for item in menu_items if item.parent == parent]
    children = sorted(children, key=lambda x: x.name)
    OrderedDict()
    if len(children):
        return {item: collect_children(menu_items, item.id)
                for item in children}
    return {}


def print_tree(tree: dict, step: str = ''):
    for parent, children in tree.items():
        print(step, parent.name)
        print_tree(children, step=step + '  ')


tree = collect_children(randomized)
print_tree(tree)
