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
        number_of_stocks = request.data['number_of_stocks']
        user_id = request.data['user']['id']
        stock_id = request.data['stock']['id']

        formattedData = {
            'number_of_stocks': number_of_stocks,
            'user': user_id,
            'stock': stock_id
        }

        serializer = UserStockSerializer(data=formattedData)

        if serializer.is_valid():
            serializer.save()
            UserStockViewSet.update_user_money(user_id, stock_id, number_of_stocks, "SUBTRACT")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        user_id = self.get_object().user.id
        stock_id = self.get_object().stock.id
        number_of_stocks = self.get_object().number_of_stocks

        instance = self.get_object()
        self.perform_destroy(instance)

        UserStockViewSet.update_user_money(user_id, stock_id, number_of_stocks, "ADD")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update_user_money(user_id, stock_id, number_of_stocks, transaction):
        ''' update user money when stocks are bought '''
        currentStock = Stock.objects.filter(id=stock_id)
        currentUserQuerySet = User.objects.filter(id=user_id)
        currentUser = currentUserQuerySet[0]

        amountDifference = number_of_stocks * currentStock[0].price
        if transaction == "ADD":
            currentUser.money = currentUser.money + amountDifference
        else:
            currentUser.money = currentUser.money - amountDifference

        currentUser.save()
