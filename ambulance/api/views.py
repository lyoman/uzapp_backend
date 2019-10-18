from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from ambulance.models import AmbulanceRequests


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
    AmbulanceCreateUpdateSerializer,
    AmbulanceListSerializer,
    AmbulanceDetailSerializer, 
    )

#Creating an Ambulance
class AmbulanceCreateAPIView(CreateAPIView):
    queryset = AmbulanceRequests.objects.all()
    serializer_class = AmbulanceCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class AmbulanceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AmbulanceRequests.objects.all()
    serializer_class = AmbulanceCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Ambulance
class AmbulanceDeleteAPIView(DestroyAPIView):
    queryset = AmbulanceRequests.objects.all()
    serializer_class = AmbulanceDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Ambulance Details
class AmbulanceDetailAPIView(RetrieveAPIView):
    queryset = AmbulanceRequests.objects.all()
    serializer_class = AmbulanceDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Ambulance List
class AmbulanceListAPIView(ListAPIView):
    serializer_class = AmbulanceListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['location', 'problem']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = AmbulanceRequests.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset