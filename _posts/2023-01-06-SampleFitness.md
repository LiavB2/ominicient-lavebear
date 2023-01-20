---
toc: true
layout: post
description: Front end that we can possibly use for our Etracker project
categories: [CPT]
title: Fitness Frontend
---

<html>
  <head>
    <title>Fitness Tracker</title>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#features">Features</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <section id="about">
        <h1>About Our Fitness Tracker</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra euismod odio, gravida pellentesque urna varius vitae.</p>
      </section>
      <section id="features">
        <h1>Features</h1>
        <ul>
          <li>Track your workouts</li>
          <li>Set and track goals</li>
          <li>Connect with friends for added motivation</li>
          <li>View progress and statistics</li>
        </ul>
      </section>
      <section id="pricing">
        <h1>Pricing</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra euismod odio, gravida pellentesque urna varius vitae.</p>
      </section>
      <section id="contact">
        <h1>Contact Us</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra euismod odio, gravida pellentesque urna varius vitae.</p>
      </section>
    </main>
    <footer>
      <p>Copyright ©2022 Fitness Tracker</p>
    </footer>
  </body>
</html>

<head>
  <title>Fitness Tracker</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <header>
    <h1>Fitness Tracker</h1>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Exercises</a></li>
        <li><a href="#">Statistics</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section id="exercise-form">
      <h2>Log an Exercise</h2>
      <form>
        <label for="exercise-name">Exercise Name:</label>
        <input type="text" id="exercise-name" name="exercise-name">
        <label for="reps">Reps:</label>
        <input type="number" id="reps" name="reps">
        <label for="sets">Sets:</label>
        <input type="number" id="sets" name="sets">
        <label for="weight">Weight (kg):</label>
        <input type="number" id="weight" name="weight">
        <button type="submit">Submit</button>
      </form>
    </section>
    <section id="exercise-log">
      <h2>Exercise Log</h2>
      <table>
        <tr>
          <th>Exercise Name</th>
          <th>Reps</th>
          <th>Sets</th>
          <th>Weight (kg)</th>
          <th>Date</th>
        </tr>
        <tr>
          <td>Bench Press</td>
          <td>8</td>
          <td>3</td>
          <td>70</td>
          <td>2022-01-01</td>
        </tr>
      </table>
    </section>
  </main>
  <footer>
    <p>Made by Liav Bar</p>
  </footer>
  <script src="main.js"></script>
</body>
</html>

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #4CAF50;
  color: white;
  text-align: center;
  padding: 1em;
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

nav li {
  float: left;
}

nav a {
  color: white;
  text-align: center;
  padding: 1em;
  text-decoration: none;
}

main {
  margin: 2em;
}

section {
  margin-bottom: 2em;
}

footer {
  background-color: #4CAF50;
  color: white;
  text-align: center;
  padding: 1em;
  position: absolute;
  bottom: 0;
  width: 100%;
}


# Attempt at Calendar 

{% extends "layouts/base.html" %}
{% set project = "Calendar" %}

{% block body %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendar</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div id="container">
      <div id="calendarHeader">
        
          
  </body>

<style>
/* saved events */

#eventcontainer {
  width: 450px;
  height: 728px;
  background: #222;
  float: right;
  right: 120px;
  position: relative;
  bottom: 685px;
  font-family: 'montserrat', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: left;
  color: white;
}

#eventtitle {
  background-color: #167b7e;
  padding: 5px;
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
}

#scheduledevents {
  padding: 10px;
  font-size: 25px;
}

/* saved events */

/*WEATHER THING  */
.H, .L {
  font-weight: 500;
  font-style: italic;
  padding: 5px;
}
.icon {
  display: flex;
}
.weather {
  font-size: 25px;
  font-weight: 900;
  font-style: italic;
  margin-bottom: 15px;

}
.search {
  width: 100%;
  height: 100%;
  width: 450px;
  height: 100px;
  background-color: rgb(8, 112, 112);
  align-items: center;
  justify-content: center;
  display: flex;
}  
.searchbar {
  width: 100%;
  width: 300px;
  height: 35px;
  display: flex;
}
i {
  height: 100%;
  height: 25px;
  align-items: center;
  display: flex;
  justify-content: center;
  font-size: 23px;
}
#weatherContainer {
  width: 450px;
  height: 728px;
  background: #222;
  align-items: center;
  float: right;
  right: 5px;
  position: relative;
  bottom: 685px;
  font-family: 'montserrat', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  
}
#weatherHeader {
  width: 100%;
  width: 450px;
  height: 450px;
  background-color: #002d44;
  display: flex;
  align-items: center;
}
.city, .currenttemp, .weather, .H, .L, .icon {
  text-shadow:#38878a, 5px;
  opacity: 100%;
  display: flex;
  align-items: center;
  color: antiquewhite;
  /* transform: translateX(25%); */
  justify-content: center;
  text-align: center;
}
.currenttemp {
  font-size: 50px;
  font-weight: 900;
  margin: 30px 0px;
  text-shadow: 2px 3px rgba(0, 0, 0, 0.6);
}


