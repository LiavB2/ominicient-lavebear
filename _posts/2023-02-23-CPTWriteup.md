---
toc: true
layout: post
description: A writup of what a submission to the Collegeboard APCSP Create a Performance Task would look like for my individual feature of our project.
categories: [CPT]
title: Create a Performance Task Writeup for Stats Feature
---

# [Video]()

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

![]({{site.baseurl}}/images/3.c.ii3.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.ii4.png "https://github.com/LiavB2/ominicient-lavebear")

### 3.c.ii

![]({{site.baseurl}}/images/3.c.iii.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.iii2.png "https://github.com/LiavB2/ominicient-lavebear")

![]({{site.baseurl}}/images/3.c.iii3.png "https://github.com/LiavB2/ominicient-lavebear")

### 3.c.iii
- These code segments display the two procedures that are abundant in this program: Create function and read function. Both functions utilize the parameters of Age, Weight, Bench, Squat, Pullup, Mile. The functions both utilize the data that was inputted by the user which is jsonified into json formatted data. This data is then fetched seperately into the create (post) and read functions. The read function displays the data onto the table which allows the user to see it. Whereas the create function allows the user to input new data that is then outputted using the read function. Overall, the Create function allows for the user input while the read function allows for the output that is seen on the front end.

3.c.iv.
- 

3.d.
3.d.i
First call:

Second Call:

3.d.ii.
Condition(s) tested by first call:

Condition(s) tested by second call:

3.d.iii.
Results of the first call:

Results of the second call:
