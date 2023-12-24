from __future__ import annotations
OUTPUT_TYPE = int


class Entity:
    def __init__(self, type: bool, x: int, y: int, hp: int = 200, power: int = 3) -> None:
        self.type: bool = type
        self.x: int = x
        self.y: int = y
        self.hp: int = hp
        self.power: int = power

        self.friends: list[Entity]
        self.enemies: list[Entity]
        self.all: list[Entity]
        self.map: list[str]
        self.other_set: bool = False

    def set_other_entities(self, friends: list[Entity], enemies: list[Entity], all_entities: list[Entity], field_map: list[str]) -> None:
        self.friends = friends
        self.enemies = enemies
        self.all = all_entities
        self.map = field_map
        self.other_set = True

    def find_targets(self) -> list[Entity]:
        return self.enemies

    def find_possible_destinations(self, targets: list[Entity]) -> list[tuple[int, int]]:
        destinations: list[tuple[int, int]] = []
        for target in targets:
            for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x: int = target.x + x_diff
                y: int = target.y + y_diff

                if self.map[y][x] != ".":
                    continue

                destination: tuple[int, int] = (x, y)

                if destination not in destinations:
                    destinations.append(destination)

        return destinations

    def find_target(self, destinations: list[tuple[int, int]]) -> tuple[int, int] | None:
        points_seen: set[tuple[int, int]] = set()
        edge: list[tuple[int, int]] = [(self.x, self.y)]
        possible_points: list[tuple[int, int]] = []

        while not possible_points:
            new_points: list[tuple[int, int]] = []
            for x, y in edge:
                for x_diff, y_diff in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_x: int = x + x_diff
                    new_y: int = y + y_diff

                    if self.map[new_y][new_x] != ".":
                        continue

                    if (new_x, new_y) in points_seen:
                        continue

                    if (new_x, new_y) in destinations:
                        possible_points.append((new_x, new_y))

                    new_points.append((new_x, new_y))
                    points_seen.add((new_x, new_y))

            if new_points == [] and possible_points == []:
                return None

            edge = new_points

        possible_points.sort(key=lambda x: (x[1], x[0]))

        return possible_points[0]

    def find_new_location(self, target: tuple[int, int]) -> tuple[int, int]:
        points_seen: set[tuple[int, int]] = set()
        edge: list[tuple[int, int]] = [target]
        possible_points: list[tuple[int, int]] = []
        destinations: list[tuple[int, int]] = [
            (self.x + 1, self.y),
            (self.x - 1, self.y),
            (self.x, self.y + 1),
            (self.x, self.y - 1)
        ]

        if target in destinations:
            return target

        while not possible_points:
            new_points: list[tuple[int, int]] = []
            for x, y in edge:
                for x_diff, y_diff in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_x: int = x + x_diff
                    new_y: int = y + y_diff

                    if self.map[new_y][new_x] != ".":
                        continue

                    if (new_x, new_y) in points_seen:
                        continue

                    if (new_x, new_y) in destinations:
                        possible_points.append((new_x, new_y))

                    new_points.append((new_x, new_y))
                    points_seen.add((new_x, new_y))

            edge = new_points

        possible_points.sort(key=lambda x: (x[1], x[0]))

        return possible_points[0]

    def determine_target_enemy(self) -> Entity | None:
        lowest_hp: int = 1000000000000000000000
        entity: Entity | None = None
        for enemy in self.enemies:
            distance: int = abs(enemy.x - self.x) + abs(enemy.y - self.y)
            if distance != 1:
                continue

            if enemy.hp >= lowest_hp:
                continue

            entity = enemy
            lowest_hp = enemy.hp

        return entity

    def do_all(self) -> int:
        if not self.other_set:
            raise RuntimeError("Well y'dun goofed up mate!")

        target_enemy: Entity | None = self.determine_target_enemy()
        if target_enemy:
            target_enemy.hp -= self.power
            index: int = self.all.index(target_enemy)
            if target_enemy.hp < 0:
                self.all.remove(target_enemy)
                self.enemies.remove(target_enemy)
                del target_enemy
                return index
            return -1

        targets: list[Entity] = self.find_targets()
        if len(targets) == 0:
            return -1

        possible_destinations: list[tuple[int, int]
                                    ] = self.find_possible_destinations(targets)
        target: tuple[int, int] | None = self.find_target(
            possible_destinations)
        if not target:
            return -1

        new_location: tuple[int, int] = self.find_new_location(target)

        self.x = new_location[0]
        self.y = new_location[1]

        target_enemy = self.determine_target_enemy()
        if target_enemy:
            target_enemy.hp -= self.power
            if target_enemy.hp < 0:
                self.all.remove(target_enemy)
                self.enemies.remove(target_enemy)
                del target_enemy
            return -1

        return -1


