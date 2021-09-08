'''i want to be financial indepent next year, so i will change the start age and ending age, besides i increased the saving amount every year into 9000 sek'''

INTEREST = 0.10

START_AGE = 23
END_AGE = 40
RETIREMENT_AGE = 67


def savings_counter():
    amount = 0

    for age in range(START_AGE, END_AGE):
        amount += 9000
        amount = amount * (1 + INTEREST)

    for age in range(END_AGE, RETIREMENT_AGE):
        amount = amount * (1 + INTEREST)

    return amount


amount = savings_counter()
print("Savings at retirement", round(amount, 2))
