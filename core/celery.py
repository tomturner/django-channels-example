import django
from celery import Celery
from django.conf import settings

django.setup()
app = Celery('core', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

CELERY_ACCEPT_CONTENT = ['json']


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
