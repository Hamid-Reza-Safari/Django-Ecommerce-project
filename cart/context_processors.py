from .cart import Cart

# Create context processor to include cart and cart products on all pages
def cart(request):
    # Get the cart instance
    cart = Cart(request)
    # Get cart products
    cart_products = cart.get_prods()
    # Return cart and cart products in the context
    return {'cart': cart, 'cart_products': cart_products}
