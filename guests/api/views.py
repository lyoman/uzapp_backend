from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from guests.models import Guest


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
    GuestCreateUpdateSerializer,
    GuestListSerializer,
    GuestDetailSerializer, 
    )

#Creating an Guest
class GuestCreateAPIView(CreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class GuestUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Guest
class GuestDeleteAPIView(DestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Guest Details
class GuestDetailAPIView(RetrieveAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Guest List
class GuestListAPIView(ListAPIView):
    serializer_class = GuestListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['phone', 'name', 'lat', 'lng']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Guest.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset