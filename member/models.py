from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    device = models.CharField(max_length=100,null=True)
    phone = models.IntegerField(null=True)

class GameScore(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    game_name = models.CharField(max_length=200)
    score = models.IntegerField(null=True)
    date_played = models.DateField(auto_now_add=True)
        