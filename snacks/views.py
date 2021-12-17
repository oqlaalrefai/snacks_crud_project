from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import (
                    ListView,
                    DetailView,
                    CreateView,
                    UpdateView,
                    DeleteView
)
from django.urls import reverse_lazy
from .models import Snack
# Create your views here.

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks_list"


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ['title','purchaser','description']


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = "snack"


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ['title', 'description']
    context_object_name = "snack"


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    context_object_name = "snack"
    success_url = reverse_lazy("snack_list")