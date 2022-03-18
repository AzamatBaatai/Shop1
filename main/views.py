from django.shortcuts import render

# Create your views here.
from .models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})





#ToDo: sdelat spisok produktov
#ToDo: avtorizatsiya
#ToDo: filtratsiya, poisk, paginatsiya
#ToDo: korzina
#ToDo: zakazy
#ToDo: otpravka pisem
#ToDo: deploy
#ToDo: vertska