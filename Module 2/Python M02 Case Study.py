#Haydn Gable, Python M02 Case Study
"""
This app prompts the user to enter a student's last name, then checks if that
last name is 'ZZZ' and runs the loop if not. Then the user is prompted to enter
the student's first name and GPA, the GPA is checked by an if/else statement and
the proper statement is printed and finally, the user is prompted
to enter another last name and has the chance to exit the loop.
"""

last_name = input("Enter a student's last name or 'ZZZ' to exit: ")
while last_name != "ZZZ":
    first_name = input("Enter that student's first name: ")
    gpa = float(input("Enter that student's GPA: "))
    if gpa >= 3.5:
        print("This student has made the Dean's list!")
    elif gpa >= 3.25:
        print("This student has made the Honor Roll!")
    else:
        print("This student has not made the Honor Roll or the Dean's List.")
    last_name = input("Enter a student's last name or 'ZZZ' to exit: ")
