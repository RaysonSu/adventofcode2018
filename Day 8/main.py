OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[int]:
    return list(map(int, inp[0].split(" ")))


def parse_packet(packet: list[int]) -> tuple[int, int, int]:
    packet = packet.copy()

    child_nodes: int = packet[0]
    meta_nodes: int = packet[1]

    total_length: int = 2
    meta_total: int = 0
    parsed_values: list[int] = [0]

    packet_meta: int
    packet_value: int
    packet_length: int
    for _ in range(child_nodes):
        packet_meta, packet_value, packet_length = parse_packet(
            packet[total_length:])
        total_length += packet_length
        meta_total += packet_meta
        parsed_values.append(packet_value)

    metadata: list[int] = packet[total_length:total_length + meta_nodes]
    meta_total += sum(metadata)

    value: int = 0
    if child_nodes == 0:
        value = sum(metadata)
    else:
        for entry in metadata:
            try:
                value += parsed_values[entry]
            except IndexError as _:
                pass

    return meta_total, value, total_length + meta_nodes


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return parse_packet(parse_inp(inp))[0]


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return parse_packet(parse_inp(inp))[1]


def main() -> None:
    test_input: str = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 138
    test_output_part_2_expected: OUTPUT_TYPE = 66

    file_location: str = "python/Advent of Code/2018/Day 8/input.txt"
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
