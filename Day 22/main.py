from __future__ import annotations
import heapq
OUTPUT_TYPE = int


class State:
    def __init__(self,
                 grid: list[list[int]],
                 target: tuple[int, int],
                 location: tuple[int, int] = (0, 0),
                 gear: int = 1,
                 time: int = 0) -> None:

        self.grid: list[list[int]] = grid
        self.location: tuple[int, int] = location
        self.gear: int = gear
        self.time: int = time
        self.target: tuple[int, int] = target

    def generate_neighbours(self) -> list[tuple[int, State]]:
        ret: list[tuple[int, State]] = []
        for direction in range(4):
            new_location: tuple[int, int] = (
                self.location[0] + [1, 0, -1, 0][direction],
                self.location[1] + [0, -1, 0, 1][direction]
            )

            if not self.is_valid_coord(new_location):
                continue

            ret.append((1, State(
                self.grid,
                self.target,
                new_location,
                self.gear,
                self.time + 1
            )))

        ret.append((7, State(
            self.grid,
            self.target,
            self.location,
            3 - self.gear - self.grid[self.location[1]][self.location[0]]
        )))

        return ret

    def is_valid_coord(self, location: tuple[int, int]) -> bool:
        if location[0] < 0 or location[0] >= len(self.grid[0]):
            return False

        if location[1] < 0 or location[1] >= len(self.grid):
            return False

        if self.gear == self.grid[location[1]][location[0]]:
            return False

        return True

    def is_finished(self) -> bool:
        if self.location != self.target:
            return False

        if self.gear != 1:
            return False

        return True

    def __hash__(self) -> int:
        return hash(f"{self.location}//{self.gear}")

    def __lt__(self, other) -> bool:
        return hash(self) < hash(other)


def generate_grid(depth: int, size: tuple[int, int], target: tuple[int, int]) -> list[list[int]]:
    ret: list[list[int]] = []
    for y in range(size[1] + 1):
        row: list[int] = []
        for x in range(size[0] + 1):
            geo_index: int
            if x == 0 and y == 0:
                geo_index = 0
            elif (x, y) == target:
                geo_index = 0
            elif x == 0:
                geo_index = 48271 * y
            elif y == 0:
                geo_index = 16807 * x
            else:
                geo_index = ret[y - 1][x] * row[x - 1]

            row.append((geo_index + depth) % 20183)

        ret.append(row)

    for y in range(size[1] + 1):
        for x in range(size[0] + 1):
            ret[y][x] %= 3

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    depth: int = int(inp[0][7:])
    row: int = int(inp[1].split(",")[0][8:])
    col: int = int(inp[1].split(",")[1])

    return sum(map(sum, generate_grid(depth, (row, col), (row, col))))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    depth: int = int(inp[0][7:])
    row: int = int(inp[1].split(",")[0][8:])
    col: int = int(inp[1].split(",")[1])

    grid: list[list[int]] = generate_grid(
        depth, (max(row, col) * 2, max(row, col) * 2), (row, col))

    initial_state: State = State(grid, (row, col))
    best_found: dict[int, int] = {hash(initial_state): 0}
    states: list[tuple[int, State]] = [(0, initial_state)]

    while states:
        current_score: int
        current_state: State

        current_score, current_state = heapq.heappop(states)

        if current_state.is_finished():
            return current_score

        for cost, new_state in current_state.generate_neighbours():
            new_cost: int = current_score + cost
            hashed_state: int = hash(new_state)

            if hashed_state in best_found.keys() and best_found[hashed_state] <= new_cost:
                continue

            best_found[hashed_state] = new_cost
            heapq.heappush(states, (new_cost, new_state))

    return -1


def main() -> None:
    test_input: str = """depth: 510
target: 10,10"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 114
    test_output_part_2_expected: OUTPUT_TYPE = 45

    file_location: str = "python/Advent of Code/2018/Day 22/input.txt"
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
