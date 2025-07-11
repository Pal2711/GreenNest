from django.db import models

# Create your models here.


class usersgimup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Password = models.CharField(max_length=50)
    checkbox = models.BooleanField(default=False)


class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField

class payment(models.Model):
    name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20, choices=[
        ('cod', 'cod'),
        ('card', 'card'),
        ('card', 'Credit/Debit Card'),
        ('upi', 'upi'),
    ])