from django.db import models

from django.contrib.auth.models import User  # 장고에서 제공하는 유저모델.

class Writing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  # 유저모델과 연결!
    subject = models.CharField(max_length=30)  # 제목에 해당하는 필드 작성.
    content = models.TextField()  # 내용에 해당하는 필드 작성.

    create_date = models.DateTimeField(auto_now_add=True)  # 글이 만들어지면 자동 작성.
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정할 때마다 갱신.(뷰에서 제어)

    def __str__(self):
        return self.subject  # 관리자페이지에서 어떻게 보여질 것인가.
