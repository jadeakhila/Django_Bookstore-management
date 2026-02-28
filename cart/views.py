
from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from store.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    items=Cart.objects.filter(user=request.user)
    total=sum(i.book.price*i.quantity for i in items)
    return render(request,'cart.html',{'cart_items':items,'total':total})

@login_required
def add_to_cart(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    item,created=Cart.objects.get_or_create(user=request.user,book=book)
    if not created:
        item.quantity+=1
        item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request,cart_id):
    Cart.objects.filter(id=cart_id).delete()
    return redirect('cart')
