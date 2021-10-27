from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('returns/', views.returns, name='returns'),
    path('faq/', views.faq, name='faq'),
]
