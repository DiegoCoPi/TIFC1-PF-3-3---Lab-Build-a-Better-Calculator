def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def isiteven(num):
    if isinstance(num, int) or (isinstance(num, float) and num.is_integer()):
        return int(num) % 2 == 0
    return False


def isitaninteger(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def main():
    print("Hello learners!")
    nums = [2, 7, 8.5, 7, 9, 8, 30]


if __name__ == "__main__":
    main()
