
from django.shortcuts import render
from .models import Book
from django.db.models import Q

def home(request):
    q=request.GET.get('q')
    books=Book.objects.all()
    if q:
        books=books.filter(Q(title__icontains=q)|Q(author__icontains=q))
    return render(request,'home.html',{'books':books})
