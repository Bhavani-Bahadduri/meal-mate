from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.username} {self.password} {self.email} {self.mobile} {self.address}"
    

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default="https://cwdaust.com.au/wpress/wp-content/uploads/2015/04/placeholder-restaurant.png")
    cuisine = models.CharField(max_length = 200)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.cuisine} {self.rating}/5"






class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = "menu_items")

    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default="https://th.bing.com/th?id=OIP.Jd-H-LHiVSkNBlLR65nuVwHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2")
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    is_veg = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"