from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class State(models.Model):
  state = models.CharField(max_length=150)

  class Meta:
    db_table = 'state'

class City(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = models.CharField(max_length=150)

  class Meta:
    db_table = 'city'

class Area(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  area = models.CharField(max_length=150)

  class Meta:
    db_table = 'area'
  

class Role(models.Model):
  role = models.CharField(max_length=100)

  class Meta:
    db_table = 'role'


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.ForeignKey(Role, on_delete=models.CASCADE)
  description = models.CharField(max_length=1000, null=True)
  gender = models.CharField(max_length=120, null=True)
  dob = models.DateField(null=True)
  contact = models.PositiveBigIntegerField(null=True)
  owner_name = models.CharField(max_length=150, null=True)
  owner_number = models.PositiveBigIntegerField(null=True)
  address = models.CharField(max_length=1000, null=True)
  state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
  city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
  area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
  certified = models.CharField(max_length=100, null=True)
  gst_no = models.CharField(max_length=100, null=True)
  image = models.FileField(upload_to='profile', null=True)

  class Meta:
    db_table = 'profile'




class Inquiry(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField()
  contact = models.PositiveBigIntegerField()
  subject = models.CharField(max_length=500)
  message = models.CharField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'inquiry'


class FoodCategory(models.Model):
  name = models.CharField(max_length=150)
  agency = models.ForeignKey(Profile, on_delete=models.CASCADE)

  class Meta:
    db_table = 'food_category'


class Food(models.Model):
  ftime = models.CharField(max_length=150)
  fname = models.CharField(max_length=150)
  fprice = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.CharField(max_length=1500)
  fimage = models.FileField(upload_to='agency')
  ftype = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
  roti = models.CharField(max_length=200)
  rise = models.CharField(max_length=200)
  veg = models.CharField(max_length=200)
  butter_milk = models.CharField(max_length=200)
  papad = models.CharField(max_length=200)
  agency = models.ForeignKey(Profile, on_delete=models.CASCADE)

  class Meta:
    db_table = 'food'


class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  fname = models.CharField(max_length=300)
  ftime = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.IntegerField()
  total_price = models.DecimalField(max_digits=10, decimal_places=2)

  class Meta:
    db_table = 'cart'


class Orders(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  agency = models.ForeignKey(Profile, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=200, default='Pending')

  class Meta:
    db_table = 'orders'

class OrderItems(models.Model):
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  fname = models.CharField(max_length=300)
  ftime = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.IntegerField()
  

  class Meta:
    db_table = 'order_items'


class TiffinDeliveryAddress(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.CASCADE)
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  username = models.CharField(max_length=100)
  email = models.EmailField()
  contact = models.PositiveBigIntegerField()
  address = models.CharField(max_length=1000)

  class Meta:
    db_table = 'tiffin_delivery_address'




class Feedback(models.Model):
  review = models.IntegerField()
  feedback = models.TextField()
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)