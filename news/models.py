from django.db import models
from django.utils import timezone

# Create your models here.

class InputModelForm(models.Model):
    name = models.CharField(
        '名前',
        max_length=50
    )
    age = models.IntegerField(
        '年齢',
        default=0
    )
    mail = models.EmailField(
        'メールアドレス',
        max_length=255
    )
    title = models.CharField(
        'タイトル',
        max_length=255
    )
    history = models.CharField(
        '背景',
        max_length=255
    )
    done = models.CharField(
        '実績',
        max_length=255
    )
    question = models.CharField(
        '問いかけ',
        max_length=255
    )
    idea = models.CharField(
        '考え',
        max_length=255
    )
    reference = models.CharField(
        '参考文献',
        max_length=255
    )
    created_at = models.DateField(
        '作成日',
        default=timezone.now
    )