def power_value(serial: int, x: int, y: int) -> int:
    rack_id: int = x + 10
    power: int = rack_id * y
    power += serial
    power *= rack_id
    power %= 1000
    power //= 100
    power -= 5
    return power


def main_part_1(inp: int) -> str:
    grid: list[list[int]] = [
        [
            power_value(inp, x, y)
            for x in range(1, 301)
        ] for y in range(1, 301)
    ]

    best_power: int = 0
    best_index: str = "-/-"
    for x in range(297):
        for y in range(297):
            power: int = 0
            for x_diff in range(3):
                for y_diff in range(3):
                    power += grid[y + y_diff][x + x_diff]

            if power > best_power:
                best_index = f"{x + 1},{y + 1}"
                best_power = power

    return best_index


def main_part_2(inp: int) -> str:
    grid: list[list[int]] = [
        [
            power_value(inp, x, y)
            for x in range(1, 301)
        ] for y in range(1, 301)
    ]

    best_power: int = 0
    best_index: str = "-/-"

    total: list[list[int]] = [row.copy() for row in grid]
    for size in range(2, 300):
        for x in range(300 - size):
            for y in range(300 - size):
                for row in range(size):
                    total[y][x] += grid[y + row][x + size - 1]

                for col in range(size - 1):
                    total[y][x] += grid[y + size - 1][x + col]

                if total[y][x] > best_power:
                    best_index = f"{x + 1},{y + 1},{size}"
                    best_power = total[y][x]

        # print(size, best_power)
    return best_index


def main() -> None:
    test_input: int = 42
    test_output_part_1_expected: str = "21,61"
    test_output_part_2_expected: str = "232,251,12"

    input_file: int = 9306

    test_output_part_1: str = main_part_1(test_input)
    test_output_part_2: str = main_part_2(test_input)

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
