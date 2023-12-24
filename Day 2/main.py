def main_part_1(inp: list[str]) -> int:
    two: int = 0
    three: int = 0
    for line in inp:
        counts: list[int] = [line.count(char) for char in set(line.strip())]
        if 2 in counts:
            two += 1
        if 3 in counts:
            three += 1

    return two * three


def main_part_2(inp: list[str]) -> str:
    for line in inp:
        for other in inp:
            diffs: int = 0
            index: int = -1
            for char_1, char_2, i in zip(line, other, range(len(line))):
                if char_1 != char_2:
                    diffs += 1
                    index = i
            if diffs == 1:
                return line[:index] + line[index + 1:].strip()
    return ""


def main() -> None:
    file_location: str = "python/Advent of Code/2018/Day 2/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
