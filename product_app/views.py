from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Notebook


def notebook_list(request):
    data = Notebook.objects.all().prefetch_related('images')

    paginator = Paginator(data, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'data': data,
        'title': 'Ноутбуки'
    }
    return render(request, 'product_app/notebook_list.html', context=context)


def notebook_detail(request, pk):
    data = Notebook.objects.prefetch_related('images').get(pk=pk)
    return render(request, 'product_app/notebook_detail.html', {'data': data})

