from datetime import datetime

from ajax_helpers.utils import ajax_command
from ajax_helpers.websockets.tasks import TaskHelper
from asgiref.sync import async_to_sync
from celery import Celery, Task, shared_task
from celery.utils.log import get_task_logger


from django.conf import settings

logger = get_task_logger(__name__)

app = Celery('core', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)


class ChannelExampleTask(TaskHelper):

    def process(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        self.send_ws_commands('main', 'html', selector='#celery_div', html=f'Message from celery websocket {date_time}')


@shared_task(bind=True, base=ChannelExampleTask)
def channel_example(self):
    self.process()


@app.task(bind=True)
def debug_task2(self):
    print('Request: {0!r}'.format(self.request))



