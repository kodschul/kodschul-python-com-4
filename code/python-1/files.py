
# -- Datei kurz lesen
file = open("sample.txt", "r")
sample_content = file.read()
print(sample_content)


# --- Datei kurz schreiben

file = open("sample_write.txt", "w+")
file.write("\nHallo\n")


# -- Datei lesen
file = open("sample.txt", "r")
sample_lines = file.readlines()
print(sample_lines)

fruits = []

for line in sample_lines:
    line = line.replace("\n", "")
    if line != "":
        fruits.append(line)


fruits.sort()
print(fruits)

lines = []
for fruit in fruits:
    lines.append(fruit + "\n")
print(lines)

file = open("sample_output.txt", "w+")
file.writelines(lines)
