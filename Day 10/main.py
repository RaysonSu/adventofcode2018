def str_assign(string: str, index: int, item: str) -> str:
    return string[:index] + item + string[index+1:]


def main_all(inp: list[str]) -> None:
    positions: list[tuple[int, int]] = []
    velocities: list[tuple[int, int]] = []
    for line in inp:
        data: list[int] = [
            int(x)
            for x in "".join([
                char
                for char in line
                if char.isnumeric() or char in "- "
            ]).split(" ")
            if x != ""
        ]
        positions.append((data[0], data[1]))
        velocities.append((data[2], data[3]))

    total: float = 0
    for position, velocity in zip(positions, velocities):
        total += position[0] / max(1, velocity[0])
        total += position[1] / max(1, velocity[1])

    time = int(total / len(positions) // 2) - 10

    new_x: list[int] = [-1, 9999]
    new_y: list[int] = [-1, 9999]
    x_diff: int = 100000
    y_diff: int = 100000
    prev_x: int = 1000001
    prev_y: int = 1000001
    while x_diff < prev_x and y_diff < prev_y:
        time += 1
        new_x = [
            pos[0] + vel[0] * time
            for pos, vel in zip(positions, velocities)
        ]

        new_y = [
            pos[1] + vel[1] * time
            for pos, vel in zip(positions, velocities)
        ]

        prev_x = x_diff
        prev_y = y_diff

        x_diff = max(new_x) - min(new_y)
        y_diff = max(new_y) - min(new_y)

    time -= 1
    new_x = [
        pos[0] + vel[0] * time
        for pos, vel in zip(positions, velocities)
    ]

    new_y = [
        pos[1] + vel[1] * time
        for pos, vel in zip(positions, velocities)
    ]

    prev_x = max(new_x) - min(new_x)
    prev_y = max(new_y) - min(new_y)

    grid: list[str] = [" " * (prev_x + 1) for _ in range(prev_y + 1)]
    for x, y in zip(new_x, new_y):
        grid[y - min(new_y)] = str_assign(grid[y - min(new_y)],
                                          x - min(new_x), "#")

    print("Part 1: ")
    for row in grid:
        print(row)

    print(f"Part 2: {time}")


def main() -> None:
    file_location: str = "python/Advent of Code/2018/Day 10/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    main_all(input_file)


if __name__ == "__main__":
    main()
