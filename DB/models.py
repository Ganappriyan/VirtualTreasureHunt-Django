from django.db import models

class Participants(models.Model):
  teamname = models.CharField(max_length=50, default='NULL')
  collegename = models.CharField(max_length=50, default='NULL')
  starttime1 = models.CharField(max_length=10, default='0:0:0')
  level1 = models.CharField(max_length=10, default='0:0:0')
  level2 = models.CharField(max_length=10, default='0:0:0')
  level3 = models.CharField(max_length=10, default='0:0:0')
  totaltime1 = models.CharField(max_length=10, default='0:0:0')
  points1 = models.IntegerField(default=-1)
  
  def __str__(self):
    return self.teamname
  
class Finalers(models.Model):
  teamname = models.CharField(max_length=50, default='NULL')
  collegename = models.CharField(max_length=50, default='NULL')
  starttime2 = models.CharField(max_length=10, default='0:0:0')
  level4 = models.CharField(max_length=10, default='0:0:0')
  level5 = models.CharField(max_length=10, default='0:0:0')
  totaltime2 = models.CharField(max_length=10, default='0:0:0')
  points2 = models.IntegerField(default=-1)
  