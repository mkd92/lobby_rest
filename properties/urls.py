from django.urls import include, path

from properties.views import PropertyView

urlpatterns = [
    path('', PropertyView.as_view(), name='property')
]