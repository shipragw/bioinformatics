def finding_subset(str1, str2):
    if len(str2) > len(str1):
        raise ValueError("Invalid input")
    locations = []
    start = 0
    while start < len(str1):
        point = str1.find(str2, start)
        if point == -1:
            break
        locations.append(point)
        start = point + 1
    return locations


