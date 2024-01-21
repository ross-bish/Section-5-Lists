# Lists - Predict and Run Task ✍👨‍💻

## What’s a **Predict & Run** task?

In this task you are given a sample of code as shown below:

````py
# Sample Code

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence)
print(Sentence[1])
Sentence.append("life")
Sentence[4] = "sunny"
print(Sentence[4])
print(Sentence[0] + " " + Sentence[3])
print(Sentence)
````

- Look at each line, study it carefully.  
- Write a prediction of what it will do when it runs.  Your prediction should be added to the code as ``#comments``.
- You should use the key terms *"list", "item"* and *"index"* in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down any differences between your prediction and what actually happens.

## List Operations - Reference Table 📚
- Create a new list called `sweets[]`
- Add some of your favourite sweets to this list *e.g.*
  ````py
  sweets = ["M&Ms", "Skittles", "Dairymilk"]
  ````
- Experiment with the operations shown below. 👇



| Output item      | Outputs a single item from the array.                    | print(arrayName\[itemIndex\])<br><br>``print(sweets[3])``                                                                                                                                                                                                                           |
| ---------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edit item        | Changes or replaces an item in an array.                 | arrayName\[itemIndex\] = New data<br><br>``sweets[1] = "Haribo"``                                                                                                                                                                                                                   |
| Add an item      | Puts a new item onto the end of the array                | arrayName.append(new data)<br><br>``sweets.append("Galaxy")``                                                                                                                                                                                                                         |
| Remove an item   | Removes an item from the array                           | arrayName.pop(itemIndex)<br><br>``sweets.pop(2)``                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                              |
| Output all items | Outputs every item in the array one by one using a loop. | for i in range(0, len(arrayName)):<br>print(arrayName\[i\])<br><br>``for i in range(0, len(sweets)):``<br>``print(sweets[i])``<br><br>#You need to know how to do the for loop version for the exam.<br><br>You can also use... <br><br>``print(sweets)``<br> |


## 🤔Help! My code doesn't work
Make sure that you check for the following things:
- The list name is identical everywhere it is used (capital letters  matter)
- List index is surrounded by *square* brackets `[ ]`
- List indexing starts at *zero* `[0]`- are you counting properly?


  