from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.views import View

# import plotly.graph_objs as go
import plotly.graph_objs as go
import json

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ChartGeneratorView(View):
    def post(self, request):
        # Retrieve data from POST request

        rate_dict = {
            "1Y": float(request.POST.get("1Y", 0)),
            "2Y": float(request.POST.get("2Y", 0)),
            "3Y": float(request.POST.get("3Y", 0)),
            "4Y": float(request.POST.get("4Y", 0)),
            "5Y": float(request.POST.get("5Y", 0)),
            "6Y": float(request.POST.get("6Y", 0)),
            "7Y": float(request.POST.get("7Y", 0)),
            "8Y": float(request.POST.get("8Y", 0)),
            "9Y": float(request.POST.get("9Y", 0)),
            "10Y": float(request.POST.get("10Y", 0)),
        }

        # Generate Plotly chart
        data = [
            go.Scatter(
                x=list(rate_dict.keys()),
                y=list(rate_dict.values()),
                mode="lines+markers",
            )
        ]
        layout = go.Layout(title="Numbers Chart")
        fig = go.Figure(data=data, layout=layout)

        chart = fig.to_html(full_html=False, include_plotlyjs=False)

        return HttpResponse(chart)

        # NOTE: This was my first attempt to return it
        # with JsonResponse but it didn't work:

        # Construct JSON response
        # response_data = {"chart": chart_json}

        # Serialize Plotly figure to JSON
        # chart_json = json.loads(fig.to_json())

        # return JsonResponse(response_data)
