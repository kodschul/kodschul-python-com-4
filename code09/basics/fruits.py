fruits = ["orange", "mango", "apple", "lemonafe"]

print("current list:", fruits)

new_fruits = input("enter a fruit:").strip()

fruits.append(new_fruits)


print("after adding:" , fruits)

remove_f= input("enter to remove: ").strip()

if remove_f in fruits:

    fruits.remove(remove_f)
    print(fruits)

else:

    print(f"{remove_f}is not in the list")

    print("after remove," , fruits)