from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from django.urls import path
from django_celery_results.views import task_status
from hands_on.users.api.views import UserViewSet
from hands_on.mnist_predict.api.views import TaskResultViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
# router.register("tasks", TaskResultViewSet)


app_name = "api"
urlpatterns = [
    path('tasks/<str:task_id>/', task_status, name="task_status")
] + router.urls
