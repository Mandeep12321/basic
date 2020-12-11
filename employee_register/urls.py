from django.urls import path
from .views import *


urlpatterns = [
    path('', RegistrationView, name='employee_insert'),
    path('list/',employee_list , name='employee_list'),
    path('delete/<int:id>',employee_delete, name ="employee_delete"),
    path('<int:id>/',employee_update,name='employee_update'),
    path('remove/<int:id>/', remove,name='remove'),

]