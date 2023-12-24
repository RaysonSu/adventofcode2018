OUTPUT_TYPE = int


def instruction(ins: str, inp_a: int, inp_b: int, inp_c: int, regs: list[int]) -> None:
    if ins == "addr":
        regs[inp_c] = regs[inp_a] + regs[inp_b]
        return
    elif ins == "addi":
        regs[inp_c] = regs[inp_a] + inp_b
        return
    elif ins == "mulr":
        regs[inp_c] = regs[inp_a] * regs[inp_b]
        return
    elif ins == "muli":
        regs[inp_c] = regs[inp_a] * inp_b
        return
    elif ins == "banr":
        regs[inp_c] = regs[inp_a] & regs[inp_b]
        return
    elif ins == "bani":
        regs[inp_c] = regs[inp_a] & inp_b
        return
    elif ins == "borr":
        regs[inp_c] = regs[inp_a] | regs[inp_b]
        return
    elif ins == "bori":
        regs[inp_c] = regs[inp_a] | inp_b
        return
    elif ins == "setr":
        regs[inp_c] = regs[inp_a]
        return
    elif ins == "seti":
        regs[inp_c] = inp_a
        return
    elif ins == "gtir":
        regs[inp_c] = int(inp_a > regs[inp_b])
        return
    elif ins == "gtri":
        regs[inp_c] = int(regs[inp_a] > inp_b)
        return
    elif ins == "gtrr":
        regs[inp_c] = int(regs[inp_a] > regs[inp_b])
        return
    elif ins == "eqir":
        regs[inp_c] = int(inp_a == regs[inp_b])
        return
    elif ins == "eqri":
        regs[inp_c] = int(regs[inp_a] == inp_b)
        return
    elif ins == "eqrr":
        regs[inp_c] = int(regs[inp_a] == regs[inp_b])
        return


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    opcodes: list[str] = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr",
                          "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

    index: int = 0
    count: int = 0

    while inp[index] != "":
        start: list[int] = eval(inp[index][8:])
        end: list[int] = eval(inp[index + 2][8:])

        inp_a: int
        inp_b: int
        inp_c: int
        inp_a, inp_b, inp_c = tuple(map(int, inp[index + 1].split()))[1:]

        possibilities: int = 0
        for opcode in opcodes:
            start_tmp: list[int] = start.copy()
            instruction(opcode, inp_a, inp_b, inp_c, start_tmp)
            if start_tmp == end:
                possibilities += 1

        if possibilities >= 3:
            count += 1

        index += 4

    return count


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp = list(map(str.strip, inp))
    opcodes: list[str] = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr",
                          "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    opcode_possibilities: list[set[str]] = [
        set(opcodes.copy()) for _ in range(16)]

    index: int = 0

    while inp[index] != "":
        start: list[int] = eval(inp[index][8:])
        end: list[int] = eval(inp[index + 2][8:])

        op: int
        inp_a: int
        inp_b: int
        inp_c: int
        op, inp_a, inp_b, inp_c = tuple(map(int, inp[index + 1].split()))

        possibilities: set[str] = set()
        for opcode in opcodes:
            start_tmp: list[int] = start.copy()
            instruction(opcode, inp_a, inp_b, inp_c, start_tmp)
            if start_tmp == end:
                possibilities.add(opcode)

        opcode_possibilities[op].intersection_update(possibilities)

        index += 4

    while max(map(len, opcode_possibilities)) > 1:
        for i in range(16):
            if len(opcode_possibilities[i]) != 1:
                continue

            for j in range(16):
                if i == j:
                    continue

                opcode_possibilities[j] = opcode_possibilities[j].difference(
                    opcode_possibilities[i])

    opcode_conversion: list[str] = [op.pop() for op in opcode_possibilities]
    regs: list[int] = [0, 0, 0, 0]
    index += 2
    while index < len(inp):
        op, inp_a, inp_b, inp_c = tuple(map(int, inp[index].split()))
        instruction(opcode_conversion[op], inp_a, inp_b, inp_c, regs)
        index += 1

    return regs[0]


def main() -> None:
    test_input: str = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]

"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1

    file_location: str = "python/Advent of Code/2018/Day 16/input.txt"
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

    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
