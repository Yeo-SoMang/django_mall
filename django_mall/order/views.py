from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Order

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

class OrderList(ListView):
    template_name = 'order/order.html'
    context_object_name = 'order_list'

    ## quetyset으로 사용자를 지정하기 힘드므로 함수로 만듬.
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset