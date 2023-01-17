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
3. Navbar: The navbar nearly done. I still need to code the login button to do what it's supposed to, which is to redirect to a login page. We are planning to use oauth2 for the login. The login page will be designed shortly. The navbar includes all the pages that will be on the website. 


# Difficulties experienced
- Sure, it doesn't seem like a lot of features have been coded, but that is because we am doing extensive research on how to get the features to work. 
- For example, I was doing research on the workout logger, but it had to be cutshort inorder for the navbar to be developed.
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

![]({{site.baseurl}}/images/cpt3.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt4.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt5.png "https://github.com/LiavB2/ominicient-lavebear") 

![]({{site.baseurl}}/images/cpt6.png "https://github.com/LiavB2/ominicient-lavebear") 