from django_celery_results.models import TaskResult
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import TaskResultSerializer


class TaskResultViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = TaskResultSerializer
    queryset = TaskResult.objects.all()
