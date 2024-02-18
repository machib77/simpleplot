from django.urls import path
from .views import HomePageView, ChartGeneratorView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("generate_chart/", ChartGeneratorView.as_view(), name="generate_chart"),
]
