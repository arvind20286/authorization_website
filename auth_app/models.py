from django.db import models

# Create your models here.
class AuthProvider(models.Model):
  name = models.CharField(max_length=10, primary_key=True)

class User(models.Model):
  email = models.EmailField(primary_key=True)
  password = models.CharField(max_length=20, blank=True, null=True)
  google_id = models.CharField(max_length=255, blank=True, null=True)
  auth_provider = models.ForeignKey(AuthProvider, on_delete=models.SET_NULL, null=True)
  


