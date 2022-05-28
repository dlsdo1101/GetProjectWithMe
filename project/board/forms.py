from django import forms
from matplotlib import widgets
from .models import Writing  # 폼을 적용할 모델을 불러온다.

class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing  # 사용할 모델
        fields = ['title', 'technical_field', 'topic_area', 'content', 'team', '최종학력', '신분']  # 폼으로 입력할 필드를 입력해준다.
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'signup-input midinput',
                    'placeholder' : '프로젝트 제목을 입력해주세요'
                }
            ),
            
            'content': forms.TextInput(
                attrs={
                    'class': 'signup-input'
                }
            ),
            'team': forms.TextInput(
                attrs={
                    'class': 'signup-input'
                }
            )
,
            '최종학력': forms.TextInput(
                attrs={
                    'class': 'signup-input',
                    'placeholder' : '예) 평택대 4학년 융합소프트웨어학과 재학중/휴학/졸업'
                }
            ),
            
            
        }
        # fields에 '__all__'을 따옴표까지 함께 넣어주면 모든 필드를 가져오라는 명령이 된다.