# Lists - Investigate Task 🕵️‍♂️

## What is an Investigate task?

- In investigate tasks you are given some example code to study. 
- Underneath it are questions to make sure that you understand how the code works.

- Use the ``# comments`` to answer the investigate questions.


````python
# -----------------------------
# Title: Lists Investigate Task
# Date:
# -----------------------------

### Example code:

# What does this line do?
names = ["Alex","Anita","Patrick","Atif","Sue"]
# Answer: 

while True:                                                 # Line 12
  print("Enter a number for your choice.")
  print("1. Show all")
  print("2. Add name")
  print("3. Show name")
  print("4. Exit")
  choice = int(input("Enter Number: "))                     # Line 18

  if choice == 1:
    print(names)
    print("")
  elif choice == 2:
    name = input("Enter the name: ")
    names.append(name)                                      # Line 25
    print("")
  elif choice == 3:
    index = int(input("Enter the index of the name: "))
    print(names[index])
    print("")
  else:
    print("Goodbye")
    break                                                   # Line 33
  

# What is the identifier for the list in this program?
  # Answer:

# What would happen if you choose option “3” and entered index “0”? 
  # Answer:

# What would happen if you choose option “3” and entered index “7”?
  # Answer:

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer:

# What is the purpose of int(input()) on line 18 ?
  # Answer:

# What is the purpose of the code on line 25?
  # Answer:

# What is the purpose of the while loop on line 12?
  # Answer:

# What does the break command do on line 33?
  # Answer:
````

  
