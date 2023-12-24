from time import time


def main_part_1(inp: int) -> str:
    recipes: list[int] = [3, 7]
    one_index: int = 0
    two_index: int = 1
    while len(recipes) < inp + 10:
        one_recipe: int = int(recipes[one_index])
        two_recipe: int = int(recipes[two_index])
        total: int = one_recipe + two_recipe
        recipes.extend(map(int, str(total)))
        one_index = (one_index + 1 + one_recipe) % len(recipes)
        two_index = (two_index + 1 + two_recipe) % len(recipes)

    return "".join(map(str, recipes[inp:inp+10]))


def main_part_2(inp: int) -> int:
    recipes: list[int] = [3, 7]
    one_index: int = 0
    two_index: int = 1
    for _ in range(25000000):
        one_recipe: int = int(recipes[one_index])
        two_recipe: int = int(recipes[two_index])
        total: int = one_recipe + two_recipe
        recipes.extend(map(int, str(total)))
        one_index = (one_index + 1 + one_recipe) % len(recipes)
        two_index = (two_index + 1 + two_recipe) % len(recipes)

    return "".join(map(str, recipes)).index(str(inp))


def main() -> None:
    test_input: int = 2018
    test_output_part_1_expected: str = "5941429882"
    test_output_part_2_expected: int = 86764

    input_file: int = 430971

    test_output_part_1: str = main_part_1(test_input)
    test_output_part_2: int = main_part_2(test_input)

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
