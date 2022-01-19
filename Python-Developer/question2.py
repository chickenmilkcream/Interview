from math import floor, ceil


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    """
    Move the zeros to the center of the array, where center position is defined by floor(len(array)/2)
    If the list is empty, return []

    Space: O(n)
    Time: O(n)
    """

    if len(array) == 0:
        return []

    num_zeros = 0
    non_zero_array = []
    for number in array:
        if number == 0:
            num_zeros += 1
        else:
            non_zero_array.append(number)

    center_num = floor(len(non_zero_array)/2)
    array_left = non_zero_array[:center_num]
    array_right = non_zero_array[center_num:]
    zeros = [0] * num_zeros

    return array_left + zeros + array_right


if __name__ == "__main__":
    # write your debug code here
    center_zeros([0, 0, 1])