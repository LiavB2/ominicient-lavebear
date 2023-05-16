---
toc: true
layout: post
description: Likes Feature 
categories: [Notes]
title: ALAAT Likes Feature + Hours Tracking
---

# Hours I Worked

|Task #|Hours|Task|
|-|-|-|
|1|Plan out group project + Canva Model [Here](https://liavb2.github.io/ominicient-lavebear/notes/2023/05/12/ALAAT-Planning.html)|1 Hour|
|2|||
|3|||
|4|||
|5|||
|6|||
|7|||
|8|||
|9|||
|9|||
|10|||

# Feature Overview
- Like and comment system
    - The images will sort based on amount of likes and comments



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
                    Striver
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
                                Quotes
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"> Forum </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container mt-3">
            <h1>Forum</h1>
            <p class="text-muted">
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