from django import forms
from pybo.models import Question, Answer


# forms.ModelForm)을 상속했다
class QuestionForm(forms.ModelForm):
    #모델폼을 사용하기 위해서는 반드시 inner class로 Meta가 사용되어야함
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
