---
toc: true
layout: post
description: Front end that we can possibly use for our Etracker project
categories: [Notes]
title: Fitness Frontend
---

<html>
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
