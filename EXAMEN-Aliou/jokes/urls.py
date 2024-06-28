
from django.urls import path
from .views import JokeListView, JokeCreateView, JokeDetailView, JokeUpdateView, JokeDeleteView, SignupView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('joke/', JokeListView.as_view(), name='list-jokes'),
    path('joke/new/', JokeCreateView.as_view(), name='create-joke'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail-joke'),
    path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update-joke'),
    path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='delete-joke'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='jokes/login.html'), name='login'),
]
