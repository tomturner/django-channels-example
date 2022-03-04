from django.urls import path


from .views import MainView, ControlView

urlpatterns = [
    path('', MainView.as_view(), name='helper_index'),
    path('control/', ControlView.as_view(), name='control_index'),
]
