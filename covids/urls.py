from django.urls    import path
from .views import CovidApiView


urlpatterns = [
    path('', CovidApiView.as_view()),
]