class Simulation:
    def __init__(self, grid: list[str]) -> None:
        self.entities: list[Entity] = []
        self.goblins: list[Entity] = []
        self.elfs: list[Entity] = []
        self.grid: list[str] = grid

        self.turns: int = 0

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
        if entity.type:
            entity.set_other_entities(
                self.elfs, self.goblins, self.entities, self.grid
            )
            self.elfs.append(entity)
        else:
            entity.set_other_entities(
                self.goblins, self.elfs, self.entities, self.grid
            )
            self.goblins.append(entity)

    def update_entites(self) -> None:
        if self.turns == 32:
            pass
        index: int = 0
        while index < len(self.entities):
            removed: int = self.entities[index].do_all()
            self.update_grid()
            if index < removed or removed == -1:
                index += 1

    def update_grid(self) -> None:
        for i in range(len(self.grid)):
            self.grid[i] = self.grid[i].replace("E", ".").replace("G", ".")

        for entity in self.entities:
            self.grid[entity.y] = str_assign(
                self.grid[entity.y],
                entity.x,
                "E" if entity.type else "G"
            )

    def sort_lists(self) -> None:
        self.entities.sort(key=lambda entity: (entity.y, entity.x))
        self.elfs.sort(key=lambda entity: (entity.y, entity.x))
        self.goblins.sort(key=lambda entity: (entity.y, entity.x))

    def total_hp(self) -> int:
        ret: int = 0
        for entity in self.entities:
            ret += entity.hp

        return ret

    def print_grid(self) -> None:
        for i, row in enumerate(self.grid):
            print(row, end="")
            for entity in self.entities:
                if entity.y == i:
                    print("   ", end="")
                    if entity.type:
                        print("E", end="")
                    else:
                        print("G", end="")

                    print(f"({entity.hp})", end="")
            print()
        print(self.turns)

    def tick(self) -> bool:
        # self.print_grid()
        self.sort_lists()
        self.update_entites()
        if len(self.elfs) == 0 or len(self.goblins) == 0:
            return False
        self.update_grid()
        self.turns += 1

        return True


def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]


def parse_inp(inp: list[str], req: int = 3) -> Simulation:
    inp = list(map(str.strip, inp))
    ret: Simulation = Simulation(inp)
    for row_index, row in enumerate(inp):
        for col_index, char in enumerate(row):
            if char == "E":
                ret.add_entity(Entity(
                    True,
                    col_index,
                    row_index,
                    power=req
                ))
            elif char == "G":
                ret.add_entity(Entity(
                    False,
                    col_index,
                    row_index
                ))

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    simulation = parse_inp(inp)
    while simulation.tick():
        pass

    return simulation.turns * simulation.total_hp()


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    init: int = 3
    while True:
        simulation: Simulation = parse_inp(inp.copy(), init)
        elfs: int = len(simulation.elfs)

        while simulation.tick():
            pass

        # simulation.print_grid()

        if len(simulation.elfs) == elfs:
            return simulation.turns * simulation.total_hp()

        init += 1
        # print(init)


def main() -> None:
    test_input: str = """#######       #######
#.E...#  
#.#..G#   
#.###.# 
#E#G#G#    
#...#G#       #...#.#
#######       #######"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 28944
    test_output_part_2_expected: OUTPUT_TYPE = 6308

    file_location: str = "python/Advent of Code/2018/Day 15/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
