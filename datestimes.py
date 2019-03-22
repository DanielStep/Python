import datetime

def create_file(filename):
    with open(filename, "w") as file:
        file.write("Created on: ")


date=datetime.datetime.now()
filename=date.strftime("%Y-%m-%d-%H-%M") + ".txt"
create_file(filename)

# date=datetime.datetime.now()
# pastdate=datetime.datetime(2000, 1, 1)
# print(date)
# print(pastdate)

# diff= date-pastdate
# print(type(diff))
# print(diff)