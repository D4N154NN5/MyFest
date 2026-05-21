from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("<int:pk>/", views.event_detail, name="event_detail"),
    path("shift/<int:pk>/signup/", views.shift_signup, name="shift_signup"),
    path("shift/<int:pk>/cancel/", views.shift_cancel, name="shift_cancel"),
]
