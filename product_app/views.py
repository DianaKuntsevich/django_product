from django.shortcuts import render

from .models import Notebook


def notebook_list(request):
    data = Notebook.objects.all()
    context = {
        'data': data,
        'title': 'Ноутбуки'
    }
    return render(request, 'product_app/notebook_list.html', context=context)


def notebook_detail(request, pk):
    data = Notebook.objects.get(pk=pk)
    return render(request, 'product_app/notebook_detail.html', {'data': data})

