from django.shortcuts import render
from .models import Orders


def index(request):
    orders_all = Orders.objects.order_by('id')
    return render(request, 'myapp/index.html', {'title': 'Главная страница сайта',
                                               'tasks': orders_all})
