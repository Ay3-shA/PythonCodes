#Life in weeks 
#supposing average age is 90 years
#f - string

age = input("What is your current age? ")

#year_remaining = 90 - int(age)

days_remaining = (90 - int(age)) * 365
weeks_remaining = (90 - int(age)) * 52
months_remaining = (90 - int(age)) + 12
print (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

#-----------------------------------------------------------