from django.db import models

class mainitem(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media_images/', null=True, blank=True)
    des = models.CharField(max_length=300,default='No description provided')

    def __str__(self):
        return self.name


class Firut(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media_images/', null=True, blank=True)
    des = models.CharField(max_length=300, default='No description provided')

    def __str__(self):
        return self.name
    

class Vegetables(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media_images/', null=True, blank=True)
    des = models.CharField(max_length=300, default='No description provided')

    def __str__(self):
        return self.name
    

class Signup(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class request(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    your_name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.CharField(max_length=25)
    main_category = models.CharField(max_length=25)
    item_name = models.CharField(max_length=56)
    message =models.CharField(max_length=50)

class sellproduct(models.Model):
    list_at = models.DateTimeField(auto_now_add=True)
    farmer_name = models.CharField(max_length=25)
    product = models.CharField(max_length=25)
    quantity_kg = models.CharField(max_length=25)
    price_kg = models.IntegerField(blank=True , null=True)
    harvest_date = models.DateField()

    packagingtype = [
        ("Loose", "Loose"),
        ("Bagged_25kg", "Bagged_25kg"),
        ("Bagged_50kg", "Bagged_25kg"),
        ("Custom", "Custom"),
    ]
    packaging = models.CharField(max_length=50, choices=packagingtype)

    description = models.CharField(max_length=60)
    image = models.ImageField(upload_to="sellproduct")
    location = models.CharField(max_length=50)

    deliveryopson = [
        ("self_pickup", "Self_Pickup"),
        ("courier", "Courier"),
        ("transport", "Transport"),
    ]
    delivery = models.CharField(max_length=50, choices=deliveryopson)
    contact = models.CharField(max_length=25)

