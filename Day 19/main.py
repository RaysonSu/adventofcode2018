OUTPUT_TYPE = int


def divisors(x: int) -> set[int]:
    ret: set[int] = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            ret.add(i)
            ret.add(x // i)

    return ret


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


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ins_pointer: int = int(inp[0][4:])
    regs: list[int] = [0, 0, 0, 0, 0, 0]

    inp = inp[1:]

    for _ in range(100):
        instruction: int = regs[ins_pointer]
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

    return sum(divisors(max(regs)))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ins_pointer: int = int(inp[0][4:])
    regs: list[int] = [1, 0, 0, 0, 0, 0]

    inp = inp[1:]

    for _ in range(100):
        instruction: int = regs[ins_pointer]
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

    return sum(divisors(max(regs)))


def main() -> None:
    file_location: str = "python/Advent of Code/2018/Day 19/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    print(f"Part 1: {main_part_1(input_file)}")
    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
