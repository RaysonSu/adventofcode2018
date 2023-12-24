from collections import deque

OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[int, int]:
    raw_list: list[int] = [
        int(x)
        for x in "".join([
            char
            for char in inp[0]
            if char.isnumeric() or char == " "
        ]).split(" ")
        if x != ""]
    return raw_list[0], raw_list[1]


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    players: int
    marble_count: int

    players, marble_count = parse_inp(inp)
    score: list[int] = [0 for _ in range(players)]
    marbles: deque[int] = deque()

    marbles.append(0)

    for index in range(1, marble_count + 1):
        if index % 23 == 0:
            score[index % players] += index
            marbles.rotate(7)
            score[index % players] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(index)
    return max(score)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    players: int
    marble_count: int

    players, marble_count = parse_inp(inp)
    score: list[int] = [0 for _ in range(players)]
    marbles: deque[int] = deque()

    marbles.append(0)

    for index in range(1, marble_count * 100 + 1):
        if index % 23 == 0:
            score[index % players] += index
            marbles.rotate(7)
            score[index % players] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(index)

    return max(score)


def main() -> None:
    test_input: str = """9 players; last marble is worth 25 points"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 32
    test_output_part_2_expected: OUTPUT_TYPE = 22563

    file_location: str = "python/Advent of Code/2018/Day 9/input.txt"
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
