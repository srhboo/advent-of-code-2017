from math import sqrt, ceil
from pipetools import pipe


# rounds up to nearest odd number
def ceil_odd(number):
    if number % 2 == 0:
        return number + 1
    else:
        return number


def divide_two(number):
    return number / 2


def square(number):
    return number ** 2

# input: the problem number
# returns nearest rounded up square root
ceil_nearest_root = pipe | sqrt | ceil


# input: the problem number
# returns ring the number is in (center counts as first ring)
which_ring = pipe | ceil_nearest_root | ceil_odd | divide_two | ceil


def side_length(square):
    return sqrt(square) - 1

# input: the problem number
# returns the largest number in the ring it is in
sq_corner_number = pipe | ceil_nearest_root | ceil_odd | square


def get_centers(side):
    half_lengths_away = {
        'bottom': 1,
        'left': 3,
        'top': 5,
        'right': 7,
    }[side]

    def get_side_center(right_corner):
        return right_corner - (
            half_lengths_away * side_length(right_corner) / 2)
    return get_side_center


def distance(number):
    right_corner = sq_corner_number(number)
    bottom_center = get_centers('bottom')(right_corner)
    left_center = get_centers('left')(right_corner)
    top_center = get_centers('top')(right_corner)
    right_center = get_centers('right')(right_corner)

    ring = which_ring(number)
    if number in [bottom_center, left_center, top_center, right_center]:
        return ring - 1
    else:
        diff_left = abs(number - left_center)
        diff_right = abs(number - right_center)
        diff_top = abs(number - top_center)
        diff_bottom = abs(number - bottom_center)
        return int(min(
            diff_left,
            diff_right,
            diff_bottom,
            diff_top
        ) + ring - 1)


def main():
    num = int(input("Please enter a number \n"))
    print("The Manhattan Distance is:")
    print(distance(num))

if __name__ == "__main__":
    main()
