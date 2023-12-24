from typing import Any
OUTPUT_TYPE = int


def parse_unit(row: str) -> dict[str, Any]:
    units: str
    units, row = tuple(row.split(" units each with "))

    hp: str
    hp, row = tuple(row.split("hit points "))

    weakness: list[str] = []
    immune: list[str] = []

    if ")" in row:
        row = row[1:]

        type_data: str
        type_data, row = tuple(row.split(")"))

        for data in type_data.split("; "):
            if data.startswith("weak to "):
                weakness = data[8:].split(", ")
            else:
                immune = data[10:].split(", ")

        row = row[26:]
    else:
        row = row[25:]

    dmg: str
    dmg, row = tuple(row.split(" ", 1))

    dmg_type: str
    initiative: str
    dmg_type, initiative = tuple(row.split(" damage at initiative "))

    return {
        "units": int(units),
        "hp": int(hp),
        "weak": weakness,
        "immune": immune,
        "dmg": int(dmg),
        "type": dmg_type,
        "init": int(initiative)
    }


def calc_damage(attacking: dict[str, Any], defending: dict[str, Any]):
    base_dmg: int = attacking["units"] * attacking["dmg"]

    if attacking["type"] in defending["weak"]:
        return base_dmg * 2
    elif attacking["type"] in defending["immune"]:
        return 0
    else:
        return base_dmg


def parse_inp(inp: list[str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    inp = list(map(str.strip, inp))

    immune: list[dict[str, Any]] = []
    for row in inp[1:inp.index("")]:
        immune.append(parse_unit(row))

    infect: list[dict[str, Any]] = []
    for row in inp[inp.index("") + 2:]:
        infect.append(parse_unit(row))

    return immune, infect


def simulate(immune: list[dict[str, Any]], infect: list[dict[str, Any]]) -> tuple[int, bool]:
    all_armies: list[dict[str, Any]] = immune.copy()
    all_armies.extend(infect)

    while immune and infect:
        immune.sort(key=lambda army: army["units"]
                    * army["dmg"] * 100 + army["init"], reverse=True)
        infect.sort(key=lambda army: army["units"]
                    * army["dmg"] * 100 + army["init"], reverse=True)
        all_armies.sort(key=lambda army: army["init"], reverse=True)

        chosen: dict[str, Any] | None
        best: int
        stat: int
        dmg: int

        infect_picked: list[dict[str, Any] | None] = []
        for attacking in infect:
            best = -1
            chosen = None
            for defending in immune:
                if defending in infect_picked:
                    continue

                dmg = calc_damage(attacking, defending)
                if dmg == 0:
                    continue

                stat = dmg * 1000000000000000 \
                    + defending["dmg"] * defending["units"] * 100 \
                    + defending["init"]

                if stat > best:
                    chosen = defending
                    best = stat

            infect_picked.append(chosen)

        immune_picked: list[dict[str, Any] | None] = []
        for attacking in immune:
            best = -1
            chosen = None
            for defending in infect:
                if defending in immune_picked:
                    continue

                dmg = calc_damage(attacking, defending)
                if dmg == 0:
                    continue

                stat = dmg * 1000000000000000 \
                    + defending["dmg"] * defending["units"] * 100 \
                    + defending["init"]

                if stat > best:
                    chosen = defending
                    best = stat

            immune_picked.append(chosen)

        units_killed: int = 0
        for army in all_armies:
            if army["units"] <= 0:
                continue

            side: bool = army in immune

            amount: int
            target: dict[str, Any] | None

            if side:
                index = immune.index(army)
                target = immune_picked[index]
            else:
                index = infect.index(army)
                target = infect_picked[index]

            if not target:
                continue

            dmg = calc_damage(army, target)
            amount = dmg // target["hp"]

            target["units"] -= amount
            units_killed += amount

        if units_killed == 0:
            return -1, False

        to_remove: list[dict[str, Any]] = []
        for army in all_armies:
            if army["units"] <= 0:
                to_remove.append(army)

        while to_remove:
            to_del: dict[str, Any] = to_remove.pop()
            all_armies.remove(to_del)
            try:
                infect.remove(to_del)
            except ValueError as _:
                pass

            try:
                immune.remove(to_del)
            except ValueError as _:
                pass
    ret: int = 0
    for army in all_armies:
        ret += army["units"]

    return ret, bool(immune)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    infect: list[dict[str, Any]]
    immune: list[dict[str, Any]]

    immune, infect = parse_inp(inp)

    return simulate(immune, infect)[0]


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    infect: list[dict[str, Any]]
    immune: list[dict[str, Any]]

    boost: int = 42
    while True:
        immune, infect = parse_inp(inp)

        for army in immune:
            army["dmg"] += boost

        count: int
        res: bool
        count, res = simulate(immune, infect)

        if res:
            return count

        boost += 1


def main() -> None:
    test_input: str = """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5216
    test_output_part_2_expected: OUTPUT_TYPE = 51

    file_location: str = "python/Advent of Code/2018/Day 24/input.txt"
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
