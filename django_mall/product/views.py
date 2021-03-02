from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

class ProductList(ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_list = 'product_list'

class ProductCreate(FormView):
    template_name = 'product/register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context