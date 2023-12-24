OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> str:
    seen: list[tuple[int, int, int, int]] = []
    for row_index, row in enumerate(inp):
        for col_index, char in enumerate(row):
            if char in "<v>^":
                seen.append((row_index, col_index, ">^<v".index(char), 0))

    locations: list[tuple[int, int]] = [minecart[:2]
                                        for minecart in seen]
    directions: list[tuple[int, int]] = [minecart[2:]
                                         for minecart in seen]

    while True:
        for i in range(len(locations)):
            new_loc: tuple[int, int] = (
                locations[i][0] + [0, -1, 0, 1][directions[i][0]],
                locations[i][1] + [1, 0, -1, 0][directions[i][0]]
            )

            tile = inp[new_loc[0]][new_loc[1]]

            new_direction: tuple[int, int]
            if tile == "\\":
                new_direction = (3 - directions[i][0], directions[i][1])
            elif tile == "/":
                new_direction = (
                    [1, 0, 3, 2][directions[i][0]], directions[i][1])
            elif tile == "+":
                new_direction = (
                    (directions[i][0] - directions[i][1] + 1) % 4, (directions[i][1] + 1) % 3)
            else:
                new_direction = directions[i]

            if new_loc in locations:
                return f"{new_loc[1]},{new_loc[0]}"
            else:
                locations[i] = new_loc
                directions[i] = new_direction

        directions = [x for _, x in sorted(zip(locations, directions))]
        locations.sort()


def main_part_2(inp: list[str]) -> str:
    seen: list[tuple[int, int, int, int]] = []
    for row_index, row in enumerate(inp):
        for col_index, char in enumerate(row):
            if char in "<v>^":
                seen.append((row_index, col_index, ">^<v".index(char), 0))

    locations: list[tuple[int, int]] = [minecart[:2]
                                        for minecart in seen]
    directions: list[tuple[int, int]] = [minecart[2:]
                                         for minecart in seen]

    while len(locations) > 1:
        for i in range(len(locations)):
            if locations[i] == (-1, -1):
                continue

            new_loc: tuple[int, int] = (
                locations[i][0] + [0, -1, 0, 1][directions[i][0]],
                locations[i][1] + [1, 0, -1, 0][directions[i][0]]
            )

            tile = inp[new_loc[0]][new_loc[1]]

            new_direction: tuple[int, int]
            if tile == "\\":
                new_direction = (3 - directions[i][0], directions[i][1])
            elif tile == "/":
                new_direction = (
                    [1, 0, 3, 2][directions[i][0]], directions[i][1])
            elif tile == "+":
                new_direction = (
                    (directions[i][0] - directions[i][1] + 1) % 4, (directions[i][1] + 1) % 3)
            else:
                new_direction = directions[i]

            if new_loc in locations:
                locations[i] = (-1, -1)
                directions[i] = (-1, -1)
                directions[locations.index(new_loc)] = (-1, -1)
                locations[locations.index(new_loc)] = (-1, -1)
            else:
                locations[i] = new_loc
                directions[i] = new_direction

        while (-1, -1) in locations:
            locations.remove((-1, -1))

        while (-1, -1) in directions:
            directions.remove((-1, -1))

        directions = [x for _, x in sorted(zip(locations, directions))]
        locations.sort()

    return f"{locations[0][1]},{locations[0][0]}"


def main() -> None:
    test_input: str = """/>-<\  
|   |  
| /<+-\\
| | | v
\>+</ |
  |   ^
  \<->/ """
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: str = "2,0"
    test_output_part_2_expected: str = "6,4"

    file_location: str = "python/Advent of Code/2018/Day 13/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: str = main_part_1(test_input_parsed)
    test_output_part_2: str = main_part_2(test_input_parsed)

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
