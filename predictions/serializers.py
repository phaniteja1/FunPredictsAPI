from rest_framework import serializers
from .models import Prediction, Stock, User, UserStock


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('id', 'title', 'image_url', 'stocks')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'money', 'user_stocks')


class UserStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStock
        fields = ('id', 'user', 'stock', 'number_of_stocks')
