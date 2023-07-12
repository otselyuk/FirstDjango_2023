from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


author = {
    "name": "Владислав",
    "middle": "Валерьевич",
    "surname": "Оцелюк",
    "phone": "8-800-555-55-55",
    "email": "mail@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



# Create your views here.
def home(request):
    context = {
        "name": 'Оцелюк Владислав Валерьевич',
        "email": 'mail@mail.ru'
    }
    return render(request, "index.html", context)


def about(request):
    result = f"""
    Имя: <b>{author['name']}</b><br>
    Отчество: <b>{author['middle']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    Телефон: <b>{author['phone']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)

#url /item/1
#url /item/2

def get_item(request, id):
    for item in items:
        if item['id'] == id:
        #     result = f"""
        #     <h2>Имя:{item["name"]} </h2>
        #     <p>Колличество: {item["quantity"]} </p>
        #     <a href='/items'> Назад </a>
        #     """
        #     return HttpResponse(result)
            context = {
            'item' : item
            }
            return render(request, 'item-page.html', context)
    return HttpResponseNotFound(f'Item with {id} = id not foud')

def items_list(request):
    # result = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '<ol>'
    # return HttpResponse(result)
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)