---
toc: true
layout: post
description: Group Front end blog + Hacks for our CPT project.
categories: [CPT]
title: Group CPT Front End
---

# What features have been coded? 
So far, the navbar, homepage, and workout logger have been coded. Ofcourse, all of these have not been completely coded, but rather have been made progress upon. 

# More about the features
1. homepage: The homepage includes the navbar and details about our web-app Etracker (name subject to change). The homepage will have clickable elements where the user can click to find more information about the web-app. 
2. Workout logger: The workout logger includes the navbar at the top and the workout tracker. The user can click the add workout button to, well, add a workout. The user can then click on which workout to log (still in development).
3. Navbar: The navbar nearly done. We still need to code the login button to do what it's supposed to, which is to redirect to a login page. We are planning to use oauth2 for the login. The login page will be designed shortly. The navbar includes all the pages that will be on the website. 


# Difficulties experienced
- Sure, it doesn't seem like a lot of features have been coded, but that is because we am doing extensive research on how to get the features to work. 
- For example, We were doing research on the workout logger, but it had to be cutshort inorder for the navbar to be developed.
    - Talking about the navbar, it was a pain in the butt to get it to work. Other files from the leuck project interefered with it and caused a bunch of errors. For example, the workout logger had bugged out and wasn't displaying/working how it is supposed to. 
    - So far, the easiest has been the CSS. We only had to search up the type of code we needed and followed tutorials to make it look how we want it to. 

# Few ways we modularized/ increased efficiency in our code
- The first way we did this is through dividing elements into different files (organized in folders) to make the code look more polished. 
    - We did this by linking the files into the html. For example, we would not code the JS into the html file. 
    - We rather added a source to the script tag and then linked the separate JS file to the script. 
- We also used scss to make our UI development more efficient. SCSS features such as mixins and vars were crucial and saved a lot of copy-pasta time. 

# Next steps towards the frontend development
- This week there will be strict deadlines towards the frontend development. 
- The main features that will need to be designed are: Log in page, completed workout tracker, and completed homepage. The user customization will also have been touched upon. More information will be on the scrumboard. 

# Project Frontend Progress:

## Homepage and Nav bar (with code)

![]({{site.baseurl}}/images/cpt1.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt2.png "https://github.com/LiavB2/ominicient-lavebear") 

## Workout Logger (with code)

![]({{site.baseurl}}/images/cpt6.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt3.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt4.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt5.png "https://github.com/LiavB2/ominicient-lavebear") 


# Gym Logging
- Here is also some progress we had in one of our features.
**Log your hours, Target Muscle Group, Exercises, Gym Location, and Hours in the Gym every week. **

<table id="gymTable">
    <tr>
        <td>Athlete</td>
        <td>Target Muscle Group</td>
        <td>Exercises</td>
        <td>Gym Location</td>
        <td>Time in Gym (Hours)</td>
    </tr>
    <tr>
        <td>Liav</td>
        <td>Legs</td>
        <td>3x12 Leg Press, 3x12 Squat, 3x14 Calf Raise, Hip Thrusters</td>
        <td>LA Fitness</td>
        <td>10 Hours</td>
    </tr>
    <tr>
        <td>Noor</td>
        <td>Chest</td>
        <td>3x12 Bench Press, 3x12 Chest Press, 3x30 Band Pushup, 3x12 Dumbell Incline Bench Press</td>
        <td>24 Hour Fitness</td>
        <td>12 hours</td>
    </tr>
</table>


## Add an entry
<table>
    <tr>
        <th><label for="athlete">Athlete</label></th>
        <th><label for="muscle">Muscle Group</label></th>
        <th><label for="exercise">Exercise</label></th>
        <th><label for="location">Gym Location</label></th>
        <th><label for="hours">Hours in the Gym</label></th>
    </tr>
    <tr>
        <td><input type="text" name="athlete" id="athlete" required></td>
        <td><input type="text" name="muscle" id="muscle" required></td>
        <td><input type="text" name="exercise" id="exercise" required></td>
        <td><input type="text" name="location" id="location" required></td>
        <td><input type="text" name="hours" id="hours" required></td>
        <td ><button onclick="create_Entry()">Add</button></td>
    </tr>
</table>

## Remove an entry
<table>
    <tr>
        <th><label for="num">Entry Number to Remove</label></th>
    </tr>
    <tr>
        <td><input type="number" name="num" id="num" required></td>
        <td ><button onclick="delete_Entry()">Delete</button></td>
    </tr>
</table>

<script>
function create_Entry() {
  var table = document.getElementById("gymTable");
  var row = table.insertRow(1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  cell1.innerHTML = document.getElementById("athlete").value;
  cell2.innerHTML = document.getElementById("muscle").value;
  cell3.innerHTML = document.getElementById("exercise").value;
  cell4.innerHTML = document.getElementById("location").value;
  cell5.innerHTML = document.getElementById("hours").value;
}

function delete_Entry() {
    var table = document.getElementById("gymTable");
    document.getElementsByTagName("tr")[document.getElementById("num").value].remove();
}

</script>

- As you can see, they user can input the values for the gym logging every week in order to track their fitness, as well as removing entries.
- However, at the moment, the data only stores locally so we are working on creating a database.