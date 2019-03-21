def age_foo(age):
    new_age = float(age) + 50
    return new_age


age = float(input("Enter your age: "))

if age < 150:
    new_age = age_foo(age)
    print(new_age)
else:
    print("How is that possible?")
