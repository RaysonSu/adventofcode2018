OUTPUT_TYPE = int


class CellularAutomata:
    def __init__(self, data: list[str]) -> None:
        self.states: list[list[int]] = [
            [".|#".index(char) for char in row.strip()]
            for row in data
        ]

    def __str__(self) -> str:
        ret: str = ""
        for row in self.states:
            for char in row:
                ret += ".|#"[char]
            ret += "\n"
        return ret

    def __hash__(self) -> int:
        return hash(str(self))

    def in_bound(self, x: int, y: int) -> bool:
        return 0 <= x and x < len(self.states[0]) and 0 <= y and y < len(self.states)

    def count_neighbours(self, x: int, y: int) -> list[int]:
        counts: list[int] = [0, 0, 0]
        for x_diff, y_diff in [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            new_x: int = x + x_diff
            new_y: int = y + y_diff

            if not self.in_bound(new_x, new_y):
                continue

            counts[self.states[new_y][new_x]] += 1

        return counts

    def determine_future_point(self, x: int, y: int) -> bool:
        current: int = self.states[y][x]

        two: int
        three: int
        _, two, three = tuple(self.count_neighbours(x, y))

        if current == 0:
            if two >= 3:
                return 1
            return 0

        if current == 1:
            if three >= 3:
                return 2
            return 1

        if current == 2:
            if three >= 1 and two >= 1:
                return 2
            return 0

        return -1

    def tick(self) -> None:
        self.states = [
            [self.determine_future_point(x, y)
             for x in range(len(self.states[0]))]
            for y in range(len(self.states))
        ]

    def counts(self) -> list[int]:
        counts: list[int] = [0, 0, 0]
        for row in self.states:
            for i in range(3):
                counts[i] += row.count(i)

        return counts

    def value(self) -> int:
        counts: list[int] = self.counts()
        return counts[1] * counts[2]


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    cell: CellularAutomata = CellularAutomata(inp)

    for _ in range(10):
        cell.tick()

    return cell.value()


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    cell: CellularAutomata = CellularAutomata(inp)

    seen: list[int] = []
    values: list[int] = []

    while hash(cell) not in seen:
        seen.append(hash(cell))
        values.append(cell.value())
        cell.tick()

    initial: int = seen.index(hash(cell))
    period: int = len(seen) - initial

    periodic_values: list[int] = values[initial:]

    return periodic_values[(1000000000 - initial) % period]


def main() -> None:
    test_input: str = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1147
    test_output_part_2_expected: OUTPUT_TYPE = 0

    file_location: str = "python/Advent of Code/2018/Day 18/input.txt"
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
