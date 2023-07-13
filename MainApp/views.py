from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def home(request):
    context = {
        "name": 'Оцелюк Владислав Валерьевич',
        "email": 'mail@mail.ru'
        }
    return render(request, "index.html", context)


def about(request):
    author = {
    "name": "Владислав",
    "middle": "Валерьевич",
    "surname": "Оцелюк",
    "phone": "8-800-555-55-55",
    "email": "mail@mail.ru"
    }
    context = {
        "author" : author
        }
    return render(request, "about.html", context)


def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id={id} not found')
    context = {
            'item' : item}
    return render(request, 'item-page.html', context)
    

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
        }
    return render(request, "items-list.html", context)