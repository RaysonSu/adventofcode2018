OUTPUT_TYPE = int


def str_assign(string: str, index: int, value: str) -> str:
    return string[:index] + value + string[index + 1:]


def generate_grid(width: int, length: int) -> list[str]:
    return [" " * width for _ in range(length)]


def add_point(grid: list[str], point: list[int]) -> None:
    try:
        while grid[point[1]][point[0]] == " ":
            point[1] += 1
    except IndexError as _:
        return

    point[1] -= 1

    low: list[int] = point.copy()
    high: list[int] = point.copy()

    while grid[low[1]][low[0]] == " " and grid[low[1] + 1][low[0]] in "#~":
        low[0] -= 1

    low[0] += 1

    while grid[high[1]][high[0]] == " " and grid[high[1] + 1][high[0]] in "#~":
        high[0] += 1

    high[0] -= 1

    backup: bool = True

    if grid[low[1] + 1][low[0] - 1] == " ":
        if grid[low[1]][low[0] - 1] == " ":
            add_point(grid, [low[0] - 1, low[1]])
        backup = False

    if grid[high[1] + 1][high[0] + 1] == " ":
        if grid[high[1]][high[0] + 1] == " ":
            add_point(grid, [high[0] + 1, high[1]])
        backup = False

    if backup:
        for x in range(low[0], high[0] + 1):
            grid[low[1]] = str_assign(grid[low[1]], x, "~")


def main_part_1(inp: list[str]) -> int:
    grid: list[str] = generate_grid(1000, 2040)
    for line in inp:
        constant: int
        variable_low: int
        variable_high: int

        constant = int(line.split(", ")[0][2:])
        variable_low = int(line.split(", ")[1].split("..")[0][2:])
        variable_high = int(line.split(", ")[1].split("..")[1])
        if line[0] == "x":
            for y in range(variable_low, variable_high + 1):
                grid[y] = str_assign(grid[y], constant, "#")
        else:
            for x in range(variable_low, variable_high + 1):
                grid[constant] = str_assign(grid[constant], x, "#")

    while "#" not in grid[-2]:
        grid.pop()

    prev: list[str] = []
    while prev != grid:
        prev = grid.copy()
        add_point(grid, [500, 0])

    initial_point: tuple[int, int, int] = (500, 0, 0)
    points: list[tuple[int, int, int]] = [initial_point]
    while points:
        x: int
        y: int
        direction: int

        x, y, direction = points.pop(0)
        grid[y] = str_assign(grid[y], x, "|")

        if y == len(grid) - 1:
            continue

        lower_tile: str = grid[y + 1][x]
        if lower_tile == " ":
            points.append((x, y + 1, 0))
            continue

        if lower_tile == "|":
            continue

        left_tile: str = grid[y][x - 1]
        right_tile: str = grid[y][x + 1]

        if left_tile == " " and direction != 2:
            points.append((x - 1, y, 1))

        if right_tile == " " and direction != 1:
            points.append((x + 1, y, 2))

    while "#" not in grid[0]:
        grid.pop(0)

    while "#" not in grid[-1]:
        grid.pop()

    ret: int = 0
    for row in grid:
        ret += row.count("~") + row.count("|")

    return ret


def main_part_2(inp: list[str]) -> int:
    grid: list[str] = generate_grid(1000, 2040)
    for line in inp:
        constant: int
        variable_low: int
        variable_high: int

        constant = int(line.split(", ")[0][2:])
        variable_low = int(line.split(", ")[1].split("..")[0][2:])
        variable_high = int(line.split(", ")[1].split("..")[1])
        if line[0] == "x":
            for y in range(variable_low, variable_high + 1):
                grid[y] = str_assign(grid[y], constant, "#")
        else:
            for x in range(variable_low, variable_high + 1):
                grid[constant] = str_assign(grid[constant], x, "#")

    while "#" not in grid[-2]:
        grid.pop()

    prev: list[str] = []
    while prev != grid:
        prev = grid.copy()
        add_point(grid, [500, 0])

    ret: int = 0
    for row in grid:
        ret += row.count("~")

    return ret


def main() -> None:
    test_input: str = """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 57
    test_output_part_2_expected: OUTPUT_TYPE = 29

    file_location: str = "python/Advent of Code/2018/Day 17/input.txt"
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
