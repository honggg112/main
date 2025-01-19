import math
def min_radars(n, d, islands):
    # If d <= 0, only islands on the x-axis can be covered
    if d <= 0:
        return -1 if any(y > 0 for _, y in islands) else n

    intervals = []
    for x, y in islands:
        # If any island is too high to be covered by radar
        if y > d:
            return -1
        # Calculate the horizontal distance that can be covered
        horizontal_dist = math.sqrt(d ** 2 - y ** 2)
        intervals.append((x - horizontal_dist, x + horizontal_dist))

    # Sort intervals by their right endpoint
    intervals.sort(key=lambda interval: interval[1])

    radars = 0
    last_covered_end = -float('inf')

    for interval in intervals:
        left, right = interval
        # If the current interval starts after the last covered point
        if left > last_covered_end:
            # Place a radar at the right end of the current interval
            radars += 1
            last_covered_end = right

    return radars

def main():
    test_case_number = 1
    while True:
        # Read the first line for the test case
        line = input().strip()
        if line == "0 0":
            break

        n, d = map(int, line.split())
        islands = []

        for _ in range(n):
            x, y = map(int, input().strip().split())
            islands.append((x, y))

        # Read the blank line between test cases
        input().strip()

        # Calculate and print the result for the current test case
        result = min_radars(n, d, islands)
        print(f"Case {test_case_number}: {result}")
        test_case_number += 1

if __name__ == "__main__":
    main()