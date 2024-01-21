# Random Sentence Generator 👨‍💻 

For this exercise you are required to write program that generates a random sentence.

The program will make use of four different lists of strings called ``articles``, ``nouns``, ``verbs`` and ``prepositions``. 

💡Note: The syntax rule for a _"valid sentence"_ is that it must have the following structure:


````
article noun verb article noun preposition verb.
````
## List of words 📚
- A sample list of words for each of the four lists is given:
````
articles = “the”, “a”, “one”, “some”, “any”

nouns = “teacher”, “student”, “principal”, “library”, “school”

verbs = “taught”, “learned”, “read”, “walked”, “ran”

prepositions = “to”, “from”, “over”, “under”, “on”
````

- Valid sentences must be _**syntactically correct**_ but may not make any sense.

For example,
````
the teacher taught a student to read.  
````
makes sense however...

````
some school walked under a principal 
````
...is semantically nonsensical!


## 👀 Hints

1. The solution will need to create a list to store the words of the sentence _e.g._ ``wordlist = []``

Initially this list will be empty.

2. The words will need to be selected at random from each list.
3. The following line of code 
may be adapted to generate a random word.

````py
print(random.choice(nouns))
````

4.  As words are randomly selected they can be **_appended_** to ``wordlist``.
5.  Once the seven words have been generated they can be displayed in a sentence.


# ✨ Extra Credit
You can also refer to these [Simple List Exercises](https://www.w3schools.com/python/python_lists_exercises.asp) to practice what we have learned so far on Lists.

  