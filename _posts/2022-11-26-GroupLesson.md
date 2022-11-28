---
toc: true
layout: post
description: Markdown post of the group lesson by Liav Bar, Noor B, Steven W, Nathan C, Ederick W.
categories: [Markdown]
title: 3.1-3.2 Group Lesson
---

# Unit 3, Section 1.1: Data Types and Variables - Ederick

## Essential Knowledge (College Board's Must Knows):
 * A variable is an abstraction inside a program that holds a value, where each variable has associated data storage that represents a single value at a time (However, if the value is a collection type such as a list, then the value can contain multiple values).
 * Variables typically have meaningful names that helps with the overall organization of the code and understanding of what is being represented by the variables
 * Some programming languages provide a variety of methods to represent data, which are referenced using variables 9Booleans, numbers, lists, and strings)
 * One form of a value is better suited for representation than antoher.

## What is a Variable?

A variable is an abstraction made inside a program that holds a value. These variables are used in code to refer to more comples values that the variable contains and makes the program code more organized and smoother to run.

Variables can be seen as "containers" and each container has a name that holds what it is supposed to hold.
In the following code, we can see that a variable has the value of "Alex." How can we make the variable appear more organized in the code?

![]({{site.baseurl}}/images/eddy1.png "https://github.com/LiavB2/ominicient-lavebear")

## Choosing Variables
When choosing variables, it is important to assign the variables name to something that correlates with what the function of the variable is supposed to do. For example, we do not want a variable that is supposed to hold a name be named "age" becaue it can be confusing and mistakes may be more prevalent.

Example:

![]({{site.baseurl}}/images/eddy4.png "https://github.com/LiavB2/ominicient-lavebear")

- Notice how age is going to be seen when printing the code. That can lead to confusion

## Data Types

Variables have different data types that store specific kinds of data depending on what is being represented. Some examples are shown below:

* integer (numbers)
* string (or text/letters)
* Boolean (True/False statements)

These types of data types can be useful when trying to represent a value. For example, you would not want a variable meant to represent someone's name with an integer.

