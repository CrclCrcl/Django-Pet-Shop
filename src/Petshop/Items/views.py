
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'item_detail.html', {'item': item})