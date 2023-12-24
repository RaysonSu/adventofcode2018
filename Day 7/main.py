from collections import defaultdict


def next_step(rules: defaultdict[str, list[str]], remaining: list[str], finished: list[str]) -> str:
    for step in remaining:
        for check in rules[step]:
            if check not in finished:
                break
        else:
            return step

    return "."


def main_part_1(inp: list[str]) -> str:
    requirements: set[str] = set()
    rules: defaultdict[str, list[str]] = defaultdict(lambda: [].copy())
    for line in inp:
        requirements.add(line[5])
        requirements.add(line[36])

        rules[line[36]].append(line[5])

    steps: list[str] = sorted(list(requirements))
    ret: str = ""

    i: int = 0
    while steps:
        can_do: bool = True
        for req in rules[steps[i]]:
            can_do = can_do and req not in steps

        if can_do:
            ret += steps[i]
            del steps[i]
            i = 0
        else:
            i += 1

    return ret


def main_part_2(inp: list[str]) -> int:
    requirements: set[str] = set()
    rules: defaultdict[str, list[str]] = defaultdict(lambda: [].copy())
    for line in inp:
        requirements.add(line[5])
        requirements.add(line[36])

        rules[line[36]].append(line[5])

    steps: list[str] = sorted(list(requirements))
    finished: list[str] = []
    time: int = 0
    working: list[str] = [".", ".", ".", ".", "."]
    finishing: list[int] = [0, 0, 0, 0, 0]

    while len(finished) != len(requirements):
        for i in range(len(working)):
            if finishing[i] <= time:
                if working[i] != ".":
                    finished.append(working[i])
                    working[i] = "."

        for i in range(len(working)):
            if working[i] == ".":
                next_job: str = next_step(rules, steps, finished)
                if next_job == "":
                    continue
                if next_job in working:
                    continue
                working[i] = next_job
                finishing[i] = time + ord(next_job) - 4
                steps.remove(next_job)

        # print(" " * (4 - len(str(time))), end="")
        # print(time, end="")
        # for i in range(len(working)):
        #     print(" " * 4, end="")
        #     print(working[i], end="")
        # print(" " * 4, end="")
        # print("".join(finished))
        try:
            time = min([finishing[i] for i in range(5) if working[i] != "."])
        except ValueError as _:
            pass
    return time


def main() -> None:
    test_input: str = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: str = "CABDFE"
    test_output_part_2_expected: int = 253

    file_location: str = "python/Advent of Code/2018/Day 7/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = [x.replace("\n", "") for x in input_file]

    test_output_part_1: str = main_part_1(test_input_parsed)
    test_output_part_2: int = main_part_2(test_input_parsed)

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
