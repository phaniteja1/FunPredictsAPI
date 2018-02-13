from django.db import models


# Create your models here.
class Prediction(models.Model):
    ''' Contains the prediction model'''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    image_url = models.URLField(max_length=128, blank=True)

    class Meta:
        verbose_name = "Prediction"
        verbose_name_plural = "Predictions"

    def __str__(self):
        return self.title


class Stock(models.Model):
    ''' Contains the stock model '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(blank=False)
    price_change_value = models.IntegerField(blank=False)

    PRICE_CHANGE_CHOICES = (
        ('P', 'positive'),
        ('N', 'negative'),
    )
    price_change = models.CharField(max_length=1, choices=PRICE_CHANGE_CHOICES)
    prediction = models.ForeignKey(Prediction, related_name='stocks', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.title


class User(models.Model):
    ''' Contains the user model'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    money = models.IntegerField(blank=False)

    user_stocks = models.ManyToManyField(to='Stock', through='UserStock')

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class UserStock(models.Model):
    ''' Contains the stock and the number of stocks'''
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', related_name='user_stocks', on_delete=models.CASCADE)
    number_of_stocks = models.IntegerField()

    class Meta:
        verbose_name = "User Stock"
        verbose_name_plural = "User Stocks"
