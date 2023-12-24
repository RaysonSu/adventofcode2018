OUTPUT_TYPE = int


class CellularAutomata:
    def __init__(self, rule: list[bool]) -> None:
        self.rule: list[bool] = rule
        self.points: list[int] = []

        self.determine_bounds()

    def add_point(self, points: int | list[int]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.append(point)
        else:
            self.points.append(points)
        self.determine_bounds()

    def determine_bounds(self) -> None:
        min_x: int = 10000
        max_x: int = -10000

        for x in self.points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)

        self.bounds = (min_x, max_x)

    def in_bound(self, x: int) -> bool:
        return self.bounds[0] <= x and x <= self.bounds[1]

    def determine_future_point(self, x: int) -> bool:
        lookup: int = 0
        for x_diff in range(-2, 3):
            lookup = lookup << 1
            if x + x_diff in self.points:
                lookup = lookup + 1

        return self.rule[lookup]

    def tick(self) -> None:
        new_points: list[int] = []
        for x in range(self.bounds[0] - 2, self.bounds[1] + 3):
            if self.determine_future_point(x):
                new_points.append(x)

        self.points = new_points
        self.determine_bounds()

    def __str__(self) -> str:
        ret: str = ""
        for x in range(self.bounds[0], self.bounds[1] + 1):
            if x in self.points:
                ret += "#"
            else:
                ret += "."

        return ret

    def __hash__(self) -> int:
        return hash(str(self))


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    rules: list[str] = inp[2:]
    rules.sort(reverse=True)

    rule: list[bool] = [char[-1] == "#" for char in rules]
    cell: CellularAutomata = CellularAutomata(rule)
    grid: list[int] = []

    for x, char in enumerate(inp[0][15:]):
        if char == "#":
            grid.append(x)

    cell.add_point(grid)
    for _ in range(20):
        cell.tick()

    return sum(cell.points)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    rules: list[str] = inp[2:]
    rules.sort(reverse=True)

    rule: list[bool] = [char[-1] == "#" for char in rules]
    cell: CellularAutomata = CellularAutomata(rule)
    grid: list[int] = []

    for x, char in enumerate(inp[0][15:]):
        if char == "#":
            grid.append(x)

    cell.add_point(grid)
    seen_hashes: list[int] = []
    hashed: int = hash(cell)
    total: int = 50000000000
    prev_count: int = -1
    curr_count: int = -1
    while hashed not in seen_hashes:
        cell.tick()
        seen_hashes.append(hashed)
        hashed = hash(cell)
        prev_count = curr_count
        curr_count = sum(cell.points)
        total -= 1

    return sum(cell.points) + total * (curr_count - prev_count)


def main() -> None:
    test_input: str = """initial state: #..#.#..##......###...###

..... => .
....# => .
...#. => .
...## => #
..#.. => #
..#.# => .
..##. => .
..### => .
.#... => #
.#..# => .
.#.#. => #
.#.## => #
.##.. => #
.##.# => .
.###. => .
.#### => #
#.... => .
#...# => .
#..#. => .
#..## => .
#.#.. => .
#.#.# => #
#.##. => .
#.### => #
##... => .
##..# => .
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
##### => ."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 325
    test_output_part_2_expected: OUTPUT_TYPE = 999999999374

    file_location: str = "python/Advent of Code/2018/Day 12/input.txt"
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
