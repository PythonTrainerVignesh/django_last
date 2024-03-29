from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import models, User


class RegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        # fields = '__all__'


class Students(models.Model):
    s_name = models.CharField(max_length=100)
    s_email = models.EmailField(max_length=100)
    s_phone = models.BigIntegerField(null=True, blank=True)
    s_entry_date = models.DateTimeField(auto_now_add=True)
    manager = models.Manager()


class Products(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=500)
    manager = models.Manager()








