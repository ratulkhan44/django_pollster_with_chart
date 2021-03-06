from django.urls import path, include
from .views import index, detail, results, vote, results_data

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>', detail, name='detail'),
    path('<int:question_id>/results', results, name='results'),
    path('<int:question_id>/vote', vote, name='vote'),
    path('<int:question_id>/resultdata', results_data, name='results_data'),
]
