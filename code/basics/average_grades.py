grades = [1, 2, 3, 1, 2, 3, 5]


def average_grade(grades):
    return sum(grades) / len(grades)


# -
avg1 = average_grade(grades)
avg2 = average_grade(grades)
avg3 = average_grade(grades)
print(f"Average grade = {avg1} out of {len(grades)}")
print(f"Average grade = {avg2} out of {len(grades)}")
print(f"Average grade = {avg3} out of {len(grades)}")
