// var elem = document.querySelector('input[type="range"]');

// var rangeValue = function() {
//   var newValue = elem.value;
//   var target = document.querySelector(".value");
//   target.innerHTML = newValue;
// };

// if (elem) {
//   console.warn("lilly sez hi");
//   elem.addEventListener("input", rangeValue);
// }

var slider = document.getElementById("myRange");
var output = document.getElementById("value");
output.innerHTML = slider.value + "/10"; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value + "/10";
};
