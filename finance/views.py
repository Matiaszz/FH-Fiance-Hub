from django.shortcuts import render
from django.views.generic import DetailView


class HomeView(DetailView):
    template_name = 'finance/home.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
