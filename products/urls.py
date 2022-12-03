from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.products_list,name='products_list'),
    path('create/',views.products_create,name='products_create'),
    path('<int:id>/update/',views.products_update,name='products_update'),
    path('<int:id>/details/',views.products_detail,name='products_details'),
    path('<int:id>/delete/',views.products_delete,name='products_delete'),
]