from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='pro_cat'),
    path('<slug:c_slug>/<slug:pro_slug>',views.details,name='details'),
    path('search',views.search,name='search'),
]