document.addEventListener('DOMContentLoaded', function() {
    const bar = document.getElementById('bar');
    const nav = document.getElementById('navbar');

    if (bar && nav) {
        bar.addEventListener('click', function() {
            nav.classList.toggle('active');
            bar.classList.toggle('active'); // Add or remove active class on click
        });
    }

// Get the button:
var mybutton = document.getElementById("back-to-top-btn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document smoothly
mybutton.addEventListener("click", function() {
  // Scroll to the top of the document smoothly
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

});
document.addEventListener("DOMContentLoaded", function () {
  const searchIcon = document.querySelector(".search-icon");
  const searchOverlay = document.getElementById("search-overlay");
  const closeSearch = document.getElementById("close-search");

  searchIcon.addEventListener("click", function () {
    searchOverlay.style.display = "flex";
  });

  closeSearch.addEventListener("click", function () {
    searchOverlay.style.display = "none";
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const searchIcon = document.querySelector(".search-icon2");
  const searchOverlay = document.getElementById("search-overlay");
  const closeSearch = document.getElementById("close-search");

  searchIcon.addEventListener("click", function () {
    searchOverlay.style.display = "flex";
  });

  closeSearch.addEventListener("click", function () {
    searchOverlay.style.display = "none";
  });
});
