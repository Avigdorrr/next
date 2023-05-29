def parse_ranges(ranges_string):
    split_gen = (number.split("-") for number in ranges_string.split(","))
    numbers_gen = (number for start, stop in split_gen for number in range(int(start), int(stop)+1))
    return numbers_gen