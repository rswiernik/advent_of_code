import sys
from dataclasses import dataclass
from typing import List, Set


class Room(object):
    def __init__(self, name):
        self.name: str = name
        self.neighbors: List[Room] = []

    def add_neighbor(self, room):
        if room not in self.neighbors:
            self.neighbors.append(room)

    def is_big(self):
        return self.name.upper() == self.name

    def is_small(self):
        return self.name.lower() == self.name

    def __repr__(self):
        return 'Room("{}" -> {})'.format(
            self.name,
            [x.name for x in self.neighbors]
        )


def crawl(room: Room, path: List[Room], visited: Set[Room]) -> List[List[Room]]:
    print(room)
    print(path)
    print(visited)
    print('------')
    v = []
    v.extend(visited)
    if room.is_small():
        v.append(room)

    p = []
    p.extend(path)
    p.append(room)

    # End case
    if room.name == 'end':
        return [p]

    neighbor_paths = []
    for neighbor in room.neighbors:
        if neighbor in v:
            continue
        neighbor_paths.extend(
            crawl(
                neighbor,
                p,
                v,
            )
        )

    return neighbor_paths




if __name__ == "__main__":
    in_file = sys.argv[1]

    room_by_name = {}
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                (left, right) = line.strip().split('-')

                def init_room(pointer, name):
                    pointer = room_by_name.get(name)
                    if not pointer:
                        room_by_name[name] = Room(name)
                        pointer = room_by_name.get(name)
                    return pointer

                a = None
                a = init_room(a, left)

                b = None
                b = init_room(b, right)

                a.add_neighbor(b)
                b.add_neighbor(a)

    # print(room_by_name)

    paths = crawl(room_by_name['start'], [], [])
    print('\n'.join([str([i.name for i in x]) for x in paths]))
    print(len(paths))



