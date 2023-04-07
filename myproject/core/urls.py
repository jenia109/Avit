from django.urls import path, re_path
from .views import index1, index2

urlpatterns = [
    path('', index1),
    re_path('^$', index2)

]
