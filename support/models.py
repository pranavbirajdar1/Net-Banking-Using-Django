from django.db import models

# Create your models here.
class Support(models.Model):
    id = models.BigAutoField(verbose_name='ID',primary_key=True)
    name =models.CharField(max_length=50,verbose_name='Name')
    email = models.EmailField()
    subject =models.TextField(max_length=300)
    message =models.TextField(max_length=400)
    
    def __str__(self):
        return f"{self.name} {self.subject}"
    
    def save(self, *args, **kwargs):
        # Capitalize names and format pan before saving
        self.name= self.name.capitalize()
        