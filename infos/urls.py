from django.urls import path
from infos.views import sg, me, contact

urlpatterns = [
    path('', sg),
    path('me', me),
    path('contact', contact),
]