---
toc: true
layout: post
description: ALAAT Likes and comments feature demo
categories: [Notes]
title: Likes and Comments Sample Front End
---

<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- imports bootstrap styling library -->
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- CSS only -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi"
            crossorigin="anonymous"
        />
        <link
            rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css"
        />
        <!-- JavaScript Bundle with Popper -->
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3"
            crossorigin="anonymous"
        ></script>
        <title>Striver Home</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <img
                        src="/ominicient-lavebear/images/smiley.png"
                        width="30"
                        height="30"
                        class="d-inline-block align-top rounded"
                        style="margin-right: 10px"
                        alt=""
                    />
                    ALAAT
                </a>
                <button
                    class="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div
                    class="collapse navbar-collapse"
                    id="navbarSupportedContent"
                >
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="#">Quotes</a>
                        </li>
                        <li class="nav-item">
                            <a
                                class="nav-link"
                                href="/striver-frontend/forum.html"
                                >Forum</a
                            >
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container mt-3">
            <div class="row">
                <!-- creates first column in layout -->
                <div class="col-sm">
                    <!-- site header -->
                    <h1>Striver</h1>
                    <p class="text-muted">
                        Created by Liav Bar, Taiyo, Arnav, Adi, Amay | Mortensen
                        Period 4
                    </p>
                    <p>
                        Welcome to ALAAT Photo Gallery! Take a look at this gallery
                        <a href="/striver-frontend/forum.html">Forum</a> to
                        freely post and discuss your thoughts on the images. You can even react
                        to the artists photos with cool emoji reactions! All of
                        your comments, likes, and reactions are persisted
                        to our backend, so you'll never have to worry about
                        losing track of them.
                    </p>
                    <button
                        type="button"
                        class="btn btn-primary"
                        onclick="getQuote()"
                    >
                        Get new quote
                    </button>
                    <!-- display quote using bootstrap -->
                    <figure class="mt-3">
                        <blockquote class="blockquote">
                            <p id="quote"></p>
                        </blockquote>
                        <figcaption
                            class="blockquote-footer"
                            id="quoteAuthor"
                        ></figcaption>
                    </figure>
                    <!-- bootstrap button for liking quote -->
                    <!-- btn-success = green -->
                    <!-- on click, run the increment likes function -->
                    <button
                        type="button"
                        class="btn btn-success"
                        onclick="incrementLikes()"
                    >
                        <span id="likeCount">N/A</span>
                        <!-- thumbs up icon -->
                        <i class="bi bi-hand-thumbs-up-fill"></i>
                    </button>
                    <button
                        type="button"
                        class="btn btn-danger"
                        onclick="incrementDislikes()"
                    >
                        <span id="dislikeCount">N/A</span>
                        <i class="bi bi-hand-thumbs-down-fill"></i>
                    </button>
                </div>
                <!-- second layout column -->
                <div class="col-sm">
                    <h2>Add a comment</h2>
                    <!-- form to submit new comment -->
                    <div class="mb-3">
                        <!-- name input -->
                        <input
                            type="text"
                            id="commentName"
                            placeholder="Name"
                            class="form-control"
                        />
                    </div>
                    <div class="mb-3">
                        <!-- comment textarea (large text box) -->
                        <textarea
                            class="form-control"
                            placeholder="Your comment"
                            id="commentText"
                        ></textarea>
                    </div>
                    <div class="mb-3">
                        <!-- submit button runs submit comment function -->
                        <button
                            onclick="submitComment()"
                            class="btn btn-primary"
                        >
                            Submit
                        </button>
                    </div>
                    <h2 id="commentsh2">Comments</h2>
                    <!-- displays all the comments in a list -->
                    <div id="commentList"></div>
                </div>
            </div>
        </div>
        <script src="/striver-frontend/scripts/quotes.js"></script>
    </body>
</html>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css" />
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar {
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .navbar-brand {
            display: flex;
            align-items: center;
            font-weight: bold;
        }
        .navbar-brand img {
            margin-right: 10px;
            border-radius: 50%;
        }
        .navbar-nav .nav-item {
            margin-right: 15px;
        }
        .container {
            margin-top: 30px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 30px;
        }
        h1 {
            font-size: 28px;
            margin-bottom: 20px;
        }
        .text-muted {
            margin-bottom: 30px;
        }
        p {
            margin-bottom: 15px;
        }
        .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
            font-size: 16px;
            padding: 10px 20px;
        }
        .btn-primary:hover {
            background-color: #0069d9;
            border-color: #0062cc;
        }
        .mt-3 {
            margin-top: 20px;
        }
        .blockquote {
            font-size: 18px;
            margin-bottom: 15px;
        }
        .blockquote-footer {
            font-size: 14px;
        }
        .btn-success,
        .btn-danger {
            padding: 5px 10px;
            font-size: 16px;
        }
        .bi-hand-thumbs-up-fill,
        .bi-hand-thumbs-down-fill {
            vertical-align: middle;
        }
        .col-sm {
            margin-bottom: 30px;
        }
        h2 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .form-control {
            margin-bottom: 15px;
        }
        #commentList {
            margin-top: 20px;
        }
    </style>
    <title>ALAAT Gallery Home</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="#">
                <img src="/ominicient-lavebear/images/smiley.png" width="30" height="30" class="d-inline-block align-top rounded" alt="" />
                ALAAT
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler

