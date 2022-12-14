// Animate.style animation handling

document.documentElement.style.setProperty('--animate-duration', '1.5s');


document.getElementById("recipe-add-button").onclick = function() {addRecipeAnimation()};

function addRecipeAnimation() {
  document.getElementById("recipe-add-button").classList.toggle("animate__bounceOut");
}

// Animate.style animation handling ends here

document.querySelectorAll('.recipe-card').forEach(div => {
    div.addEventListener('click', function() {
      this.classList.add('animate__backOutRight');
    })
  });
