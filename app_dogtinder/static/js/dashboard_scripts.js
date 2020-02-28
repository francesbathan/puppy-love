///////// slider functionality for ratings ////////////

var slider = document.getElementsByClassName("slider");
var output = document.getElementsByClassName("output");

//Update the current slider value (each time you drag the slider handle)
function render() {
  for (var i = 0; i < slider.length; i++) {
    output[i].innerHTML = slider[i].value + "/10"; // Display the default values
  }
}

// When pages loads, get values
render();

// i know its es6, but i couldnt get it to work either way lol
document.querySelectorAll(".slider").forEach(element => {
  element.addEventListener("input", event => {
    event.innerHTML = event.target.value;
    render();
  });
});

///////// shuffle functionality for dogs ////////////

let deck = Array.from(new Array(totalRatings), (x, i) => i);

// hand.push(deck.splice(Math.floor(Math.random() * deck.length), 1)[0]);

// function stackShuffle(deck) {
//   let count = deck.length;
//   while (count) {
//     deck.push(deck.splice(Math.floor(Math.random() * count), 1)[0]);
//     count -= 1;
//   }
// }

// stackShuffle(rating_panel);