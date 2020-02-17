from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django_celery_results.models import TaskResult

from .models import PredictNumber
from hands_on.mnist_predict.tasks import predict_number_task


logger = getLogger(__name__)


class PredictNumberListView(ListView):
    model = PredictNumber


class PredictNumberDetailView(DetailView):
    model = PredictNumber

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info(TaskResult.objects.all())
        return context


class PredictNumberCreateView(CreateView):
    model = PredictNumber
    fields = ('image_file', 'actual_result')
    task_id = None

    def form_valid(self, form):
        self.object = form.save()
        task = predict_number_task.delay(self.object.id, current_scheme_host=self.request._current_scheme_host)
        self.task_id = task.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.task_id:
            context['task_id'] = self.task_id
        return context
    
    def get_success_url(self):
        return reverse('mnist_predict:detail', kwargs={'pk': self.object.id})


class PredictNumberUpdateView(UpdateView):
    model = PredictNumber
    fields = ('image_file', 'actual_result')
    task_id = None

    def form_valid(self, form):
        self.object = form.save()
        task = predict_number_task.delay(self.object.id, current_scheme_host=self.request._current_scheme_host)
        self.task_id = task.id
        logger.info(TaskResult.objects.get_task(self.task_id))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.task_id:
            context['task_id'] = self.task_id
        return context
    
    def get_success_url(self):
        return reverse('mnist_predict:detail', kwargs={'pk': self.object.id})


class PredictNumberDeleteView(DeleteView):
    model = PredictNumber
    success_url = reverse_lazy('mnist_predict:list')