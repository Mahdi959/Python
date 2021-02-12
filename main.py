from datetime import datetime;
user ="mahdi1"
password = "mahdi2"
print("Application For Certitficate: ")

us = input("Username: ")
ps = input("Password: ")
if us == user and ps == password:
    print("loggen in")

else:
    print("Wrong Password")
    quit("Reload the page - Please - Insert the correct username and password to get your Certificate.\n"
         "To Reset Password Call - 84865684688 ")


name = input("What's Your Name : ")
fname = input("What's Your Father Name : ")
School = input("What's the name of you school : ")
roll = input("Your Roll Number : ")

print("Hi "+name+"! We certify that "+name+", Son of "+fname+" has passed his exam from "+School+". We wish you to have a wonderful life.\n Thank You So Much")
sign = input("Please type you name as your signature : "  ": ")
print("Thank You so Much and have a nice day!" )

now = datetime.now().time()

print("Time =", now)

