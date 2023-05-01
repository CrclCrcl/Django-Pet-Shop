from django.shortcuts import render
from Items.models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(availability=True)[0:6]
    categories = Category.objects.all()
    return render(request,'index.html',{
        'categories': categories,
        'items' : items
    })
