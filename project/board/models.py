from django.db import models

from django.contrib.auth.models import User  # 장고에서 제공하는 유저모델.

class Writing(models.Model):
    
    TECHNICAL_CHOICES = {
       ('웹', '웹'),
       ('앱', '앱'), 
       ('게임', '게임'), 
       ('인공지능', '인공지능'), 
       ('기타', '기타')
    }
    
    TOPIC_CHOICES = {
       ('생활', '생활'),
       ('업무', '업무'), 
       ('공공/교통', '공공/교통'), 
       ('금융/핀테크', '금융/핀테크'), 
       ('의료', '의료'),
       ('교육', '교육'),
       ('유통/쇼핑', '유통/쇼핑'),
       ('엔터테인먼트', '엔터테인먼트'), 
    }
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  # 유저모델과 연결!
    
    title = models.CharField(max_length=200, default = '') #프로젝트 개요
    email = models.CharField(max_length=30, default = '') #연락처
    #프로젝트 기간
    technical_field = models.CharField(max_length=80, choices=TECHNICAL_CHOICES, default = '') #기술분야
    topic_area = models.CharField(max_length=80, choices=TOPIC_CHOICES, default = '')#주제영역
    content = models.TextField('프로젝트 개요서 첨부')  # 프로젝트 개요서 첨부
    #상태
    team = models.CharField(max_length=30, default = '')#모집인원

    create_date = models.DateTimeField(auto_now_add=True)  # 글이 만들어지면 자동 작성.
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정할 때마다 갱신.(뷰에서 제어)

    
    
    def __str__(self):
        return self.title  # 관리자페이지에서 어떻게 보여질 것인가.
