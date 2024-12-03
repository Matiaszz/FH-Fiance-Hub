from django.views.generic import DetailView
from django.shortcuts import render
from .forms import UploadCSV
from django.http import JsonResponse
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
        total = request.session.get('total', 0)
        chart_path = 'static/analytics/input_chart.png'

        context = {
            'chart_exists': os.path.exists(chart_path),
            'upload_csv': UploadCSV(),
            'page_title': 'Dashboard',
            'total': total,
        }
        return render(request, 'finance/dashboard.html', context)


class ReceiveCsvView(View):
    def post(self, request):
        csv_file = request.FILES.get('file')
        if not csv_file:
            return JsonResponse(
                {'error': 'Nenhum arquivo foi enviado'}, status=400)

        try:
            df = pd.read_csv(csv_file)

            totals = df.iloc[0].to_dict()
            totals = {k: v for k, v in totals.items()
                      if pd.api.types.is_number(v)}

            total = sum(totals.values())

            request.session['total'] = total

            data = {
                'Category': list(totals.keys()),
                'Values': list(totals.values())
            }

            df_inputs = pd.DataFrame(data)

            plt.figure(figsize=(10, 8))
            df_inputs.plot(kind='bar', x='Category', y='Values',
                           legend=False, color='green')

            plt.title('Entrada de renda')
            plt.xlabel('Categoria')
            plt.ylabel('Valores (R$)')

            chart_path = 'static/analytics/input_chart.png'
            os.makedirs(os.path.dirname(chart_path), exist_ok=True)
            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()

            return JsonResponse(
                {'message': 'Gráfico atualizado com sucesso', 'total': total},
                status=200)

        except Exception as e:
            return JsonResponse(
                {'error': f'Ocorreu um erro ao processar o arquivo: {str(e)}'},
                status=500)
