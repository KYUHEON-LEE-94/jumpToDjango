from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    # 매핑주소, controller의 메서드, 별칭
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create')
]