from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)