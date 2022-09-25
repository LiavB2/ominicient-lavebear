---
toc: true
layout: post
description: Music Shuffle Program for Java
categories: [Java]
title: Music Shuffle Song Selector with Java
---

### Submenu:
{% include navbar.html %}

## What is this program?
- This will be a program that randomly selects a song from a list, and gives you a spotify link to listen to it.

<button name="button" onclick="randomSelect()">Click Me</button>
<p id="Song Selector"></p>
<script>
const songList = ["https://open.spotify.com/track/39az7WzBipIvzCCTfpwtGa?si=5a3535af908f4640", "https://open.spotify.com/track/7d4W06sKxGEm40rYdQgEtt?si=12d41809294443a0", "https://open.spotify.com/track/0p7qrH9BepbFOukVfgzLu7?si=17941606f91b4fad", "https://open.spotify.com/track/21Qsj3cMVCx2xF2EVVNbEu?si=46626ccac8f34e90", "https://open.spotify.com/track/29tzJGvqJPTAFs6LXmsHoA?si=f4b93105aebb455f", "https://open.spotify.com/track/2nZ33CKRbgpJQJJQKHuGXb?si=d41c2a9440fd4202"]
function randomSelect() {
    var index=Math.floor(Math.random() *songList.length)
    document.getElementById("Song Selector").innerHTML = songList[index]
}

</script>