from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from lostandfound.models import Lost


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
    LostsCreateUpdateSerializer,
    LostsListSerializer,
    LostsDetailSerializer, 
    )


#Creating an Lost
class LostCreateAPIView(CreateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostsCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class LostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostsCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Lost
class LostDeleteAPIView(DestroyAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostsDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Lost Details
class LostDetailAPIView(RetrieveAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Losts List
class LostListAPIView(ListAPIView):
    serializer_class = LostsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'contact', 'place']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Lost.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset