---
toc: true
layout: post
description:  Display of using Javascript and explaination of program/tables created with Javascript
categories: [Java]
title: JavaScript Usage
---

## Submenu:
- This is the navigation bar submenu I created with links to this page, and the Javascript program I created that outputs a random song from a playlist.

{% include navbar.html %}

## Coding of Navbar Submenu:
![]({{site.baseurl}}/images/navbar.png "https://github.com/LiavB2/ominicient-lavebear")

- As you can see, I created this table using Javascript and HTML fragments. This was made as an "include" so I can include this table in any post I want using the include command like so:

![]({{site.baseurl}}/images/include.png "https://github.com/LiavB2/ominicient-lavebear")

## Coding of Music Shuffle Song Selector:
![]({{site.baseurl}}/images/musicshuffle.png "https://github.com/LiavB2/ominicient-lavebear")

- I used numerous commands such as "var", "randomSelect()", "document.getElementById", "const", and "onclick"
- This function takes a list of links to songs from a spotify playlist, and their names, and outputs a link to a random song after the push of the button.