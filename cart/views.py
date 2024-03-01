from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods()
	return render(request, "cart_summary.html", {"cart_products": cart_products})




def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        del cart.cart[str(product_id)]
        request.session.modified = True
        return JsonResponse({'message': 'Item removed from cart.'})


def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        cart.cart[str(product_id)]['quantity'] = quantity
        request.session.modified = True
        return JsonResponse({'message': 'Cart updated.'})


