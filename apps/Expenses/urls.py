from django .urls import path
from . import views
urlpatterns = [
    path('expenses/', views.expenses_list, name="expenses_list"),
    path('expenses/add/',views.ExpensesCreateView.as_view(),
    name="create_expenses"),
    path('expenses/<int:pk>/',views.ExpensesDetailView.as_view(),
    name = 'expenses_detail'),

    
]