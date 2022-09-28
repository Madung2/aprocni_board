from ipaddress import ip_address
from tabnanny import verbose
from django.db import models

# Create your models here.
class article_A(models.Model):
    title=models.CharField("제목", max_length=20)
    password=models.CharField("비밀번호",max_length=128)
    content=models.CharField("내용", max_length=300)
    ip_address=models.GenericIPAddressField(protocol='IPv4')
    created_at=models.DateTimeField("생성 날짜", auto_now_add=True)
    updated_at=models.DateTimeField("수정 날짜", auto_now=True)
    board_A_id=models.PositiveSmallIntegerField("게시글 번호(홀수)")

class article_B(models.Model):
    title=models.CharField("제목", max_length=20)
    password=models.CharField("비밀번호",max_length=128)
    content=models.CharField("내용", max_length=300)
    ip_address=models.GenericIPAddressField(protocol='IPv4')
    created_at=models.DateTimeField("생성 날짜", auto_now_add=True)
    updated_at=models.DateTimeField("수정 날짜", auto_now=True)
    board_B_id=models.PositiveSmallIntegerField("게시글 번호(짝수)")

class comment_A(models.Model):
    article= models.ForeignKey("article_A", verbose_name="원글", on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField(protocol='IPv4')

class comment_B(models.Model):
    article= models.ForeignKey("article_B", verbose_name="원글", on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField(protocol='IPv4')

class like_A(models.Model):
    article= models.ForeignKey("article_A", verbose_name="원글", on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField(protocol='IPv4')

class like_B(models.Model):
    article= models.ForeignKey("article_B", verbose_name="원글", on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField(protocol='IPv4')


