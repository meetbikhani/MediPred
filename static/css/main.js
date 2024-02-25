// Header Scroll
let nav = document.querySelector(".navbar");
window.addEventListener("scroll", function() {
    if (document.documentElement.scrollTop > 100) {
        nav.classList.add("header-scrolled");
    } else {
        nav.classList.remove("header-scrolled");
    }
});

// Nav hide
let navBar = document.querySelectorAll(".nav-link");
let navCollapse = document.querySelector(".navbar-collapse.collapse");
navBar.forEach(function(a) {
    a.addEventListener("click", function() {
        navCollapse.classList.remove("show");
    });
});

// Typing Text Animation
const line1 = "Predicting Health,";
const line2 = "Defining Futures";
const typingLine1Element = document.getElementById('typing-line1');
const typingLine2Element = document.getElementById('typing-line2');
let index1 = 0;
let index2 = 0;

function typeLine1() {
    if (index1 < line1.length) {
        typingLine1Element.textContent += line1.charAt(index1);
        index1++;
        setTimeout(typeLine1, 100); // Delay between each letter (in milliseconds)
    }
}

function typeLine2() {
    if (index2 < line2.length) {
        typingLine2Element.textContent += line2.charAt(index2);
        index2++;
        setTimeout(typeLine2, 100); // Delay between each letter (in milliseconds)
    }
}

window.onload = function() {
    typeLine1();
    setTimeout(typeLine2, line1.length * 100 + 500); // Delay before starting the second line
};


// detect-disease
$('#recipeCarousel').carousel({
    interval: 10000
  })
  
  $('.carousel .carousel-item').each(function(){
      var minPerSlide = 3;
      var next = $(this).next();
      if (!next.length) {
      next = $(this).siblings(':first');
      }
      next.children(':first-child').clone().appendTo($(this));
      
      for (var i=0;i<minPerSlide;i++) {
          next=next.next();
          if (!next.length) {
              next = $(this).siblings(':first');
            }
          
          next.children(':first-child').clone().appendTo($(this));
        }
  });