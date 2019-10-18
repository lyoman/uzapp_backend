from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from cordinates.models import Cordinate


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
    CordinateCreateUpdateSerializer,
    CordinateListSerializer,
    CordinateDetailSerializer, 
    )

#Creating an Cordinate
class CordinateCreateAPIView(CreateAPIView):
    queryset = Cordinate.objects.all()
    serializer_class = CordinateCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class CordinateUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Cordinate.objects.all()
    serializer_class = CordinateCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Cordinate
class CordinateDeleteAPIView(DestroyAPIView):
    queryset = Cordinate.objects.all()
    serializer_class = CordinateDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Cordinate Details
class CordinateDetailAPIView(RetrieveAPIView):
    queryset = Cordinate.objects.all()
    serializer_class = CordinateDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Cordinate List
class CordinateListAPIView(ListAPIView):
    serializer_class = CordinateListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'location', 'icon']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Cordinate.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset