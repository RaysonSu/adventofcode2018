OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[tuple[int, int, int, int]]:
    ret: list[tuple[int, int, int, int]] = []
    for line in inp:
        ret.append(
            eval(f"({''.join([x for x in line if x in '1234567890-,'])})"))

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    const: list[tuple[int, int, int, int]] = parse_inp(inp)

    ret: int = 0
    while const:
        curr: set[tuple[int, int, int, int]] = {const.pop(0)}
        ret += 1
        while curr:
            new_curr: set[tuple[int, int, int, int]] = set()
            for x0, y0, z0, t0 in const:
                for x1, y1, z1, t1 in curr:
                    if abs(x1 - x0) + abs(y1 - y0) + abs(z1 - z0) + abs(t0 - t1) <= 3:
                        new_curr.add((x0, y0, z0, t0))

            for point in new_curr:
                const.remove(point)

            curr = new_curr

    return ret


def main() -> None:
    test_input: str = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 8

    file_location: str = "python/Advent of Code/2018/Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()


if __name__ == "__main__":
    main()
