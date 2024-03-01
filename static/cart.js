document.addEventListener("DOMContentLoaded", function () {
  let iconCart = document.querySelector(".cart");
  let closeCart = document.querySelector(".close");
  let body = document.querySelector("body");
  let mobileCartContainer = document.getElementById("mobile_cart_container"); // Select the mobile cart container


  // Toggle cart menu when clicking either cart icon or mobile cart icon span
  function toggleCartMenu() {
    body.classList.toggle("showCart");
    console.log("Cart clicked");
  }

  iconCart.addEventListener("click", toggleCartMenu);

  // Attach event listener to the mobile cart container
  mobileCartContainer.addEventListener("click", toggleCartMenu);

  closeCart.addEventListener("click", () => {
    body.classList.remove("showCart");
    console.log("Close cart clicked");
  });
});
