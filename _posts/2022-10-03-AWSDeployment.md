---
toc: true
layout: post
description: Display of successful AWS Deployment, curl command, docker command, and edits to flask site.
categories: [AWS]
title: AWS Deployment
---

# Build Site with docker compose command 
- As you can see, I was able to make the server with "sudo docker-compose up --build -d"

![]({{site.baseurl}}/images/workingdockercommand.png "https://github.com/LiavB2/ominicient-lavebear")

# Docker PS
- Here is our output for "sudo docker ps" command. 
- As you can see, it displays all of our group member's flasks (including the overall "lash" flask)

![]({{site.baseurl}}/images/sudodockerps.png "https://github.com/LiavB2/ominicient-lavebear")

# Curl Command 
- As you can see the curl command displays my Flask Site in the AWS instance:

![]({{site.baseurl}}/images/workingcurlcommand.png "https://github.com/LiavB2/ominicient-lavebear")

# Edits to Flask Page
- Now you can see that the flask page is updated with the new local host "8089" and PublicIPs: 3.16.187.234:

![]({{site.baseurl}}/images/flaskpagewithedits.png "https://github.com/LiavB2/ominicient-lavebear")

