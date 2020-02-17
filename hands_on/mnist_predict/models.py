from django.db import models


class PredictNumber(models.Model):

    image_file = models.ImageField(upload_to='images/')
    predict_result = models.SmallIntegerField(blank=True, default=-1)
    actual_result = models.SmallIntegerField(blank=True, default=-1)