/* WEATHER THING */





/* #month h1 {
  font-size: 3rem;
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.2rem;
  margin-bottom: 1rem;
}

#month p {
  font-size: 1.6rem;
} */

button {
    width: 75px;
    cursor: pointer;
    box-shadow: 0px 0px 2px gray;
    border: none;
    outline: none;
    padding: 5px;
    border-radius: 5px;
    color: rgb(255, 255, 255);
    
  }
  
  #calendarHeader {
    font-size: 50px;
    color: white;
    background-color: rgb(76, 159, 140);
    text-align: center;
  }

  #calendartop {
    padding: 10px;
    color: white;
    font-size: 26px;
    font-family: sans-serif;
    display: flex;
    justify-content: space-between;
  }
  /* #month {
    height: 200px;
  } */

  #backButton {
    background-color: #167b7e;
    position: relative;
    left: 650px;
  }
  #nextButton {
    background-color: #167b7e;
    position: relative;
    left: 650px;
  }

  #container {
    width: 770px;
    background-color: rgb(0, 0, 0, 0.85);
    left: 5px;
  }
  #weekdays {
    width: 100%;
    display: flex;
    color: white;
    justify-content: right;
    background-color: #167b7e;
  }
  #weekdays div {
    width: 110px;
    padding: 10px;
    
  }
  #calendar {
    width: 100%;
    margin: auto;
    display: flex;
    flex-wrap: wrap;
  }
  .day {
    width: 100px;
    padding: 10px;
    height: 100px;
    cursor: pointer;
    box-sizing: border-box;
    background-color: rgb(51, 51, 51);
    margin: 5px;
    box-shadow: 0px 0px 3px #CBD4C2;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: white;
  }
  .day:hover {
    background-color: #38878a;
  }

  .day + #currentDay {
    background-color:#e8f4fa;
  }
  
  .padding {
  cursor: default !important;
  background-color: #FFFCFF !important;
  box-shadow: none !important;
}

#newEventPopup, #deleteEventPopup {
  display: none;
  z-index: 20;
  padding: 25px;
  background-color: #002d44;
  box-shadow: 0px 0px 3px black;
  border-radius: 5px;
  width: 350px;
  top: 100px;
  left: calc(50% - 175px);
  position: absolute;
  font-family: sans-serif;
  color: white;
}
#eventTitleInput {
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 25px;
  border-radius: 3px;
  outline: none;
  border: none;
  box-shadow: 0px 0px 3px gray;
}

#cancelButton, #deleteButton {
  background-color: rgb(221, 0, 0);
  border-radius: 11px;
  color: white;
  border-color: white;
}
#saveButton, #closeButton {
  background-color: #38878a;
  border-radius: 10px;
  border: 5px;
  border-color: white;
  color: white;
}

#eventcontainer {
  width: 450px;
  height: 728px;
  background: #222;
  float: right;
  right: 120px;
  position: relative;
  bottom: 685px;
  font-family: 'montserrat', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: left;
  color: white;
}

#eventtitle {
  background: #5bb375;
  padding: 5px;
  height: 60px;
}

#PopupBackDrop {
  display: none;
  top: 0px;
  left: 0px;
  z-index: 10;
  width: 100%;
  height: 100%;
  position: absolute;
  background-color: rgba(0,0,0,0.8);
}

</style>
    
