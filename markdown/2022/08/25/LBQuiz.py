<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="twitter:card" content="summary_large_image" /><!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Python Quiz | LB Blogs</title>
<meta name="generator" content="Jekyll v4.1.1" />
<meta property="og:title" content="Python Quiz" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Liav’s Python Quiz questions" />
<meta property="og:description" content="Liav’s Python Quiz questions" />
<link rel="canonical" href="https://liavb2.github.io/ominicient-lavebear/markdown/2022/08/25/LBQuiz.py" />
<meta property="og:url" content="https://liavb2.github.io/ominicient-lavebear/markdown/2022/08/25/LBQuiz.py" />
<meta property="og:site_name" content="LB Blogs" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2022-08-25T00:00:00-05:00" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="Python Quiz" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","dateModified":"2022-08-25T00:00:00-05:00","datePublished":"2022-08-25T00:00:00-05:00","description":"Liav’s Python Quiz questions","headline":"Python Quiz","mainEntityOfPage":{"@type":"WebPage","@id":"https://liavb2.github.io/ominicient-lavebear/markdown/2022/08/25/LBQuiz.py"},"url":"https://liavb2.github.io/ominicient-lavebear/markdown/2022/08/25/LBQuiz.py"}</script>
<!-- End Jekyll SEO tag -->
<link rel="stylesheet" href="/ominicient-lavebear/assets/css/style.css"><link type="application/atom+xml" rel="alternate" href="https://liavb2.github.io/ominicient-lavebear/feed.xml" title="LB Blogs" /><link rel="shortcut icon" type="image/x-icon" href="/ominicient-lavebear/images/favicon.ico"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Primer/15.2.0/primer.css" integrity="sha512-xTz2ys4coGAOz8vuV1NcQBkgVmKhsSEtjbqyMJbBHRplFuvKIUo6xhLHpAyPt9mfR6twHJgn9OgVLuqOvjeBhg==" crossorigin="anonymous" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />

<script>
function wrap_img(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        var elements = document.querySelectorAll(".post img");
        Array.prototype.forEach.call(elements, function(el, i) {
            if (el.getAttribute("title") && (el.className != "emoji")) {
                const caption = document.createElement('figcaption');
                var node = document.createTextNode(el.getAttribute("title"));
                caption.appendChild(node);
                const wrapper = document.createElement('figure');
                wrapper.className = 'image';
                el.parentNode.insertBefore(wrapper, el);
                el.parentNode.removeChild(el);
                wrapper.appendChild(el);
                wrapper.appendChild(caption);
            }
        });
    } else { document.addEventListener('DOMContentLoaded', fn); }
}
window.onload = wrap_img;
</script>

<script>
    document.addEventListener("DOMContentLoaded", function(){
    // add link icon to anchor tags
    var elem = document.querySelectorAll(".anchor-link")
    elem.forEach(e => (e.innerHTML = '<i class="fas fa-link fa-xs"></i>'));
    });
</script>
</head>
<body><header class="site-header">

  <div class="wrapper"><a class="site-title" rel="author" href="/ominicient-lavebear/">LB Blogs</a><nav class="site-nav">
        <input type="checkbox" id="nav-trigger" class="nav-trigger" />
        <label for="nav-trigger">
          <span class="menu-icon">
            <svg viewBox="0 0 18 15" width="18px" height="15px">
              <path d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.032C17.335,0,18,0.665,18,1.484L18,1.484z M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.032C17.335,6.031,18,6.696,18,7.516L18,7.516z M18,13.516C18,14.335,17.335,15,16.516,15H1.484 C0.665,15,0,14.335,0,13.516l0,0c0-0.82,0.665-1.483,1.484-1.483h15.032C17.335,12.031,18,12.695,18,13.516L18,13.516z"/>
            </svg>
          </span>
        </label>

        <div class="trigger"><a class="page-link" href="/ominicient-lavebear/about/">Notes</a><a class="page-link" href="/ominicient-lavebear/about/">About Creator</a><a class="page-link" href="/ominicient-lavebear/search/">Search</a><a class="page-link" href="/ominicient-lavebear/categories/">Tags</a></div>
      </nav></div>
</header>
<main class="page-content" aria-label="Content">
      <div class="wrapper">
        <article class="post h-entry" itemscope itemtype="http://schema.org/BlogPosting">

  <header class="post-header">
    <h1 class="post-title p-name" itemprop="name headline">Python Quiz</h1><p class="page-description">Liav's Python Quiz questions</p><p class="post-meta post-meta-title"><time class="dt-published" datetime="2022-08-25T00:00:00-05:00" itemprop="datePublished">
        Aug 25, 2022
      </time>
       • <span class="read-time" title="Estimated read time">
    
    
      1 min read
    
</span></p>

    
      <p class="category-tags"><i class="fas fa-tags category-tags-icon"></i></i> 
      
        <a class="category-tags-link" href="/ominicient-lavebear/categories/#markdown">markdown</a>
        
      
      </p>
    

    </header>

  <div class="post-content e-content" itemprop="articleBody">
    <ul id="toc" class="section-nav">
</ul>## Python Quiz:

import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that were previously developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command is used to evaluate correct or incorrect response in this example?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))

def question_and_answer(What is the definition of "ominicient"):
    print("Question: " + prompt)
    msg = input()
    print("Infinitely knowledgable: " + msg)
  </div><a class="u-url" href="/ominicient-lavebear/markdown/2022/08/25/LBQuiz.py" hidden></a>
</article>

      </div>
    </main><footer class="site-footer h-card">
  <data class="u-url" href="/ominicient-lavebear/"></data>

  <div class="wrapper">

    <div class="footer-col-wrapper">
      <div class="footer-col">
        <p class="feed-subscribe">
          <a href="/ominicient-lavebear/feed.xml">
            <svg class="svg-icon orange">
              <use xlink:href="/ominicient-lavebear/assets/minima-social-icons.svg#rss"></use>
            </svg><span>Subscribe</span>
          </a>
        </p>
      </div>
      <div class="footer-col">
        <p>CSP Blogs by LB</p>
      </div>
    </div>

    <div class="social-links"><ul class="social-media-list"><li><a rel="me" href="https://github.com/fastai" target="_blank" title="fastai"><svg class="svg-icon grey"><use xlink:href="/ominicient-lavebear/assets/minima-social-icons.svg#github"></use></svg></a></li><li><a rel="me" href="https://twitter.com/fastdotai" target="_blank" title="fastdotai"><svg class="svg-icon grey"><use xlink:href="/ominicient-lavebear/assets/minima-social-icons.svg#twitter"></use></svg></a></li></ul>
</div>

  </div>

</footer>
</body>

</html>
