from django.urls import path
from . import views
urlpatterns=[
    path('cartdet',views.cartdet,name='cartdet'),
    path('add/<int:prdct_id>/',views.cart_add,name='addcart'),
    path('dec/<int:prdct_id>/',views.cart_min,name='deccart'),
    path('remove/<int:prdct_id>/',views.cart_remove,name='removecart')
]
