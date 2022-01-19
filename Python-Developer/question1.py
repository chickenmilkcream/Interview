def select_max(array):
    # write your function here
    # do NOT use the built-in max() function
    """
    Given an array of Integers, return the maximum element of the array
    If the array is empty, return None

    Space: O(1)
    Time: O(n)
    """

    if len(array) == 0:
        return None

    curr_max = array[0]
    for element in array:
        if element > curr_max:
            curr_max = element
    return curr_max



if __name__ == "__main__":
    # write your debug code here
    pass
