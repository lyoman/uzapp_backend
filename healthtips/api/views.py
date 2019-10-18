from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from healthtips.models import Healthtip


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
    HealthtipsCreateUpdateSerializer,
    HealthtipsListSerializer,
    HealthtipsDetailSerializer, 
    )


#Creating an Healthtip
class HealthtipCreateAPIView(CreateAPIView):
    queryset = Healthtip.objects.all()
    serializer_class = HealthtipsCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class HealthtipUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Healthtip.objects.all()
    serializer_class = HealthtipsCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Healthtip
class HealthtipDeleteAPIView(DestroyAPIView):
    queryset = Healthtip.objects.all()
    serializer_class = HealthtipsDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Healthtip Details
class HealthtipDetailAPIView(RetrieveAPIView):
    queryset = Healthtip.objects.all()
    serializer_class = HealthtipsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Healthtips List
class HealthtipListAPIView(ListAPIView):
    serializer_class = HealthtipsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'question', 'answer']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Healthtip.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset