
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order

@login_required
def checkout(request):
    items=Cart.objects.filter(user=request.user)
    total=sum(i.book.price*i.quantity for i in items)

    if request.method=="POST":
        Order.objects.create(user=request.user,total_price=total)
        items.delete()
        return render(request,'order_success.html',{'total':total})

    return render(request,'checkout.html',{'items':items,'total':total})
