---
toc: true
layout: post
description: Likes Feature 
categories: [Notes]
title: ALAAT Likes Feature + Hours Tracking
---

# Hours I Worked

|Task #|Date|Task|Hours|
|-|-|-|-|
|1|05/06/23|Plan out group project + Canva Model [Here](https://liavb2.github.io/ominicient-lavebear/notes/2023/05/12/ALAAT-Planning.html)|1 Hour|
|2|05/08/23|Research and collaboration on implementing the likes feature on each photo and determining what the best way to implement it will be|1 hour|
|3|05/09/23|Clean up repo to make it only our code|0.5|
|4|05/15-16/23|Develop a few prototype like systems (with multiple deigns)|1.5 hours|
|5|05/18/23|Research backend likes saving from last tri full stack lessons and write the code in the backend|1.5 Hours|
|6|05/19/23|Recall how to call an API backend to the frontend (this took me a whole week to learn last tri)|0.5 hours|
|7|05/20/23|Design and add logo to the top left of the frontend on the navbar make it clickable as a home button and make agile manifesto|1|
|8|||
|9|||
|10|||
|11|||
|12|||

# Feature Overview
- Like and comment system
    - The images will sort based on amount of likes and comments
- Make a button with a count request that adds +1 everytime the button is clicked.
    - Save amount of likes on each photo to backend 



# Some Demo Code

``` 
<!DOCTYPE html>
<html>
<head>
    <title>Forum Demo</title>
    <style>
        .post {
            margin-bottom: 10px;
            padding: 10px;
            background-color: #f2f2f2;
        }
        .comment {
            margin-left: 20px;
            margin-bottom: 5px;
        }
        .like-btn {
            color: blue;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="post-container">
        <!-- Posts will be added dynamically here -->
    </div>
    <script>
        // Data structure to hold posts
        let posts = [];

        // Function to add a post
        function addPost(title, content) {
            let post = {
                title: title,
                content: content,
                likes: 0,
                comments: []
            };
            posts.push(post);
            renderPosts();
        }

        // Function to add a comment to a post
        function addComment(postIndex, commentContent) {
            let comment = {
                content: commentContent,
                likes: 0
            };
            posts[postIndex].comments.push(comment);
            renderPosts();
        }

        // Function to like a post
        function likePost(postIndex) {
            posts[postIndex].likes++;
            renderPosts();
        }

        // Function to like a comment
        function likeComment(postIndex, commentIndex) {
            posts[postIndex].comments[commentIndex].likes++;
            renderPosts();
        }

        // Function to render posts and comments
        function renderPosts() {
            let postContainer = document.getElementById("post-container");
            postContainer.innerHTML = "";

            posts.forEach(function(post, postIndex) {
                let postElement = document.createElement("div");
                postElement.className = "post";
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                    <button class="like-btn" onclick="likePost(${postIndex})">Like</button>
                    <span>Likes: ${post.likes}</span>
                `;

                post.comments.forEach(function(comment, commentIndex) {
                    let commentElement = document.createElement("div");
                    commentElement.className = "comment";
                    commentElement.innerHTML = `
                        <p>${comment.content}</p>
                        <button class="like-btn" onclick="likeComment(${postIndex}, ${commentIndex})">Like</button>
                        <span>Likes: ${comment.likes}</span>
                    `;
                    postElement.appendChild(commentElement);
                });

                postContainer.appendChild(postElement);
            });
        }
    </script>
</body>
</html>
```

<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- imports bootstrap styling library -->
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Alaat Gallery Talk</title>
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
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="/striver-frontend/index.html">
                    <img
                        src="/striver-frontend/assets/icon.png"
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
                            <a
                                class="nav-link"
                                href="/striver-frontend/index.html"
                            >
                                Comments
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"> Gallery </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container mt-3">
            <h1>Comments and Likes</h1>
            <p class="text-muted">---
toc: true
layout: post
description: Planning for our tri 3 Final Project
categories: [Notes]
title: Group ALAAT Photo Site Planning
---
                Submit your thoughts & comments on each of the photos!
            </p>
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
                    placeholder="Your post"
                    id="commentText"
                ></textarea>
            </div>
            <div class="mb-3">
                <!-- submit button runs submit comment function -->
                <button onclick="submitPost()" class="btn btn-primary">
                    Submit
                </button>
            </div>
            <div id="postList"></div>
        </div>
        <script src="/striver-frontend/scripts/forum.js"></script>
    </body>
</html>


<html>
<head>
  <title>Like System Design 1</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
  <h1>Like System Design 1</h1>

  <div>
    <button id="object1" class="like-button">Like</button>
    <span id="object1-count">0</span>
  </div>

  <div>
    <button id="object2" class="like-button">Like</button>
    <span id="object2-count">0</span>
  </div>

  <!-- Add more objects as needed -->

  <script>
    $(document).ready(function() {
      $('.like-button').click(function() {
        var objectId = $(this).attr('id');
        incrementLikeCount(objectId);
      });

      function incrementLikeCount(objectId) {
        var countElement = $('#' + objectId + '-count');
        var count = parseInt(countElement.text());
        count++;
        countElement.text(count);
        // Send an AJAX request to update the backend with the new like count
        $.ajax({
          url: 'backend.php',
          type: 'POST',
          data: { objectId: objectId, count: count },
          success: function(response) {
            console.log(response);
          },
          error: function(xhr, status, error) {
            console.error(error);
          }
        });
      }
    });
  </script>
</body>
</html>

<html>
<head>
  <title>Like System Design 2</title>
</head>

<body>
  <h1>Like System Design 2</h1>

  <button id="likeButton" onclick="incrementLikeCount()">Like</button>

  <script>
    var likeCount = 0;

    function incrementLikeCount() {
      likeCount++;
      document.getElementById('likeButton').innerHTML = 'Like (' + likeCount + ')';
    }
  </script>
</body>
</html>

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

<!-- HTML button element -->
<button id="likeButton">Like</button>

<script>
  // JavaScript code
  const likeButton = document.getElementById('likeButton');

  likeButton.addEventListener('click', async () => {
    try {
      // Send an HTTP PATCH request to update the likes count
      const response = await fetch('http://127.0.0.1:8086/api/images/', {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ increment: 1 }), // Increment likes by 1
      });

      if (response.ok) {
        // Success
        const updatedData = await response.json();
        console.log('Likes count updated:', updatedData.likes);
      } else {
        // Error
        console.error('Failed to update likes count:', response.status);
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  });
</script>
