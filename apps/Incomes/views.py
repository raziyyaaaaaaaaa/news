from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import IncomeForm
from .models import Income

def incomes_list(request):
    incomes = Income.objects.all()
    return render(request,'incomes_list.html',{'incomes':incomes})

class IncomeCreateView(CreateView):
    model =Income
    template_name = 'create_income.html'
    form_class = IncomeForm
    success_url = reverse_lazy('incomes_list')

class IncomeDetailView(DetailView):
    model = Income
    context_object_name='income'
    template_name = 'income_detail.html'




# Create your views here.