"""
Program: basic_if.py
Author:  Daniel Meeker
Date: 06/09/2020

This program accepts user input for desired membership
level then calculates and returns the cost of the level.
"""


# function definitions:


def get_membership():  # Get user input
    membership = input("Welcome to the Programmer's Toolkit Monthly Subscription Box! "
                       "\n    Our membership level's are:"
                       "\n        1: Platinum"
                       "\n        2: Gold"
                       "\n        3: Silver"
                       "\n        4: Bronze"
                       "\n        5: Free Trial"
                       "\n    Please enter the number corresponding to your desired level: ")
    # I chose to request integers from the user to avoid possible errors with spelling and to
    # make a simple input validation possible
    return membership


def calculate_cost(membership):  # Use the user input to calculate cost
    if int(float(membership)) == 1:
        price = 60
        level = "Platinum"
    elif int(float(membership)) == 2:
        price = 50
        level = "Gold"
    elif int(float(membership)) == 3:
        price = 40
        level = "Silver"
    elif int(float(membership)) == 4:
        price = 30
        level = "Bronze"
    elif int(float(membership)) == 5:
        price = 0
        level = "Free Trial"
    else:
        price = 0
        level = "Error"
    membership_cost = [level, price]  # Saved as a list to make output function easier.
    return membership_cost


def output_result(membership_cost):
    if membership_cost[0] == "Error":
        return "Error, must choose a level between 1-5"
    else:
        return "You chose {} membership, your price is ${:.2f} per month".format(membership_cost[0], membership_cost[1])


if __name__ == '__main__':
    print(output_result(calculate_cost(get_membership())))  # call the functions to run the program
