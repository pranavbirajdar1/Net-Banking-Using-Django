from django.db import models

# Create your models here.
class Support(models.Model):
    id = models.BigAutoField(verbose_name='ID',primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Name', null=True, blank=True)
    email = models.EmailField()
    subject =models.CharField(max_length=300,null=True)
    message =models.CharField(max_length=400,null=True)
    sendername = models.CharField(max_length=50, verbose_name='Sender_Name', null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.subject}"
    

    def save(self, *args, **kwargs):
        # Check if 'name' is not None or empty before capitalizing
        if self.name:
            self.name = self.name.capitalize()

        super().save(*args, **kwargs)  
        