<script>
  // steven
  
    var savedEvents = {
      
    }

    function updateCal() {
      console.log("retrieving clicked date");
      console.log(clicked);
      // savedEvents[clicked + ' events'] = Array();
      savedEvents[clicked + ' ' + document.getElementById("calendarHeader").innerText + ' events'].push(document.getElementById('eventTitleInput').value);
      document.getElementById('eventTitleInput').value = ''
      closePopup();
      console.log(savedEvents)
      notemptylists = new Array();
      for (const [k, v] of Object.entries(savedEvents)) {
        if (!Array.isArray(v) || v.length) {
          notemptylists.push(k + ": " + v);
        }
      }
      document.getElementById("scheduledevents").innerText = notemptylists.join("\n");
    }
  
  // steven

  //noor
  //just defining some variables 
    const newEventPopup = document.getElementById('newEventPopup');
    const deleteEventPopup = document.getElementById('deleteEventPopup');
    const backDrop = document.getElementById('PopupBackDrop');
    const eventTitleInput = document.getElementById('eventTitleInput');

  //open and close popup: when you click on a specific date, it opens the hidden element eventpopup. 
  //when you click cancel, it closes the popup
    function openPopup(date) {
    clicked = date;
    const eventForDay = events.find(e => e.date === clicked);

    if (eventForDay) {
      document.getElementById('eventText').innerText = eventForDay.title;
      deleteEventPopup.style.display = 'block';
    } else {
      newEventPopup.style.display = 'block';
    }

    backDrop.style.display = 'block';
  }

  function closePopup() {
    deleteEventPopup.style.display = 'none';
    newEventPopup.style.display= 'none';
    backDrop.style.display = 'none';
  }

  let monthNav = 0;
  let clicked = null;
  let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

  const calendar = document.getElementById('calendar');
  

//code for calendar render, prev/next days, and more date stuff using javascripts built-in date api
  function renderCalendar() {
    
    const date = new Date();

    const day = date.getDate();
    const month = date.getMonth();
    const year = date.getFullYear();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayOfMonth = new Date(year, month, 1);
    const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  
    const dateString = firstDayOfMonth.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'numeric',
      day: 'numeric', 

    }); //a line of the date elements


    
  document.getElementById('calendarHeader').innerText = 
    `${date.toLocaleDateString('en-us', { month: 'long' })} ${year}`; //setting the inner text of an element to the local date string

  
  calendar.innerHTML = '';
  
  const prevDays = weekdays.indexOf(dateString.split(', ')[0]); //splitting the date string to find the prev days

  //set i =1 and then we will keep looping the function because we have to render the empty square for the prev days
  //as i increments, it will create a daysquare div which has a class of day
    for(let i = 1; i <= prevDays + daysInMonth; i++) {
      const daySquare = document.createElement('div');
      daySquare.classList.add('day');

      //rendering previous day or actual daysquare? checking if we have iterated more times than there are prev days
      //we are then adding the 'padding element' to the prevdays if the amount of iterations is less than or equal to the prev days
      //if greater, we are setting the inner text of the daysquare to i - the amount of prev days to get the actual day
        if (i > prevDays) {
          daySquare.innerText = i - prevDays;
          daySquare.addEventListener('click', () => openPopup(daySquare.innerHTML));
          savedEvents[daySquare.innerHTML + ' ' + document.getElementById("calendarHeader").innerText + ' events'] = Array();
        } 
        else {
          daySquare.classList.add('padding');
        }
    calendar.appendChild(daySquare);
    }
  
  } 

  function saveEvent(day, input) { //function that has the day and the userinput as the parameters

  }
//noor

  //weather stuff:
  //alan or liav explain
  let weather = {
    apiKey: "b95c3461498620c129a3d6a6b675c29b",
    fetchWeather: function (city) {
      fetch(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=b95c3461498620c129a3d6a6b675c29b"
      )
        .then((res) => res.json())
        .then((data) => this.displayWeather(data));
    },
    //alan or liav

    //noor
    displayWeather: function(data) {
      const { name } = data;
      const { icon, description } = data.weather[0];
      const { temp } = data.main;
      const { temp_max, temp_min } = data.main
      console.log(name,icon,description,temp,temp_max,temp_min)
      document.querySelector(".city").innerText = "Weather in " + name;
      document.querySelector(".icon").src = "https://openweathermap.org/img/wn/" + icon + "@2x.png"
      document.querySelector(".weather").innerText = "Weather description:" + " " + description;
      document.querySelector(".currenttemp").innerText = temp + "℉"
      document.querySelector(".H").innerText = "High: " + temp_max + "℉"
      document.querySelector(".L").innerText = "Low: " + temp_min + "℉"
    },
    search: function () {
      this.fetchWeather(document.querySelector(".searchbar").value);
    },
  };

  renderCalendar();


</script>

</body>
</html>
{% endblock %}

