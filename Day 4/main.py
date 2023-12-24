from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp.sort()
    time_asleep: defaultdict[int, list[int]] = defaultdict(
        lambda: [0 for _ in range(60)].copy())
    total_time_asleep: defaultdict[int, int] = defaultdict(lambda: 0)

    active_guard: int = -1
    sleep_start: int = -1
    for line in inp:
        line = line.strip()
        if "begins shift" in line:
            active_guard = int(line[26:-13])
            sleep_start = -1
            continue

        if "falls" in line:
            if sleep_start == -1:
                sleep_start = int(line[15:-14])

            continue

        if "wakes" in line:
            if sleep_start != -1:
                time = int(line[15:-10])
                total_time_asleep[active_guard] += time - sleep_start
                for t in range(sleep_start, time):
                    time_asleep[active_guard][t] += 1
                sleep_start = -1

    best_guard: int = -1
    best_time: int = -1
    for guard, time in total_time_asleep.items():
        if best_time < time:
            best_guard = guard
            best_time = time

    best_minute: int = -1
    best_days: int = -1
    for minute, days in enumerate(time_asleep[best_guard]):
        if best_days < days:
            best_minute = minute
            best_days = days

    return best_guard * best_minute


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp.sort()
    time_asleep: defaultdict[int, list[int]] = defaultdict(
        lambda: [0 for _ in range(60)].copy())

    active_guard: int = -1
    sleep_start: int = -1
    for line in inp:
        line = line.strip()
        if "begins shift" in line:
            active_guard = int(line[26:-13])
            sleep_start = -1
            continue

        if "falls" in line:
            if sleep_start == -1:
                sleep_start = int(line[15:-14])

            continue

        if "wakes" in line:
            if sleep_start != -1:
                time = int(line[15:-10])
                for t in range(sleep_start, time):
                    time_asleep[active_guard][t] += 1
                sleep_start = -1

    best_guard: int
    best_minute: int
    best_days: int = -1
    for guard, minutes in time_asleep.items():
        for minute, days in enumerate(minutes):
            if best_days < days:
                best_days = days
                best_guard = guard
                best_minute = minute

    return best_guard * best_minute


def main() -> None:
    test_input: str = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 240
    test_output_part_2_expected: OUTPUT_TYPE = 4455

    file_location: str = "python/Advent of Code/2018/Day 4/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
