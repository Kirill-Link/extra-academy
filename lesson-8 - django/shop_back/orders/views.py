from rest_framework import viewsets, permissions, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemList(viewsets.ModelViewSet):
    queryset = OrderItem.objects.filter(is_active=True, quantity__gt=0)
    serializer_class = OrderItemSerializer


class BuyProductView(APIView):
    def post(self, request, product_id):
        user = request.user
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.create(user=user, product=product)

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserOrderViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(user_id=user_id)
