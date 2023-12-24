OUTPUT_TYPE = int


def find_closest(points: list[tuple[int, int]], point: tuple[int, int]) -> int:
    best_distance: int = 10000000
    best_point: int = -1

    x: int
    y: int
    x, y = point

    count: int = -1

    for index, point in enumerate(points):
        point_x: int
        point_y: int

        point_x, point_y = point
        distance: int = abs(x - point_x) + abs(y - point_y)

        if distance < best_distance:
            best_distance = distance
            best_point = index
            count = 1
        elif distance == best_distance:
            count += 1

    if count != 1:
        return -1

    return best_point


def total_distance(points: list[tuple[int, int]], point: tuple[int, int]) -> int:
    return sum([abs(point[0] - x) + abs(point[1] - y) for x, y in points])


def count_row(points: list[tuple[int, int]], y: int) -> int:
    ret: int = 0
    for x in range(-4000, 4000):
        if total_distance(points, (x, y)) < 10000:
            ret += 1

    return ret


def count_all(points: list[tuple[int, int]]) -> int:
    ret: int = 0
    for y in range(-4000, 4000):
        ret += count_row(points, y)
    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    points: list[tuple[int, int]] = []
    for line in inp:
        points.append(eval(f"({line.strip()})"))

    banned: set[int] = set()
    total: list[int] = [0 for _ in range(len(inp) + 1)]
    min_x: int = min([x for x, _ in points]) - 100
    min_y: int = min([y for y, _ in points]) - 100
    max_x: int = max([x for x, _ in points]) + 100
    max_y: int = max([y for y, _ in points]) + 100

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total[find_closest(points, (x, y))] += 1

    for x in range(min_x - 1, max_x + 1):
        banned.add(find_closest(points, (x, min_y - 1)))
        banned.add(find_closest(points, (x, max_y + 1)))

    for y in range(min_y - 1, max_y + 1):
        banned.add(find_closest(points, (min_x - 1, y)))
        banned.add(find_closest(points, (max_x + 1, y)))

    best: int = 0
    for index, value in enumerate(total[:-1]):
        if index in banned:
            continue

        best = max(best, value)

    return best


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    points: list[tuple[int, int]] = []
    for line in inp:
        points.append(eval(f"({line.strip()})"))

    return count_all(points)


def main() -> None:
    test_input: str = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 17
    test_output_part_2_expected: OUTPUT_TYPE = 5554416

    file_location: str = "python/Advent of Code/2018/Day 6/input.txt"
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
