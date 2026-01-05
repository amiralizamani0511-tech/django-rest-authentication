from django.db import models




class Kala(models.Model):
    name = models.CharField(max_length=125)
    price = models.IntegerField()
    kind = models.CharField(max_length=30)
    status = models.CharField(max_length=10,
                              choices=[("new","نو"),("used","دست دوم ")],
                              default="new")
    descriptions = models.TextField()
    # producedby = models.CharField(max_length=20)
