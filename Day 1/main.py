OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> int:
    return sum([int(x.strip()) for x in inp])


def main_part_2(inp: list[str]) -> int:
    seen: set[int] = set()
    index: int = 0
    cur: int = 0
    while cur not in seen:
        seen.add(cur)
        cur += int(inp[index])
        index += 1
        index %= len(inp)

    return cur


def main() -> None:
    test_input: str = """+7
+7
-2
-7
-4"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1
    test_output_part_2_expected: OUTPUT_TYPE = 14

    file_location: str = "python/Advent of Code/2018/Day 1/input.txt"
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
