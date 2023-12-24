from math import log2
from typing import Callable
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[tuple[int, int, int, int]]:
    ret: list[tuple[int, int, int, int]] = []
    for line in inp:
        ret.append(
            eval(f"({''.join([x for x in line if x in '1234567890-,'])})"))

    return ret


def compute_mininum_radius(nanobots: list[tuple[int, int, int, int]]) -> int:
    return 2 ** int(log2(min([r for _, _, _, r in nanobots]))) * 16


def compute_initial_bounds(nanobots: list[tuple[int, int, int, int]]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    base_radius: int = compute_mininum_radius(nanobots)

    min_x: int = min([x for x, _, _, _ in nanobots])
    max_x: int = max([x for x, _, _, _ in nanobots])
    min_y: int = min([y for _, y, _, _ in nanobots])
    max_y: int = max([y for _, y, _, _ in nanobots])
    min_z: int = min([z for _, _, z, _ in nanobots])
    max_z: int = max([z for _, _, z, _ in nanobots])

    return (
        ((min_x // base_radius) * base_radius,
         -(-max_x // base_radius) * base_radius),
        ((min_y // base_radius) * base_radius,
         -(-max_y // base_radius) * base_radius),
        ((min_z // base_radius) * base_radius,
         -(-max_z // base_radius) * base_radius)
    )


def coord_checker(nano_bots: list[tuple[int, int, int, int]]) -> Callable[[tuple[int, int, int]], int]:
    def count_points(coord: tuple[int, int, int]):
        x: int
        y: int
        z: int
        x, y, z = coord

        ret: int = 0
        for nano_x, nano_y, nano_z, nano_r in nano_bots:
            if abs(nano_x - x) + abs(nano_y - y) + abs(nano_z - z) <= nano_r:
                ret += 1

        return ret

    return count_points


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    nano_bots: list[tuple[int, int, int, int]] = parse_inp(inp)
    nano_bots.sort(key=lambda x: x[-1])

    base_x: int
    base_y: int
    base_z: int
    radius: int

    base_x, base_y, base_z, radius = nano_bots[-1]
    ret: int = 0
    for x, y, z, _ in nano_bots:
        if abs(base_x - x) + abs(base_y - y) + abs(base_z - z) <= radius:
            ret += 1

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    nanobots: list[tuple[int, int, int, int]] = parse_inp(inp)
    base_radius: int = compute_mininum_radius(nanobots)

    x_bounds: tuple[int, int]
    y_bounds: tuple[int, int]
    z_bounds: tuple[int, int]

    x_bounds, y_bounds, z_bounds = compute_initial_bounds(nanobots)

    checker: Callable[[tuple[int, int, int]], int] = coord_checker(nanobots)

    while base_radius:
        best: int = 0
        best_coords: list[tuple[int, int, int]] = []
        for x in range(x_bounds[0], x_bounds[1] + 1, base_radius):
            for y in range(y_bounds[0], y_bounds[1] + 1, base_radius):
                for z in range(z_bounds[0], z_bounds[1] + 1, base_radius):
                    in_range: int = checker((x, y, z))
                    if in_range > best:
                        best = in_range
                        best_coords = [(x, y, z)]
                    elif in_range == best:
                        best_coords.append((x, y, z))

        best_coords.sort(key=sum)
        best_point = best_coords[0]
        x_bounds = (best_point[0] - base_radius, best_point[0] + base_radius)
        y_bounds = (best_point[1] - base_radius, best_point[1] + base_radius)
        z_bounds = (best_point[2] - base_radius, best_point[2] + base_radius)

        base_radius //= 2

        # print(best, len(best_coords), best_point)

    return sum(best_point)


def main() -> None:
    test_input: str = """pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 6
    test_output_part_2_expected: OUTPUT_TYPE = 36

    file_location: str = "python/Advent of Code/2018/Day 23/input.txt"
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
