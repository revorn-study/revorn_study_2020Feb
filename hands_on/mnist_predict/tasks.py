import time
from django.contrib.staticfiles.storage import staticfiles_storage
import keras
from celery import shared_task

from .utils import load_image
from .models import PredictNumber


@shared_task
def predict_number(image_id, current_scheme_host=None):
    time.sleep(10)
    model_path = staticfiles_storage.path('model/mnist_cnn_sample.h5')
    model = keras.models.load_model(model_path, compile=False)

    predict_number_obj = PredictNumber.objects.get(id=image_id)

    test_img_array = load_image(predict_number_obj.image_file.url, current_scheme_host=current_scheme_host)
    print(test_img_array)
    test_data = test_img_array.reshape(1, 28, 28, 1)
    test_data = test_data.astype('float32')
    test_data /= 255
    predict_result = int(model.predict_classes(test_data)[0])
    predict_number_obj.predict_result = predict_result
    predict_number_obj.save()
    return {
        'predict_result': predict_result,
        'id': predict_number_obj.id
    }