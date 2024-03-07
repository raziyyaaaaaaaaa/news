from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ExpenseForm
from .models import Expense
from django.views.generic.detail import DetailView

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html',{'expenses': expenses})

# Create your views here.

class ExpensesCreateView(CreateView):
    model =Expense
    template_name = 'expenses_create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses_list')

class ExpensesDetailView(DetailView):
    model = Expense
    context_object_name='expense'
    template_name = 'expenses_detail.html'