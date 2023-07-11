from django.urls import path
from .views import EmployeeView, get_v, Partial_v, Update_v

urlpatterns = [

    path('a/', EmployeeView.as_view(), name='APICLASS_URL'),
    path('b/<int:pk>/', get_v, name='APIFUNCTION_URL'),
    path('c/<int:pk>/', Partial_v.as_view({'patch':'partial_update','delete':'destroy'})),
    path('d/<int:pk>/', Update_v.as_view())
]