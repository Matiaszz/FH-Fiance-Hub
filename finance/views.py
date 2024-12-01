import os
from django.views import View
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from django.views.generic import DetailView


class HomeView(DetailView):
    template_name = 'finance/home.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class ChartView(View):
    def get(self, request):

        data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [10, 20, 15, 30]
        }

        df = pd.DataFrame(data)

        plt.figure(figsize=(8, 5))
        df.plot(kind='bar', x='Category', y='Values', legend=False)
        plt.title('Sample Bar Chart')
        plt.xlabel('Category')
        plt.ylabel('Values')

        chart_path = 'analytics/static/analytics/chart.png'
        os.makedirs(os.path.dirname(chart_path), exist_ok=True)
        plt.savefig(chart_path)
        plt.close()

        return render(request, 'finance/dashboard.html')
