from django.urls import path

from .views import (PredictNumberCreateView, PredictNumberListView, PredictNumberDetailView,
                    PredictNumberUpdateView, PredictNumberDeleteView)

app_name = "mnist_predict"
urlpatterns = [
    path("", view=PredictNumberListView.as_view(), name="list"),
    path("create/", view=PredictNumberCreateView.as_view(), name="create"),
    path("<int:pk>/", view=PredictNumberDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", view=PredictNumberUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", view=PredictNumberDeleteView.as_view(), name="delete"),
]
