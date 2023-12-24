OUTPUT_TYPE = int


def do_instruction(ins: str, inp_a: int, inp_b: int, inp_c: int, regs: list[int]) -> None:
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


def run_program(program: list[str], regs: list[int]) -> int:
    inp: list[str] = program.copy()
    ins_pointer: int = int(inp[0][4:])

    inp = inp[1:]
    count: int = 0

    while True:
        instruction: int = regs[ins_pointer]
        if instruction == 29:
            print(regs[1])
        if instruction >= len(inp):
            break

        ins: str
        a: str
        b: str
        c: str
        ins, a, b, c = tuple(inp[instruction].split(" "))

        inp_a: int = int(a)
        inp_b: int = int(b)
        inp_c: int = int(c)

        do_instruction(ins, inp_a, inp_b, inp_c, regs)
        regs[ins_pointer] += 1
        count += 1

    return count


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ins_pointer: int = int(inp[0][4:])

    inp = inp[1:]
    count: int = 0
    regs: list[int] = [0, 0, 0, 0, 0, 0]

    while True:
        instruction: int = regs[ins_pointer]
        if instruction == 29:
            return regs[1]

        ins: str
        a: str
        b: str
        c: str
        ins, a, b, c = tuple(inp[instruction].split(" "))

        inp_a: int = int(a)
        inp_b: int = int(b)
        inp_c: int = int(c)

        if instruction == 28:
            return regs[inp_a]

        do_instruction(ins, inp_a, inp_b, inp_c, regs)
        regs[ins_pointer] += 1
        count += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ins_pointer: int = int(inp[0][4:])

    inp = inp[1:]
    count: int = 0
    regs: list[int] = [0, 0, 0, 0, 0, 0]
    seen: list[int] = []

    while True:
        instruction: int = regs[ins_pointer]
        ins: str
        a: str
        b: str
        c: str
        ins, a, b, c = tuple(inp[instruction].split(" "))

        inp_a: int = int(a)
        inp_b: int = int(b)
        inp_c: int = int(c)

        if instruction == 28:
            if regs[inp_a] in seen:
                break

            seen.append(regs[inp_a])

        do_instruction(ins, inp_a, inp_b, inp_c, regs)
        regs[ins_pointer] += 1
        count += 1

    return seen[-1]


def main() -> None:
    file_location: str = "python/Advent of Code/2018/Day 21/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
