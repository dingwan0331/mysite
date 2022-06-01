from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail , name= 'detail'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),    detail 뷰의 url을 polls/specifics/~~/ 로 나오게 하고싶을때
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')
]