from django.urls import path
from .views import Unsubscribe_user,resubscribe

urlpatterns = [
    path('unsubscribe/',Unsubscribe_user,name="unsubscribe"),
     path('re-subscribe/',resubscribe,name="re-subscribe"),
]
