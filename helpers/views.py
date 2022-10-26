from datetime import datetime

from ajax_helpers.mixins import AjaxHelpers
from ajax_helpers.utils import toast_commands
from ajax_helpers.websockets.mixin import WebsocketHelpers
from django.views.generic import TemplateView

from helpers.tasks import channel_example


class MainView(WebsocketHelpers, AjaxHelpers, TemplateView):
    template_name = 'helpers/index.html'

    def get_context_data(self, **kwargs):
        self.add_channel('main')
        context = super().get_context_data(**kwargs) if hasattr(super(), 'get_context_data') else {}
        return context


class ControlView(WebsocketHelpers, AjaxHelpers, TemplateView):
    template_name = 'helpers/control.html'

    def button_test_websocket(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        self.send_ws_commands('main', 'html', selector='#control_div', html=f'Message from websocket {date_time}')
        return self.command_response()

    def button_test_websocket2(self):
        self.send_ws_commands('main', 'message', text='Hello world')
        return self.command_response()

    def button_test_toast(self):
        self.send_ws_commands('main', toast_commands(header='Information',
                                                     text=f'toast message',
                                                     position='bottom-right'))
        return self.command_response()

    def button_test_celery(self):
        channel_example.delay()
        return self.command_response()
