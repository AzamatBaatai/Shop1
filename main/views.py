from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

class ProductsListView(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        return render(request, 'main/products_list.html', {'products': products})

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'main/product_details.html'

# class ProductsListView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'main/products_list.html'


#ToDO: sdelat perehody mejdu stranitsami
#ToDo: sdelat spisok produktov
#ToDo: avtorizatsiya
#ToDo: filtratsiya, poisk, paginatsiya
#ToDo: korzina
#ToDo: zakazy
#ToDo: otpravka pisem
#ToDo: deploy
#ToDo: vertska