Questions (College Board's Essential Knowledge):
1. What exactly IS a variable?
2. What is the best data type to represent someone's dog's name?
3. Why is it important to give variables specific names before containing values?
4. What is the best way to represent someone's phone number?

Bonus (Not required but important to know): 
1. How can we update a variable's value
2. What function is used to recieve a user's input?

## Hacks
- As your code becomes increasingly more complex, variables and their names will make reading and fixing your code easier.

### Create code that...

- Uses variables
- Show your understanding of different variable data types by using at least 2 different types in your code
- Uses meaningful names to prevent confusion

### Rubric 0.2/0.2
- Code needs to function
- Data types are properly used for their given function
- Each variable has identification to prevent confusion
- Each Variable is utilized for their intended purpose

# Variables (3.1.2) - Noor

## Learning objective for 3.1.2:
Determine the value of a variable as a result of an assignment
- done through looking at how we can use the assignment operator

## Note:
Collegeboard uses <-- as the assignment operator
- The assignment operator looks different for different types of coding languages
A variable will take the most recent value assigned

## How do you even store a value inside a variable?

Let's use python for our example:
   - In python, the assignment operator is the equal sign (=)
   - In order to store a value inside a variable, we must:
       - Give the variable a name
       - place the assignment operator 
       - input the variable value

![]({{site.baseurl}}/images/noor1.png "https://github.com/LiavB2/ominicient-lavebear")

## JavaScript Example

## Let's get a little more practical here
Imagine that you are making a calendar and have just finished the html code that is needed:
- You now want to be able to switch between the months of the year by using the "next" or "prev" buttons
    - you will need to take the html elements and use them to your advantage
        - but how?

![]({{site.baseurl}}/images/noor2.png "https://github.com/LiavB2/ominicient-lavebear")

## Recap:
- We learned what is a assignment operator
- We learned how to use the assignment operator
- We learned how to store a value inside a variable using the assignment operator
- We experimented with a few examples 

## Hacks: 
Answer these:
- In your **own** words, briefly explain by writing down what an assignment operator is
- In Collegeboard pseudocode, what symbol is used to assign values to variables?
- A variable, x, is initially given a value of 15. Later on, the value for x is changed to 22. If you print x, would the command display 15 or 22?

## Hacks:
Copy the all the html code into a markdown file and run your local server. You will then see a decimal to binary converter near the html code. The problem is that it is not converting the decimal to binary. This is because the variables are not defined properly and it is your job to use the information learned today to fix the converter. **Don't change the css**

### Bonus (optional):
There's more than one way to define the variable. List two ways to do it.

### Rubric

#### For .15:
- Student has followed directions properly and has the converter working

#### For .18:
- Student has completed some of the bonus material alongside requirement for 2.7

#### For .20:
- Student has completed all of the material, answered thoughtfully, and met requirements for 2.7

# List and Strings Using Variables- Nathan

## Strings
Strings is a series of characters (numbers, letters, etc), one example of a string is your name or your id because strings can contain both numbers and letters.

The following are all examples of strings being used in code, in this case, within print functions.

![]({{site.baseurl}}/images/nc1.png "https://github.com/LiavB2/ominicient-lavebear")

## Lists
Lists are sequences of elements with each element being a variable. An example of a list can be the names of the students in this classroom. 

### Features of Lists
* The elements within the list can be accessed by index.
* Can store various elements
* The list is in order

### Example of a list and how it can be used

![]({{site.baseurl}}/images/nc2.png "https://github.com/LiavB2/ominicient-lavebear")

## List Index
An index is an element of a string. Indices typically start with 0, but Collegeboard has the index start at 1.

![]({{site.baseurl}}/images/nc3.png "https://github.com/LiavB2/ominicient-lavebear")

## Hacks

## Questions
* What is a list?
* What is an element
* What is an easy way to reference the elements in a list or string?
* What is an example of a string?

### Create an index of your favorite foods
Tips: Index starts at 1, Strings are ordered sequences of characters

Extra work: Try to create an index that lists your favorite food and print the element at index 3.
More work: Create a list of your favorite foods and create an index to access them.

marks = ["food1"]

### Rubric 

![]({{site.baseurl}}/images/ncrubric.png "https://github.com/LiavB2/ominicient-lavebear")

# Data Abstraction with Lists - Steven

## Data abstraction can be created with lists.
- Lists bundle together multiple elements and/or variables under one name are not defined with specified lengths. 
- The variables that are stored in a list do not have to be limited to one kind of variable. 
- The user does not need to know how the list stores data (this gives way for data abstraction).

## In the code below, the logic itself works with a list, but the code abstracts it into a sequence of bits in a string (as seen in the input and output). To make this work, the splitbits lists is created and processed. At the end of the code, the result is outputted as a string rather than a list (abstraction).

![]({{site.baseurl}}/images/steven1.png "https://github.com/LiavB2/ominicient-lavebear")

## Hacks

- The following code is incomplete. It's intended purpose is to increase three numbers, all of which ask for user input, by an amount specified the user. The input code is abstracted, but the actual logic isn't connected to the abstraction.

![]({{site.baseurl}}/images/steven2.png "https://github.com/LiavB2/ominicient-lavebear")

### The following provides a rubric for my hacks (scored out of 0.20)

0.20 - Fully functioning data abstraction with a list
0.10 - not functioning, but attempt at making a list
0.00 - not functioning, no evidence of attempt based upon the guidelines


# Managing Complexity with lists - Liav 

## Long and slow way
- By now, everyone should know the "long and slow way" to print a list of something in python
    - It is easy to just assign a value to a single variable
    - This method is displayed in this example with test scores:

![]({{site.baseurl}}/images/LASW.png "https://github.com/LiavB2/ominicient-lavebear")

- As you can see, each score is assigned to its relative variable such as "score1 = 95" and then you just print each variable.
- However you can make the code segment faster, easier to read, and more efficient...

## Assinging values to one variable
- Use square brackets "[]" to store the values of a certain variable, then you can simply print the variable to output your desired list:

![]({{site.baseurl}}/images/scorevar.png "https://github.com/LiavB2/ominicient-lavebear")

- Now instead of having a difference variable and new line of code for each value, the list is simply displayed by assigning each value to a single value that you can now print.

## How lists manage complexity of a program
- Simplification
    - It is much simpler, faster, and easier to code lists this way
    - Makes the code segment much easier to read

- Variables
    - You do not need as many variables, because you can just assign all corresponding values to a single variable
    - To change a value you don't have to edit/add/remove an entire variable

## Python Quiz
- Now everyone should take this short python quiz and screenshot your score.

![]({{site.baseurl}}/images/pquiz.png "https://github.com/LiavB2/ominicient-lavebear")

## Simplify Foods List 
- Now simplify this foods list using what you have learned

![]({{site.baseurl}}/images/Lfoodlist.png "https://github.com/LiavB2/ominicient-lavebear")

## Hacks
- On a single markdown file:
    - Insert a screenshot of your score on the python quiz
    - Insert a screenshot of your simplifying of the food list
    - Why are using lists better for a program, rather than writing out each line of code?
    - Make your own list the "long and slow way" then manage the complexity of the list

## Rubric
- In ordere to earn a .20/.20 you must
    - On a markdown post:
    - make an attempt at the python quiz
    - Successfully simplify the food list
    - Answer the question in detail
    - Provide evidence of your own list that you coded