<!DOCTYPE html>
<html>
<head>
  <title>Forum</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    #posts-container {
      margin: 20px;
    }
    .post {
      margin-bottom: 20px;
      padding: 10px;
      background-color: #f5f5f5;
      border-radius: 5px;
    }
    .post h3 {
      margin-top: 0;
      color: #333;
    }
    .post p {
      color: #666;
    }
    .post button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 3px;
      cursor: pointer;
    }
    .post button:hover {
      background-color: #45a049;
    }
    .post .likes {
      color: #888;
      font-size: 12px;
    }
  </style>
  <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-database.js"></script>
  <script>
    // Initialize Firebase
    var firebaseConfig = {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_AUTH_DOMAIN",
      databaseURL: "YOUR_DATABASE_URL",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_STORAGE_BUCKET",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID"
    };
    firebase.initializeApp(firebaseConfig);
    // Get a reference to the database service
    var database = firebase.database();
    // Function to handle like button click
    function likePost(postId) {
      // Get the current number of likes from the database
      var postRef = database.ref('posts/' + postId);
      postRef.once('value', function(snapshot) {
        var likes = snapshot.val().likes || 0;
        // Update the number of likes
        postRef.update({ likes: likes + 1 });
      });
    }
    // Function to render sorted posts
    function renderSortedPosts(posts) {
      var sortedPosts = Object.keys(posts).sort(function(a, b) {
        var likesA = posts[a].likes || 0;
        var likesB = posts[b].likes || 0;
        return likesB - likesA;
      });
      renderPosts(sortedPosts);
    }
    // Function to render posts
    function renderPosts(posts) {
      var container = document.getElementById('posts-container');
      container.innerHTML = '';
      for (var i = 0; i < posts.length; i++) {
        var postId = posts[i];
        var post = posts[postId];
        var postElement = document.createElement('div');
        postElement.className = 'post';
        postElement.innerHTML = `
          <h3>${post.title}</h3>
          <p>${post.content}</p>
          <button onclick="likePost('${postId}')">Like</button>
          <span class="likes">Likes: ${post.likes || 0}</span>
        `;
        container.appendChild(postElement);
      }
    }
    // Retrieve posts from the database
    var postsRef = database.ref('posts');
    postsRef.on('value', function

<!DOCTYPE html>
<html>
<head>
  <title>Forum</title>
  <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-database.js"></script>
  <script>
    // Initialize Firebase
    var firebaseConfig = {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_AUTH_DOMAIN",
      databaseURL: "YOUR_DATABASE_URL",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_STORAGE_BUCKET",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID"
    };
    firebase.initializeApp(firebaseConfig);
    // Get a reference to the database service
    var database = firebase.database();
    // Function to handle like button click
    function likePost(postId) {
      // Get the current number of likes from the database
      var postRef = database.ref('posts/' + postId);
      postRef.once('value', function(snapshot) {
        var likes = snapshot.val().likes || 0;    
        // Update the number of likes
        postRef.update({ likes: likes + 1 });
      });
    }
  </script>
</head>
<body>
  <h1>Forum</h1>
  <div id="posts-container"></div>

  <script>
    // Function to render posts
    function renderPosts(posts) {
      var container = document.getElementById('posts-container');
      container.innerHTML = '';

      for (var postId in posts) {
        var post = posts[postId];
        var postElement = document.createElement('div');
        postElement.innerHTML = `
          <h3>${post.title}</h3>
          <p>${post.content}</p>
          <button onclick="likePost('${postId}')">Like</button>
          <span>Likes: ${post.likes || 0}</span>
        `;
        container.appendChild(postElement);
      }
    }

    // Retrieve posts from the database
    var postsRef = database.ref('posts');
    postsRef.on('value', function(snapshot) {
      var posts = snapshot.val();
      renderPosts(posts);
    });
  </script>
</body>
</html>

<!DOCTYPE html>
<html>
  <head>
    <title>Sprite Animation</title>
    <style>
      canvas {
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    <canvas id="canvas" width="800" height="600"></canvas>
    <script>
      // Get the canvas element
      const canvas = document.getElementById("canvas");
      const context = canvas.getContext("2d");
      // Load the sprite image
      const spriteImage = new Image();
      spriteImage.src = "sprite.png";
      // Set the initial position and speed of the sprite
      let spriteX = 100;
      let spriteY = 100;
      const spriteSpeed = 5;
      // Set the animation frames
      const frames = [];
      const frameWidth = 64;
      const frameHeight = 64;
      for (let i = 0; i < 6; i++) {
        const frame = {
          image: spriteImage,
          sx: i * frameWidth,
          sy: 0,
          sw: frameWidth,
          sh: frameHeight,
        };
        frames.push(frame);
      }
      // Set the initial frame index and animation delay
      let currentFrame = 0;
      const animationDelay = 10; // Lower value means faster animation
      // Function to update the animation frame
      function updateFrame() {
        currentFrame = (currentFrame + 1) % frames.length;
      }
      // Function to draw the sprite
      function drawSprite() {
        const frame = frames[currentFrame];
        context.drawImage(
          frame.image,
          frame.sx,
          frame.sy,
          frame.sw,
          frame.sh,
          spriteX,
          spriteY,
          frame.sw,
          frame.sh
        );
      }
      // Function to handle keyboard input
      function handleInput() {
        window.addEventListener("keydown", (event) => {
          switch (event.key) {
            case "ArrowLeft":
              spriteX -= spriteSpeed;
              break;
            case "ArrowRight":
              spriteX += spriteSpeed;
              break;
            case "ArrowUp":
              spriteY -= spriteSpeed;
              break;
            case "ArrowDown":
              spriteY += spriteSpeed;
              break;
          }
        });
      }
      // Game loop
      function gameLoop() {
        // Clear the canvas
        context.clearRect(0, 0, canvas.width, canvas.height);
        // Update the animation frame
        if (Date.now() % animationDelay === 0) {
          updateFrame();
        }
        // Draw the sprite
        drawSprite();
        // Request the next frame
        requestAnimationFrame(gameLoop);
      }
      // Start the game loop
      handleInput();
      gameLoop();
    </script>
  </body>
</html>

