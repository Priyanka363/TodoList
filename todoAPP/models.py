from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
  status_select=[
    ('C','COMPLETE'),
    ('P','PENDING')
  ]

  precedence_select=[
    ('1','1'),
    ('1','1'),
    ('3','3'),
    ('4','4'),
    ('5','5')
  ]

  title=models.CharField(max_length=100)
  status=models.CharField(max_length=2,choices=status_select)
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  time=models.DateTimeField(auto_now_add=True)
  precedence=models.CharField(max_length=2,choices=precedence_select)
