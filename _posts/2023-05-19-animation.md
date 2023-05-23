---
toc: true
layout: post
description: Frontend Discussion Board for the exit ticket discussion
categories: [Notes]
title: Frontend Javascrip Project
---


<!DOCTYPE html>
<html>
<head>
  <title>User Comments Board</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    #comment-form {
      margin-bottom: 10px;
    }
    #comments-board {
      border-collapse: collapse;
      width: 100%;
    }
    #comments-board th,
    #comments-board td {
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <h1>User Comments Board</h1>

  <form id="comment-form">
    <label for="name">Name:</label>
    <input type="text" id="name" required><br>
    <label for="comment">Comment:</label>
    <textarea id="comment" required></textarea><br>
    <button type="submit">Submit</button>
  </form>

  <table id="comments-board">
    <tr>
      <th>Name</th>
      <th>Comment</th>


<!DOCTYPE html>
<html>
<head>
  <title>Social Media Dashboard</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    .metrics {
      display: flex;
      justify-content: space-around;
      margin-bottom: 20px;
    }
    .metric-card {
      border: 1px solid #ccc;
      border-radius: 5px;
      padding: 10px;
      text-align: center;
    }
    .update-button {
      display: flex;
      justify-content: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Social Media Dashboard</h1>

  <div class="metrics">
    <div class="metric-card">
      <h2>Follower Count</h2>
      <p id="follower-count">Loading...</p>
      <button onclick="updateFollowerCount()">Update</button>
    </div>
    <div class="metric-card">
      <h2>Likes</h2>
      <p id="likes">Loading...</p>
      <button onclick="updateLikes()">Update</button>
    </div>
    <div class="metric-card">
      <h2>Comments</h2>
      <p id="comments">Loading...</p>
      <button onclick="updateComments()">Update</button>
    </div>
    <div class="metric-card">
      <h2>Engagement Rate</h2>
      <p id="engagement-rate">Loading...</p>
      <button onclick="updateEngagementRate()">Update</button>
    </div>
  </div>

  <script>
    // Simulated initial data (replace with real data retrieval)
    var followerCount = 15000;
    var likes = 500;
    var comments = 200;
    var engagementRate = ((likes + comments) / followerCount * 100).toFixed(2);

    // Function to update follower count
    function updateFollowerCount() {
      var newFollowerCount = parseInt(prompt("Enter new follower count:"));
      if (!isNaN(newFollowerCount)) {
        followerCount = newFollowerCount;
        updateMetrics();
      }
    }

    // Function to update likes
    function updateLikes() {
      var newLikes = parseInt(prompt("Enter new likes count:"));
      if (!isNaN(newLikes)) {
        likes = newLikes;
        updateMetrics();
      }
    }

    // Function to update comments
    function updateComments() {
      var newComments = parseInt(prompt("Enter new comments count:"));
      if (!isNaN(newComments)) {
        comments = newComments;
        updateMetrics();
      }
    }

    // Function to update engagement rate
    function updateEngagementRate() {
      var newEngagementRate = parseFloat(prompt("Enter new engagement rate:"));
      if (!isNaN(newEngagementRate)) {
        engagementRate = newEngagementRate.toFixed(2);
        updateMetrics();
      }
    }

    // Function to update metric values in the dashboard
    function updateMetrics() {
      document.getElementById("follower-count").textContent = followerCount.toLocaleString();
      document.getElementById("likes").textContent = likes.toLocaleString();
      document.getElementById("comments").textContent = comments.toLocaleString();
      document.getElementById("engagement-rate").textContent = engagementRate + "%";
    }

    // Initial update of metric values
    updateMetrics();
  </script>
</body>
</html>
