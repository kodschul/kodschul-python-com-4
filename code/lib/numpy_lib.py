import numpy as np


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
nums3 = [7, 2, 4, 2, 1]

# convert to a numpy array to process it
np1 = np.array(nums1)
np2 = np.array(nums2)
np3 = np.array(nums3)


# sum
addition = np1 + np2
subtraction = np1 - np2
# ...

print(f"Addition {np1} + {np2} = {addition}")
print(f"Subtraction {np1} - {np2} = {subtraction}")
# print(f"Division = {division}")
# print(f"Multiplication = {multiplication}")


# math ops
average = np.mean(np1)
print(f"average: {np1} = {average}")


np3.sort()


median = np.median(np3)
print(f"median: {np3} = {median}")


# sort & concatenate array
combined_nums = np.concatenate([np1, np2])
print(list(combined_nums))
