from django.views.generic import DetailView
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.views import View
import os
import matplotlib
matplotlib.use('Agg')


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

        chart_path = 'static/analytics/chart.png'
        os.makedirs(os.path.dirname(chart_path), exist_ok=True)
        plt.savefig(chart_path)
        plt.close()

        return render(request, 'finance/dashboard.html')
