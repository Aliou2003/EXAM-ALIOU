
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Joke
from .forms import UserRegisterForm, JokeForm
from django.contrib.auth import login

class JokeListView(ListView):
    model = Joke
    template_name = 'jokes/list_jokes.html'
    context_object_name = 'jokes'

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    template_name = 'jokes/create_joke.html'
    success_url = reverse_lazy('jokes:list-jokes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDetailView(DetailView):
    model = Joke
    template_name = 'jokes/detail_joke.html'

class JokeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    template_name = 'jokes/create_joke.html'
    success_url = reverse_lazy('jokes:list-jokes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        joke = self.get_object()
        return self.request.user == joke.user

class JokeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Joke
    template_name = 'jokes/delete_joke.html'
    success_url = reverse_lazy('jokes:list-jokes')

    def test_func(self):
        joke = self.get_object()
        return self.request.user == joke.user

class SignupView(CreateView):
    template_name = 'jokes/signup.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

