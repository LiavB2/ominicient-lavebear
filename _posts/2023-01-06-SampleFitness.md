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
