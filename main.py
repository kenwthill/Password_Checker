# import regular expressions
import re
import string


# function for user input and validating password if it has 1 uppercase, 1 lower case, 1 number and 1 special character, between 6 and 16 characters (inclusive)
def validate():
    while True:

        # user input

        password = input("Please enter a password to validate, enter e to exit...")

        # checking the password to each rule

        # if the user decides to exit
        if (password) == "e":
            break
            # checking the length of the password
        if len(password) < 6:
            print("Please enter a password between 6 and 16 characters")
        if len(password) > 16:
            print("Please enter a password between 6 and 16   characters")

        # checking the password for a lowercase character
        if re.search('[a-z]', password) is None:
            print("Please enter a password with at least one lowercase character")

        # checking the password for an uppercase character
        if re.search('[A-Z]', password) is None:
            print("Please enter a password with at least one uppercase character")

        # checking the password for a number
        if re.search('[0-9]', password) is None:
            print("Please enter a password with at least one number character")

        # checking the password for a special character
        if re.search('["£","#", "&", "@"]', password) is None:
            print("Please enter a password with at least one symbol")
        # if the user decides to exit
        # break the loop to menu
        else:
            print("The password is fine to use!")

        # times tables function


def times_table():
    # user input

    while True:
        table_str = input(
            "Please choose which times table you would like between 2 and 12 enter e to return to menu...")
        # exit to menu
        if (table_str) == "e":
            break
        # change to integer
        table = (int(table_str))
        # 2 times table
        if (table) == 2:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 3 times table
        elif (table) == 3:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 4 times table
        elif (table) == 4:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 5 times table
        elif (table) == 5:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 6 times table
        elif (table) == 6:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 7 times table
        elif (table) == 7:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 8 times table
        elif (table) == 8:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 9 times table
        elif (table) == 9:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 10 times table
        elif (table) == 10:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 11 times table
        elif (table) == 11:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # 12 times table
        elif (table) == 12:
            print("Table", table)
            for row in range(1, 13):
                print(row, "x", table, "=", table * row)
            print()
        # if the user inputs wrong number
        elif (table) == 1:
            print("Please enter a valid times table between 2 and 12")
        elif (table) > 12:
            print("Please enter a valid times table between 2 and 12")


# Welcome to the password checker and times table tool

print("Welcome to the Password Checker and Times Table Tool")

# Menu

while True:
    print("Menu")
    print("1: To validate your password has 1 lowercase character, 1 uppercase letter, 1 number and 1 symbol")
    print("2: To view time table of your choice")
    print("e: To exit.")

    # User Choice

    menu = input("Please enter your choice >")

    if menu == "1":
        validate()
    if menu == "2":
        times_table()
    if menu == "e":
        break
print("Thank you for using the Password Checker and Times Table Tool")
print("Goodbye")

# End of Program
