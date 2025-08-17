from django.db import models



class teams(models.Model):
    name = models.TextField(primary_key = True)
    captain  = models.TextField()
    trophy = models.IntegerField()

class players(models.Model):
    player = models.TextField()
    name = models.TextField()
    type = models.TextField()
    jersey = models.IntegerField(primary_key = True)

class points(models.Model):
    name = models.TextField()
    win = models.IntegerField()
    lose = models.IntegerField()
    point = models.IntegerField() 

class stats(models.Model):
    player =  models.TextField()
    team = models.TextField()
    sixes = models.IntegerField()
    fours = models.IntegerField()
    runs = models.IntegerField()
    wicket = models.IntegerField()


    




