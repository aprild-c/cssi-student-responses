// Creating variables for the thumbs icons
var thumbsUp = document.getElementById("thumbsUp");
var thumbsDown = document.getElementById("thumbsDown");

// Creating variable for question input box and submit buttons
var questionInput = document.querySelector(".studentQuestions");

// When buttons for student student responses are clicked it confirms response
thumbsUp.addEventListener("click", function() {
  alert("Thank you for checking in!");
});

thumbsDown.addEventListener("click", function() {
  alert("Thank you for checking in!");
});

// When buttons for student responses are hovered over, it enlarges
thumbsUp.addEventListener("mouseover", function() {
  thumbsUp.style.maxWidth = '23%';
  questionInput.style.width = "100%";
});

thumbsUp.addEventListener("mouseout", function() {
  thumbsUp.style.maxWidth = '20%';
  thumbsUp.style.height = 'auto';
});

thumbsDown.addEventListener("mouseover", function() {
  thumbsDown.style.maxWidth = '23%';
});

thumbsDown.addEventListener("mouseout", function() {
  thumbsDown.style.maxWidth = '20%';
  thumbsDown.style.height = 'auto';
});
