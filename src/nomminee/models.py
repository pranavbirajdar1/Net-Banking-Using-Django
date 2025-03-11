from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Nominee(models.Model):
    id = models.BigAutoField(db_index=True, primary_key=True)
    user = models.OneToOneField(User, verbose_name=("nominee"), on_delete=models.CASCADE , related_query_name='nominee')
    name = models.CharField(max_length=10, verbose_name="First Name" , blank =True , null =True)
    relation = models.CharField(max_length=18 , verbose_name='Relation' , blank=True , null= False)
    contact = models.CharField(max_length=10, verbose_name="Contact Number" , blank =True , null =True)

    def __str__(self):
        return f'{self.user.username} Has Nominee : Name-> {self.name} : Relation-> {self.relation} : Contact-> {self.contact}'

    def __unicode__(self):
        return 
    def save(self, *args, **kwargs):
        
        super(Nominee, self).save(*args, **kwargs)
