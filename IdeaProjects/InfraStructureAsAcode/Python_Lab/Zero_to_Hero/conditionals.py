age = 18

if age >= 18:
    print("You are an adult.")
###############################################
# temperature = 25
#
# if temperature > 30:
#     print("It's a hot day.")
# elif temperature > 20:
#     print("It's a pleasant day.")
# else:
#     print("It's a bit chilly.")

#Using or and and:

temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a nice day to go outside.")

#Using bool in Conditionals:

is_sunny = True
is_weekend = False

if is_sunny or is_weekend:
    print("You can go for a walk.")
else:
    print("Maybe stay indoors.")