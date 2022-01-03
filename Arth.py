#This code will help us with Arthemetic operations in python 
# + is used for addition 
print(2 + 3 + 9)
# - is used for subraction 
print(99 - 73)
# * is used for multiplication 
print(23.54 * -1432)
# / for division (gives us Quetiont value)
print(100 / 7)
# // for floor division (gives us floor of Quetionet value)
print(100 // 7)
# % for getting reminder 
print(100 % 7)
# ** for power 
5 ** 3

""" As you might expect, operators like / and * take precedence 
over other operators like + and - as per mathematical conventions. 
You can use parentheses, i.e. ( and ), to specify the order in which operations are performed."""
print(((2 + 5) * (17 - 3)) / (4 ** 3))


""" Variables: While working with a programming language such as Python, 
information is stored in variables. You can think of variables as containers for storing data.
 The data stored within a variable is called its value."""

""" Functions: A function is a reusable set of instructions. 
It takes one or more inputs, performs certain operations, and often returns an output.
 Python provides many in-built functions like print and also allows us to define our own functions."""

"""print: The print function is used to display information.
 It takes one or more inputs, which can be text (within quotes, e.g., "this is some text"),
  numbers, variables, mathematical expressions, etc.
   We'll learn more about variables & functions in the next tutorial."""

""" Problem 1: A grocery store sells a bag of ice for $1.25 and makes a 20% profit.
 If it sells 500 bags of ice,
 how much total profit does it make?"""

 # Store input data in variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Perform the required calculations
profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = number_of_bags * profit_per_bag

# Display the result
print("The grocery store makes a total profit of $", total_profit)

""" problem 2 : A travel company wants to fly a plane to the Bahamas.
Flying the plane costs 5000 dollars. So far, 29 people have signed up for the trip.
If the company charges 200 dollars per ticket, what is the profit made by the company?
Create variables for each numeric quantity and use appropriate arithmetic operations."""

 # Store input data in variables
flying_cost = 5000
no_of_passengers = 29 
ticket_price = 200 
# make the required calculations
flying_profit = flying_cost -(ticket_price * no_of_passengers)

# Display the result
print("The plane company has made a profit of",flying_profit,"$",)

""" Problem 3: The population of a town is 198568. 
Out of them 45312 are men and 35678 are women. Find the number of children in the town. """
total_population = 198568
men_count = 45312
women_count = 35678 
children_count = total_population - (men_count + women_count)
print("No of Children in town are:", children_count)

""" Problem 4:  A shopkeeper has 2425 boxes of 24 pencils each. 
How many pencils do all the boxes have in all?"""

no_pencil_boxes = 2425
pencils_in_box = 24 
total_pencils = no_pencil_boxes * pencils_in_box

print("total number of pencils are:", total_pencils)

""" problem 5: The cost of 21 TV sets is $95844. Find the cost of one TV set."""
cost_of_all_Tv = 95844
total_tv = 21
cost_of_each_tv = cost_of_all_Tv/total_tv

print("cost of each tv is:", cost_of_each_tv)