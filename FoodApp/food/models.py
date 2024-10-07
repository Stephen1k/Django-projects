from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://valtoripizzakitchen.com/wp-content/uploads/2021/03/pizzeria-template-header-pizza-img.png")
    
    # When item gets added, get redirected to that items detail page
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})