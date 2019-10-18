from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from foodordering.models import FoodOrder


from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)


from .permissions import IsOwnerOrReadOnly

from .serializers import (
    FoodOrderCreateUpdateSerializer,
    FoodOrderListSerializer,
    FoodOrderDetailSerializer, 
    )

#Creating an FoodOrder
class FoodOrderCreateAPIView(CreateAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class FoodOrderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an FoodOrder
class FoodOrderDeleteAPIView(DestroyAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# FoodOrder Details
class FoodOrderDetailAPIView(RetrieveAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All FoodOrder List
class FoodOrderListAPIView(ListAPIView):
    serializer_class = FoodOrderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['meal', 'amount', 'location']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = FoodOrder.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset