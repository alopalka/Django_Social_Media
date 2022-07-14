from django.urls import path
from user import views

app_name="user"

urlpatterns=[
    path('<str:username>',views.profile_details,name="profiledetails"),
]