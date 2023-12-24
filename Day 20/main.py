from collections import defaultdict
OUTPUT_TYPE = int


def evaluate_path(regex: str) -> int:
    if "(" not in regex:
        return len(regex)

    depth: int = 0
    ret: int = 0
    tmp: str = ""
    values: list[int] = []
    for char in regex:
        if depth == 0 and char not in "(|)":
            ret += 1

        if depth == 1 and char not in "|)":
            tmp += char

        if depth == 1 and char == "|":
            values.append(evaluate_path(tmp))
            tmp = ""

        if depth == 1 and char == ")":
            values.append(evaluate_path(tmp))
            tmp = ""
            ret += max(values)
            values = []

        if depth >= 2:
            tmp += char

        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    regex: str = inp[0].strip()[1:-1]
    replaced: str = ""
    while replaced != regex:
        replaced = regex
        regex = regex.replace("NS", "").replace(
            "SN", "").replace("WE", "").replace("EW", "")

    return evaluate_path(regex)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    graph: defaultdict[int, list[int]] = defaultdict(lambda: [])
    stack: list[int] = []
    location: int = 0

    for i in inp[0].strip():
        if i == "W":
            graph[location].append(location - 1)
            location -= 1
        elif i == "E":
            graph[location].append(location + 1)
            location += 1
        elif i == "N":
            graph[location].append(location - 65536)
            location -= 65536
        elif i == "S":
            graph[location].append(location + 65536)
            location += 65536
        elif i == "(":
            stack.append(location)
        elif i == "|":
            location = stack[-1]
        elif i == ")":
            stack.pop()

    depths: defaultdict[int, int] = defaultdict(lambda: 100000000000)
    points: list[tuple[int, int]] = [(0, 0)]
    while points:
        depth: int
        location: int
        depth, location = points.pop(0)

        depths[location] = depth
        for neighbour in graph[location]:
            new_depth: int = depth + 1
            if depths[neighbour] < new_depth:
                continue

            points.append((new_depth, neighbour))

    ret: int = 0
    for i in depths.values():
        if i >= 1000:
            ret += 1

    return ret


def main() -> None:
    test_input: str = """^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 31
    test_output_part_2_expected: OUTPUT_TYPE = 0

    file_location: str = "python/Advent of Code/2018/Day 20/input.txt"
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
