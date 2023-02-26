---
toc: true
layout: post
description: A writup of what a submission to the Collegeboard APCSP Create a Performance Task would look like for my individual feature of our project.
categories: [CPT]
title: Create a Performance Task Writeup for Stats Feature
---

# [Video](https://clipchamp.com/watch/urYOPfIh1FN)

# Writeup

## 3.a 
### 3.a.i
- The program presents an interactive table that logs the gym statistics of the user, to serve as a way for them to track their improvement in the gym. 

### 3.a.ii.
- The program allows the user to insert on a table their growing age, improved weight (to their liking gaining or losing), max bench press, squat, pullup, and mile time. The specific stats that the user inputs are then placed onto a table where the user can view their history of improvement based on all the inputs they have made over the time they have been using it.

### 3.a.iii.
- There are 6 inputs that the user types their specific data into manually: Age, weight, bench, squat, pullup, mile. These inputs are then signified by a "create" button which the user can click on using their moude that outputs their data onto the table. This is the process that is demonstrated in the video.

## 3.b
### 3.b.i

![]({{site.baseurl}}/images/3.b.i2.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.b.i3.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.b.i.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.b.i4.png "https://github.com/LiavB2/ominicient-lavebear")

### 3.b.ii

![]({{site.baseurl}}/images/3.b.ii.png "https://github.com/LiavB2/ominicient-lavebear")

### 3.b.iii
- There is one collection method displayed, which is a database. The database is called Class Athlete. It specifically names Age, Weight, Bench, Squat, and Pullup into the databse of stats that are assigned to "Athlete" or the user. This data then goes into the specifc "Elite" table that is assinged to the athlete.

### 3.b.iv.
- The data that is being stored into this database is Age, Weight, Bench, Squat, Pullup, Mile can be seen to be integers. These integers are inputted by the user and represent the max or improved or declined stats that the user endured over the period of time of their choosing. These inputs would have no purpose without this database that they are stored in and assinged to the corresponding variables.

### 3.b.v.
- The database managaes the complexity of this stat tracking program as the program could never work without it. Without this database, the inputs that the user completes on the frontend would go nowhere and there would be no program entirely. Due to the abundance of this database, the stats that are inputted by the user can be saved and ultimately outputted onto the frontend table.

## 3.c.
### 3.c.i.

- Procedure with Parameters:

![]({{site.baseurl}}/images/3.c.ii1.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.ii2.png "https://github.com/LiavB2/ominicient-lavebear")

- Call:

![]({{site.baseurl}}/images/3.c.i.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.ii4.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.ii3.png "https://github.com/LiavB2/ominicient-lavebear")


### 3.c.ii

![]({{site.baseurl}}/images/3.c.iii.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.iii2.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/updatedupdate.png "https://github.com/LiavB2/ominicient-lavebear")

### 3.c.iii
- These code segments display the two procedures that are abundant in this program: Create function and read function. Both functions utilize the parameters of Age, Weight, Bench, Squat, Pullup, Mile. The functions both utilize the data that was inputted by the user which is jsonified into json formatted data. This data is then fetched seperately into the create (post) and read functions. The read function displays the data onto the table which allows the user to see it. Whereas the create function allows the user to input new data that is then outputted using the read function. Overall, the Create function allows for the user input while the read function allows for the output that is seen on the front end.

### 3.c.iv.
- This program utilizes Iteration in the first code segment that is displayed. The function repeats the error message "(specific variable) is missing, or is less than 1 character" everytime the user trys to input a stat or data that is less than one character or does not input any data at all. This Error message will iterate until the requirement of at least 1 character is met in each input box. This algorithm is repeated 6 times for the 6 different variabes. The algorithm contains an if statement that declares that if the input of the specific variable is either nonexistent (none) or less than one character (len(Age)<1) then the function will return a 400 error and the message.
- The program then utilizaes Sequencing in the second code segment that is displayed. This is located in the create function of the program in which the user creates/inputs their personal statistics. The sequence instructs that for the input of Athlete (the user) it will print the output of the athlete.create() function unless there is an integrity error. This is done by utilizing a for ... in statement, specifically "for" the name of the class and "in" the user specifically. Then it writes "try:" in order to displau the print of the function that was prior created. Furthermore, it writes "except" when there is an integrity erorr and instructs the code to print the error message in this case.
- Finally, the program utilizes selection in the third code segment that is displayed. This is defined in the "create" function portion of the program. This selection signifies that only the inputs for each specific datapoin/stat that is inputed by the user that has any length (really meaning that only inputs with actual characters) will be selected as data that is used in the function. This is done by definding the variables at the start when defining the function itself, then using an if statement (that is repeated for each variable) which writes that if the input of that age is greater than 0 then the self function (assigns data to the user) will actually carry through on.  

## 3.d.
### 3.d.i
- First call: The first call is a fetch from the create function that is used to save the data that is inputted by the user (in json format) onto the database and eventually onto the front end. It fetches the json data from the database and resonds it into the datatable using response.json.
- Second Call: The second call is a fetch from the read function that is used to bring the data that is already stored into the database (in json format) in a viewable format on the front end. It fetches the json data from the database and resonds it into the datatable using response.json.

### 3.d.ii.
- Condition(s) tested by first call: The first call tests the condition that the data is in json format, that this json data alligns with the conditions that must be met in order for the create function to run (an integer with at least one character), and of course tests whether the Age, Weight, Bench, Squat, Pullup, Mile data were actully inputted or not.
- Condition(s) tested by second call: The second call solely tests whether the data that is fetched for the read function is in json format, and if the data was part of the self (athlete) database.

### 3.d.iii.
- Results of the first call: The result of the first call is creating data that is inputted by the user and formatting it onto the database.
- Results of the second call: The result of the second call is formatting the data that is already located in the database in json and displaying it in a readable manner fashion.
