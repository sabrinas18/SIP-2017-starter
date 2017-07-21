
var questionsList = ["What are your/your friend's favorite foods?", "What are your/your friend's favorite animals?", "What are your/your friend's favorite hangout spots?", "What do you/your friend's do when you're together?","Do you/your friend prefer chocolate or vanilla?","What is the best sport?"];
function init() {
  var randomIndex = Math.floor(Math.random() * questionsList.length);
  document.getElementById("question").innerHTML = questionsList[randomIndex];
}

window.onload = init;
var answerList = [];
function submitAnswer() {
  var answer = document.getElementById("answerInput").value;
  var answer2 = answer.toUpperCase();
  document.getElementById("answerInput").value = "";
  answerList.push(answer2);
}

function displayMessage (message) {
  document.getElementById("result").innerHTML = message
}

function checkGuess() {
  var guess = document.getElementById("guessInput").value;
  var guess2 = guess.toUpperCase();
  // This condition will display a certain message depending on the accuracy of the user's input.
  if (answerList.indexOf(guess2) == -1){
    displayMessage("Bummer... Guess you aren't best friends!");
  }

  else {
    displayMessage("Woah, you guys are best friends for sure!");
  }

}
