document.addEventListener("DOMContentLoaded", function () {
  let iconCart = document.querySelector(".cart");
  let closeCart = document.querySelector(".close");
  let body = document.querySelector("body");
  let listProductHTML = document.querySelector(".listProduct");
  let listCartHTML = document.querySelector(".listCart");
  let iconCartSpan = document.querySelector(".icon-cart-span");
  let mobileCartIconSpan = document.getElementById("icon-span-mobile");
  let mobileCartContainer = document.getElementById("mobile_cart_container"); // Select the mobile cart container

  let listProducts = [];
  let carts = [];

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

  const addDataToHTML = () => {
    // Select all elements with the class 'listProduct'
    let listProductContainers = document.querySelectorAll(".listProduct");

    // Iterate over each listProduct container
    listProductContainers.forEach((listProductHTML) => {
      listProductHTML.innerHTML = "";
      let start = parseInt(listProductHTML.dataset.start);
      let end = parseInt(listProductHTML.dataset.end);
      let productsInRange = listProducts.slice(start - 1, end); // Extract products within the range
      // Check if there are products in the range
      if (productsInRange.length > 0) {
        productsInRange.forEach((product) => {
          let newProduct = document.createElement("div");
          newProduct.classList.add("item");
          newProduct.dataset.id = product.id;
          let price = product.offered
            ? (product.price * (100 - product.discountPercentage)) / 100
            : product.price;
          let oldPrice = product.price;
          let priceDisplay = product.offered
            ? `<span class="old-price">${oldPrice.toLocaleString(
                "fa-IR"
              )} تومان</span> <span class="new-price">${price.toLocaleString(
                "fa-IR"
              )} تومان</span>`
            : `<span>${price.toLocaleString("fa-IR")} تومان</span>`;
            let offerText = product.offered ? `${product.discountPercentage}%` : ''; // Offer text if applicable
          newProduct.innerHTML = `
                        <img src="${product.image}" alt=""/>
                        <div class="des">
                            <h5>${product.name} <span class="offer">${offerText}</span> </h5> 
                            <h4 class="price-h4">${priceDisplay}</h4>
                        </div>
                        <button class="addCart">
                            <span class="material-symbols-outlined cart">
                                shopping_cart
                            </span>
                        </button>
                    `;
          newProduct.querySelector("img").addEventListener("click", () => {
            window.location.href = "productpage.html";
          });
          newProduct.querySelector("h5").addEventListener("click", () => {
            window.location.href = "productpage.html";
          });
          newProduct
            .querySelector(".addCart")
            .addEventListener("click", (event) => {
              event.stopPropagation();
              let product_id = newProduct.dataset.id;
              addToCart(product_id);
            });
          listProductHTML.appendChild(newProduct);
        });
      } else {
        console.log("No products found");
      }
    });
  };

  listProductHTML.addEventListener("click", (event) => {
    let positionclick = event.target;
    if (
      positionclick.classList.contains("addCart") ||
      positionclick.closest(".addCart")
    ) {
      let product_id = positionclick.parentElement.dataset.id;
      addToCart(product_id);
    }
  });

  const addToCart = (product_id) => {
    let positionThisProductInCart = carts.findIndex(
      (value) => value.product_id == product_id
    );
    let product = listProducts.find((p) => p.id == product_id);
    let price = product.offered
      ? (product.price * (100 - product.discountPercentage)) / 100
      : product.price;
    console.log("Product:", product);
    console.log("Price:", price);
    if (carts.length <= 0) {
      carts = [
        {
          product_id: product_id,
          quantity: 1,
          price: price // Store the discounted price in the cart
        },
      ];
    } else if (positionThisProductInCart < 0) {
      carts.push({
        product_id: product_id,
        quantity: 1,
        price: price // Store the discounted price in the cart
      });
    } else {
      carts[positionThisProductInCart].quantity =
        carts[positionThisProductInCart].quantity + 1;
    }
    addCartToHTML();
    addCartToMemory();
  };

  const addCartToMemory = () => {
    localStorage.setItem("carts", JSON.stringify(carts));
  };

  const addCartToHTML = () => {
    listCartHTML.innerHTML = "";
    let totalQuantity = 0;
    let totalAllPrice = 0; // Initialize total price variable
    if (carts.length > 0) {
      carts.forEach((cart) => {
        totalQuantity += cart.quantity;
        let newCart = document.createElement("div");
        newCart.classList.add("item");
        newCart.dataset.id = cart.product_id;
        let product = listProducts.find((p) => p.id == cart.product_id);
        if (product) {
          let totalPrice = cart.price * cart.quantity;
          totalAllPrice += totalPrice; // Accumulate total price
          newCart.innerHTML = `
                        <div class="image">
                            <img src="${product.image}" alt=""/>
                        </div>
                        <div class="name">
                            ${product.name}
                        </div>
                        <div class="totalPrice">
                            ${totalPrice.toLocaleString("fa-IR")} تومان
                        </div>
                        <div class="quantity">
                            <span class="minus">-</span>
                            <span>${cart.quantity}</span>
                            <span class="plus">+</span>
                        </div>
                    `;
          listCartHTML.appendChild(newCart);
        } else {
          console.log("Product not found for cart:", cart);
        }
      });
    }
    iconCartSpan.innerText = totalQuantity;
    mobileCartIconSpan.innerText = totalQuantity;

    // Update the total price in the cart
    let totalAllPriceElement = document.querySelector(".total-all-price");
    if (totalAllPriceElement) {
      totalAllPriceElement.innerHTML = `<strong>مجموع: </strong>  ${totalAllPrice.toLocaleString(
        "fa-IR"
      )} تومان`;
    } else {
      totalAllPriceElement = document.createElement("div");
      totalAllPriceElement.classList.add("total-all-price");
      totalAllPriceElement.innerHTML = `<strong>مجموع:</strong>  ${totalAllPrice.toLocaleString(
        "fa-IR"
      )} تومان`;
      // Select the cartTab div and append the total-all-price element to it
      let cartTab = document.querySelector(".cartTab");
      cartTab.appendChild(totalAllPriceElement);
    }
};


  listCartHTML.addEventListener("click", (event) => {
    let positionClick = event.target;
    if (
      positionClick.classList.contains("minus") ||
      positionClick.classList.contains("plus")
    ) {
      let product_id = positionClick.parentElement.parentElement.dataset.id;
      let type = positionClick.classList.contains("plus") ? "plus" : "minus";
      changeQuantity(product_id, type);
    }
  });

  const changeQuantity = (product_id, type) => {
    let positionItemInCart = carts.findIndex(
      (value) => value.product_id == product_id
    );
    if (positionItemInCart >= 0) {
      switch (type) {
        case "plus":
          carts[positionItemInCart].quantity =
            carts[positionItemInCart].quantity + 1;
          break;
        default:
          let valueChange = carts[positionItemInCart].quantity - 1;
          if (valueChange > 0) {
            carts[positionItemInCart].quantity = valueChange;
          } else {
            carts.splice(positionItemInCart, 1);
          }
      }
    }
    addCartToMemory();
    addCartToHTML();
  };

  const initApp = () => {
    console.log("Initializing app");
    fetch("products.json")
      .then((response) => response.json())
      .then((data) => {
        listProducts = data;
        console.log("Fetched products:", listProducts);
        addDataToHTML();
        if (localStorage.getItem("carts")) {
          carts = JSON.parse(localStorage.getItem("carts"));
          addCartToHTML();
        }
      })
      .catch((error) => {
        console.error("Error fetching products:", error);
      });
  };

  initApp();
});
