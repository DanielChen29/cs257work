function changeColor() {
  the_heading = document.getElementById("hello");
  const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
  let i = colors.indexOf(the_heading.style.color)
  if (i < colors.length - 1) {
    the_heading.style.color = colors[i + 1];
  } else {
    the_heading.style.color = colors[0]
  }
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function changeNumber() {
  the_number = document.getElementById("big-num");
  the_number.innerText = Math.floor(Math.random() * 101);
  console.log("I just changed the lucky number to: " + the_number.innerText)  
}