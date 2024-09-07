from django.urls import path
from . import views
urlpatterns = [
    path('prompt/', views.PromptRequestView.as_view(), name="prompt"),
    path('messages/<str:session_id>', views.MessagesView.as_view(), name="prompt"),
]