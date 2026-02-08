age = int(input("Enter your age: "))
amount = int(input("enter you ticket amount"))
def check_age(age,amount):
 if age <= 18:
    print("you are child",age)
    if amount <= 1000:
        print("you are poor" ,amount)
    else:
        print("you are rich",age)
 elif age <= 30:
    print("you are adult" ,age)
    if amount >= 1000:
        print("you are poor" ,amount)
    else:
        print("you are rich",age)
 elif age <= 40:
    print("you are mature" ,age)
    if amount >= 1000:
        print("you are poor" ,amount)
    else:
        print("you are rich",age)
 else:
    print("you will",age)
    if amount >= 1000:
        print("you are poor" ,amount)
    else:
        print("you are rich",age)
    age = "rip"
check_age(age,amount)