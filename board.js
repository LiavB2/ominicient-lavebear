class Person {
    constructor(name, comment) {
      this.name = name;
      this.comment = comment;
    }
  }
  
  function addComment() {
    var name = prompt("Enter your name:");
    var comment = prompt("Enter your comment:");
  
    var person = new Person(name, comment);
    user_list.push(person);
  }
  
  function generateBoard() {
    var boardContainer = document.getElementById("comments-board");
  
    for (var i = 0; i < user_list.length; i++) {
      var person = user_list[i];
  
      var nameHeader = document.createElement("h3");
      nameHeader.textContent = "Name: " + person.name;
  
      var commentParagraph = document.createElement("p");
      commentParagraph.textContent = "Comment: " + person.comment;
  
      boardContainer.appendChild(nameHeader);
      boardContainer.appendChild(commentParagraph);
      boardContainer.appendChild(document.createElement("hr"));
    }
  }
  
  // Create an empty array to store user comments
  var user_list = [];
  
  // Prompt the user for input
  var num_comments = parseInt(prompt("Enter the number of comments:"));
  
  for (var i = 0; i < num_comments; i++) {
    addComment();
  }
  
  // Generate the comments board
  generateBoard();
  
  // Convert the user list to JSON
  var user_json = JSON.stringify(user_list, null, 4);
  console.log("\nUser JSON:\n");
  console.log(user_json);
  