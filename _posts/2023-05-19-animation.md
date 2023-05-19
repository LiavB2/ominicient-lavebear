---
toc: true
layout: post
description: Bear Animation example for the exit ticket discussion
categories: [Notes]
title: Bear Animation Example
---

<!DOCTYPE html>
<html>
  <head>
    <title>Bear Animation</title>
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
      spriteImage.src = "bear.png";
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