# -----------------
# Title: 
# Date:
# -----------------


# Task 1
'''# version 1.1 - Add 5 numbers into a list
numbers = [] 
for i in range(5):
  item = int(input("Enter number:"))
  numbers.append(item)'''

'''# version 1.2 - Add 5 numbers into a list, then add 1 to each item.
numbers = []
for i in range(5):
    numbers.append(int(input("Enter a number: ")))

for i in range(len(numbers)):
    numbers[i] += 1

print(numbers)'''

'''###Using List Comprehension:
# version 1.3
numbers = [int(input("Enter a number: ")) for i in range(5)]
numbers = [x+1 for x in numbers]
print(numbers)'''

  




# Task 2
# Input the number of hours Stephen spends at home for each day
hours = [12, 7, 9, 9, 6, 8, 2]

# Calculate the total number of hours Stephen spends at home
total_hours = sum(hours)

# Calculate the total amount of milk Stephen drinks
total_milk = total_hours * 0.5

# Calculate the cost of the milk
cost = total_milk * 1.35

# Round the cost to 2 decimal places
cost = round(cost, 2)

# Print the results
print("Total hours at home:", total_hours)
print("Total milk consumed:", total_milk, "litres")
print("Cost of milk: €", cost)


# This program first inputs the number of hours Stephen spends at home for each day into a list called hours. 

# Then it calculates the total number of hours Stephen spends at home by using the sum() function on the hours list. 

# Next, it calculates the total amount of milk Stephen drinks by multiplying the total number of hours by 0.5. 

# Finally, it calculates the cost of the milk by multiplying the total amount of milk by €1.35 and assigns the value to the variable cost. Then it prints the results on the screen.



