file=open("example.txt", 'r')
file.seek(0)
content=file.readlines()
content=[i.rstrip("\n") for i in content]
print(content)
file.close

file=open("example2.txt", 'w')
l=["Line 1","Line 2","Line 3"]
for item in l:
    file.write(item+"\n")
file.close()

with open("example3.txt", "a+") as file:
    file.seek(0)
    file.write("Line 1\n")

