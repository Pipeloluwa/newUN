from django.db import models

# Create your models here.

class Information(models.Model):
    fullname = models.CharField(max_length=100)
    phone_no= models.PositiveIntegerField()
    instgram_handler= models.CharField(max_length=120)
    email_address= models.EmailField(unique=True)
    business_idea_craft_skill= models.CharField(max_length=100)
    description= models.TextField(max_length=200)

    def __str__(self):
        return f"{self.fullname},{self.phone_no},{self.instgram_handler},{self.email_address},{self.business_idea_craft_skill},{self.description}"