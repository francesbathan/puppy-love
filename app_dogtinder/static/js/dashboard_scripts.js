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
