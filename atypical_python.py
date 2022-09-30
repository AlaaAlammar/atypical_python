year = 2022
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
#---------------------------------------------
length=int(input("Enter you length here : "))
if length==170:
    print("Tall")
elif length >= 170:
    print("Tall")
elif length <170 and length >160:
    print("Normal")
elif length<150:
    print("Short")
