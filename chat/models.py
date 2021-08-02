from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model): 
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

class Member(models.Model): 
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  chat_id = models.ForeignKey(Chat,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  chat_id = models.ForeignKey(Chat,on_delete=models.CASCADE)
  text = models.CharField(max_length=200)
  file_url = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)


