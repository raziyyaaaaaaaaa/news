from django .urls import path
from . import views
urlpatterns = [
    path('',views.finicial_summary,name='finicial_summary')
    
]