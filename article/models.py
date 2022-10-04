from email.policy import default
from ipaddress import ip_address
from tabnanny import verbose
from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    uid= models.CharField(max_length=1, unique=True, default=0)
    title=models.CharField("제목", max_length=20)
    password=models.CharField("비밀번호",max_length=128)
    content=models.CharField("내용", max_length=300)
    ip_address=models.GenericIPAddressField("사용자 IP주소", protocol='IPv4')
    created_at=models.DateTimeField("생성 날짜", auto_now_add=True)
    updated_at=models.DateTimeField("수정 날짜", auto_now=True)
    board=models.CharField("게시판", max_length=1, default='A')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_uid()  
    def set_uid(self):
        if not self.uid:
            if self.board=='A':
                uid=(self.id*2-1)
                article=Article.objects.get(id=self.id)
                article.uid=uid
                article.save()
            elif self.board=='B':
                uid=(self.id*2)
                article=Article.objects.get(id=self.id)
                article.uid=uid
                article.save()


class Comment(models.Model):
    article= models.ForeignKey("article", verbose_name="원글", on_delete=models.CASCADE)
    comment= models.CharField("내용", max_length=200, default='')
    ip_address=models.GenericIPAddressField("사용자 IP주소", protocol='IPv4')
    created_at=models.DateTimeField("생성 날짜", auto_now_add=True)
    updated_at=models.DateTimeField("수정 날짜", auto_now=True)

class Like(models.Model):
    article= models.ForeignKey("article", verbose_name="원글", on_delete=models.CASCADE)
    ip_address=models.GenericIPAddressField("사용자 IP주소", protocol='IPv4')

