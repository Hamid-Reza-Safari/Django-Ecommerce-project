$(document).ready(function () {
  // Hide the .small-slider element by default
  $('.small-slider').hide();

  // Function to show/hide the .small-slider based on screen width
  function toggleSmallSlider() {
    if ($(window).width() <= 600) {
      $('.small-slider').show();
    } else {
      $('.small-slider').hide();
    }
  }

  // Call the function on document ready
  toggleSmallSlider();

  // Call the function whenever the window is resized
  $(window).resize(function() {
    toggleSmallSlider();
  });

  // Click event handler for items in the Owl Carousel
  $('.owl-carousel .item').click(function() {
    var link = $(this).data('href');
    if (link) {
      window.location.href = link;
    }
  });

  // Initialize Owl Carousel
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    rtl: true,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 1,
      },
    },
  });
});
