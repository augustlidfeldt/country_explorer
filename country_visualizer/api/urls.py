from django.urls import path
from .views import GetFertility

urlpatterns = [
    path('get-fertitilty', GetFertility.as_view())
]
