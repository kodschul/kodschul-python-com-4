from datetime import datetime

file_content = ""
with open("data/hello.txt", "r") as f: 
    file_content = f.read()
    
print("Content: ", file_content)

file_content += "\n " + str(datetime.now())

with open("data/hello.txt","w+") as f:
    f.write(file_content)



