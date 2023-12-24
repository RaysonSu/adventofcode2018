from __future__ import annotations

OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    polymer: str = inp[0].strip()
    prev_polymer: str = ""
    while polymer != prev_polymer:
        prev_polymer = polymer
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            polymer = polymer.replace(char + char.lower(), "")
            polymer = polymer.replace(char.lower() + char, "")

    return len(polymer)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    best: int = 10 ** 300
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        best = min(best, main_part_1(
            [inp[0].replace(char, "").replace(char.lower(), "")]))

    return best


def main() -> None:
    test_input: str = """dabAcCaCBAcCcaDA"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 10
    test_output_part_2_expected: OUTPUT_TYPE = 4

    file_location: str = "python/Advent of Code/2018/Day 5/input.txt"
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
