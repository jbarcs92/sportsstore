from django.db import models
from django.urls import reverse

class Football(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('footballdetail', kwargs={'football_id': self.id})

class Baseball(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('baseballdetail', kwargs={'baseball_id': self.id})

class Basketball(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('basketballdetail', kwargs={'basketball_id': self.id})

class Hockey(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('hockeydetail', kwargs={'hockey_id': self.id})

class Mma(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10,decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('mmadetail', kwargs={'mma_id': self.id})

class Soccer(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10,decimal_places=2)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('soccerdetail', kwargs={'soccer_id': self.id})

