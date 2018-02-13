from rest_framework import viewsets
from .models import Prediction, Stock, User, UserStock
from .serializers import PredictionSerializer, StockSerializer, UserSerializer, UserStockSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserStockViewSet(viewsets.ModelViewSet):
    queryset = UserStock.objects.all()
    serializer_class = UserStockSerializer

    def create(self, request):
        formattedData = {
            'number_of_stocks': request.data['number_of_stocks'],
            'user': request.data['user']['id'],
            'stock': request.data['stock']['id']
        }

        serializer = UserStockSerializer(data=formattedData)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
