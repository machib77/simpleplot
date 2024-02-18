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
        number1 = float(request.POST.get("number1", 0))
        number2 = float(request.POST.get("number2", 0))
        number3 = float(request.POST.get("number3", 0))

        # Generate Plotly chart
        data = [
            go.Scatter(
                x=["Number 1", "Number 2", "Number 3"],
                y=[number1, number2, number3],
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
