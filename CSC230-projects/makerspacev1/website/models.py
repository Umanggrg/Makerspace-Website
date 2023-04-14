from django.db import models

# Create your models here.
class Account(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    username = models.CharField(primary_key=True, max_length=55)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_loggedin = models.IntegerField(db_column='is_loggedIn')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'account'
        unique_together = (('username', 'password'),)
    
    def __str__(self):
        return self.username