def minimum_points(threshold, points):
    n = len(points)
    if n <= 0:
        return 0
    if points[-1] - points[0] < threshold:
        return n

    i = 0
    questions = 1
    start = points[0]
    while i < n and points[i]-start < threshold:
        i += 2
        questions += 1

    return questions


if __name__ == "__main__":
    # write your debug code here
    pass
