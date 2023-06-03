from math import factorial
from collections import Counter
from fractions import gcd


# Compute number of unique permutations for given cycle lengths
def compute_cycle_permutations(cycle_lengths, grid_size):
    total_permutations = factorial(grid_size)
    for length, frequency in Counter(cycle_lengths).items():
        total_permutations //= (length**frequency) * factorial(frequency)
    return total_permutations


# Generate all partitions of grid_size into cycle_lengths
def generate_cycle_partitions(grid_size, cycle_length=1):
    yield [grid_size]
    for cycle_length in range(cycle_length, grid_size // 2 + 1):
        for partition in generate_cycle_partitions(
            grid_size - cycle_length, cycle_length
        ):
            yield [cycle_length] + partition


# Calculate the sum of gcd of each cycle length pair for the grid
def compute_gcd_sum(cycle_width, cycle_height):
    return sum(
        sum(gcd(width, height) for width in cycle_width) for height in cycle_height
    )


# Main function to compute number of unique, non-equivalent configurations
def solution(w, h, s):
    total_configurations = 0
    # Generate all possible cycle partitions for width and height
    for cycle_width in generate_cycle_partitions(w):
        for cycle_height in generate_cycle_partitions(h):
            # Compute total permutations for width and height cycles
            total_permutations = compute_cycle_permutations(
                cycle_width, w
            ) * compute_cycle_permutations(cycle_height, h)

            # Compute the sum of gcd for each cycle width and height pair
            gcd_sum = compute_gcd_sum(cycle_width, cycle_height)

            # Add the configurations of this permutation to the total configurations
            total_configurations += total_permutations * (s**gcd_sum)

    # Normalize the total configurations by the number of permutations of rows and columns
    normalized_configurations = total_configurations // (factorial(w) * factorial(h))

    # Return the result as string
    return str(normalized_configurations)
