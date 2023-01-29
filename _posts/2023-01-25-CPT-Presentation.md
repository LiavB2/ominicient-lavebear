---
toc: true
layout: post
description: An overview of what I would do for the AP exam CPT written portion for my feature of the CPT tri 2 group project. 
categories: [CPT]
title: Athlete Stats Feature College Board Overview
---

# My Feature: Athlete Stats

![]({{site.baseurl}}/images/stats.png "https://github.com/LiavB2/ominicient-lavebear") 

## Overview
- My feature is a stats tracker that allows users to track their physical and fitness growth.
- When you type a new max in a certain category and click "add" then it will add to the top of the graph
- As you can see, it has tabs to add a new max for Weight, Height, Bench, and Squat, but I am planning on adding more options in the future.
- It also has a functional delete entry tab, but it is not very simple to use.

## Goals to add for future
- I would like to add a bar that displays only the maxes for every stat they have logged, on top of the graph of all of them. 
- I would like to make the delete entry feature more simple, at the moment its kind of confusing to use.
- I definately need to figure out how to save the data onto a datebase for each user, rather than locally on the browser.
- I also would add more options to the table, at the end, because this is obviously a very easy feature to add. I want to keep the current one as simple as possible so it will be easier to get the hard things done.

# College Board Describe Portion

## Line 1: Program Purpose and Function
- This program will be made by utilizting two github repositories (one for backend and one for frontend) and vscode for the coding itself.
- Purpose is to Allow users to log their physical progress/growth and Provide Users a simple way to track their max weight for various exercises
- Functionality: Stats tracker that allows users to track their physical and fitness growth. When you type a new max in a certain category and click "add" then it will add to the top of the graph
- Input your new max for height, weight, bench, squat etc. 
- Output: The user input is then outputted onto two seperate charts. One that is meant as a log for all the new maxes you have had (with dates) and one that simply displays all of your maxes.

## Line 2: Data Abstraction
- The first code segment will display the stats that a user inputted being stored into a database of somesort that I will code in the future
- This data will then be called and printed onto the two charts.
- The name of the variable will be "Athlete"
- The data contained in this list represents the statistics of the athlete, which the whole purpose of my program is to document.

## Line 3: Managing Complexity
- My data abstraction will be met using a database, but the list I will create will have to do with the printing of the data of each user. The list will contain the data and be assigned to a variable, rather than printing each individual data point
- The data will be named to the "Athlete" variable, and the program would not function without this list because the table would not not the athlete to which each max weight represents.

## Line 4: Procedural Abstraction
- The procedure I will be coding will involve creating the table that displays the max of each parameter which are the weight, height, bench, squat, etc. 
- This procedure will be called by defining the procedure eventually then printing it later.
- This procedure takes the maximum value from each parameter, that has been inputed by the user, and contributes to the functionality of the program because the function needs this procedure (that takes the max numerical input for each parameter) to work.

## Line 5: Algorithm Implementation
-  Iteration: The algorithm will iterate through the users history of logging maxes to find the max max for each weight.
- Selection: The algorithm will analzye the all the maxes they have reached and how recent to select to the user which exersize(s) they have made the most progress in
- Sequencing: The algorithm will analyze the logs the users have made of their maxes and supply their history of which exersizes they have hit the most.
- I will be able to explain how this algorithm works in detail, once I actually code it.

## Line 6: Testing
- There will be 4 (or more depending on each datapoint that I add) calls, based on each exersize max that I code.
- The condition that will be tested is the how great the number is in comparison to every other number that has been inputted for that parameter. Basically the condition is if it is the greatest weight that has been inputted for that exersize.
- The result of each call, for the max weight table, will be the max weight (of each parameter) that was abstracted from the procedure. 


# What I Will Show in My Video
- In my video I will would show the input of different maxes for each exersize on different dates. These inputs would then be outputted on the main chart or "stats table" that logs all of the maxes. Everytime I add a new max to a the main chart, it will also update the "max table" which would imply my algorithm, procedure, complexity, testing, abstraction, and function. As a bonus I would show that I can delete any entry as well. 