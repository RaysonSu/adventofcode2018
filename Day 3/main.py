OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in inp:
        data: list[str] = line.split(" ")
        base_x: int = int(data[2].split(",")[0])
        base_y: int = int(data[2].split(",")[1][:-1])
        x_range: int = int(data[3].split("x")[0])
        y_range: int = int(data[3].split("x")[1])
        for x in range(base_x, base_x + x_range):
            for y in range(base_y, base_y + y_range):
                grid[y][x] += 1

    ret: int = 0
    for row in grid:
        for box in row:
            if box > 1:
                ret += 1

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in inp:
        data: list[str] = line.split(" ")
        base_x: int = int(data[2].split(",")[0])
        base_y: int = int(data[2].split(",")[1][:-1])
        x_range: int = int(data[3].split("x")[0])
        y_range: int = int(data[3].split("x")[1])
        for x in range(base_x, base_x + x_range):
            for y in range(base_y, base_y + y_range):
                grid[y][x] += 1

    for line in inp:
        data = line.split(" ")
        claim: int = int(data[0][1:])
        base_x = int(data[2].split(",")[0])
        base_y = int(data[2].split(",")[1][:-1])
        x_range = int(data[3].split("x")[0])
        y_range = int(data[3].split("x")[1])

        failed: int = False
        for x in range(base_x, base_x + x_range):
            for y in range(base_y, base_y + y_range):
                if grid[y][x] != 1:
                    failed = True

        if not failed:
            return claim
    return -1


def main() -> None:
    test_input: str = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4
    test_output_part_2_expected: OUTPUT_TYPE = 3

    file_location: str = "python/Advent of Code/2018/Day 3/input.txt"
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
