nums = range(10)

print(list(nums))


def is_even(num):
    return num % 2 == 0


evens = filter(is_even, nums)
odds = filter(lambda num: num % 2 != 0, nums)

print(f"evens: {evens}, odds: {list(odds)}")
