from django.db import models

# Create your models here.
class players(models.Model):
    #usr_type=models.ForeignKey('user_type',on_delete='PROTECT')

    player_fullname        =models.CharField(max_length=50)
    player_login_email     =models.CharField(max_length=20)
    player_username        =models.CharField(max_length=50)
    player_Steam_id        =models.IntegerField()
    player_contactno       =models.IntegerField()
    player_Dota_rank       =models.CharField(max_length=20)
    # player_creation_time   =models.DateTimeField()