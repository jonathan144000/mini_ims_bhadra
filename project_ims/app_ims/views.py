from django.shortcuts import render
from .forms import ItemCreateForm
from .models import Category, Item, AppUser
from datetime import datetime
# Create your views here.
def item_index(request):
    return render(request, 'items/index.html')

def item_create(request):
    item_create_form = ItemCreateForm()
    context = {"form": item_create_form}
    if request.method == "post":
        # context.update({"msg":"POST Method Success"})
        item = Item()
        category = Category.objects.get(id=request.POST.get('category'))
        item.title = request.POST.get('title')
        item.particular = request.POST.get('particular')
        item.ledger_folio = request.POST.get('ledger_folio')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.category_id = category
        item.total = item.price*item.quantity
        item.entry_date = datetime.now()
        item.save()
        # item = Item(title=title, category_id=category) - parameterized constructor

        return render(request, 'items/create.html', context)
    return render(request, 'items/create.html', context)

def item_edit(request):
    return render(request, 'items/edit.html')

def item_show(request):
    return render(request, 'items/show.html')