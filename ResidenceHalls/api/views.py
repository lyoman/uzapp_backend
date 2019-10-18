from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from django.contrib.auth import get_user_model

from ResidenceHalls.models import  RezHall, Janitor, Warden, Commitie


from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

# User = get_user_model()

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)
 

from .permissions import IsOwnerOrReadOnly

# from users.api.serializers import UserListSerializer

from .serializers import (
    RezHallCreateUpdateSerializer, 
    RezHallDetailSerializer,
    RezHallListSerializer,
    JanitorDetailSerializer,
    WardenDetailSerializer,
    CommitieDetailSerializer,
    )


#Creating an ApplyMedical
class RezHallCreateAPIView(CreateAPIView):
    queryset = RezHall.objects.all()
    serializer_class = RezHallCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an ApplyMedical
class RezHallUpdateAPIView(RetrieveUpdateAPIView):
    queryset = RezHall.objects.all()
    serializer_class = RezHallCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an ApplyMedical
class RezHallDeleteAPIView(DestroyAPIView):
    queryset = RezHall.objects.all()
    serializer_class = RezHallDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]


# All ApplyMedicals List
class RezHallDetailAPIView(RetrieveAPIView):
    queryset = RezHall.objects.all()
    serializer_class = RezHallDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


class JanitorDetailAPIView(ListAPIView):
    queryset = Janitor.objects.all()
    serializer_class = JanitorDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Janitor.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset

class CommitieDetailAPIView(ListAPIView):
    queryset = Commitie.objects.all()
    serializer_class = CommitieDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Commitie.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset


class WardenDetailAPIView(ListAPIView):
    queryset = Warden.objects.all()
    serializer_class = WardenDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Warden.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset

class RezHallListAPIView(ListAPIView):
    serializer_class = RezHallListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'capacity', 'location']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = RezHall.objects.all()
        id = self.request.query_params.get('location', None)
        if id is not None:
            queryset = queryset.filter(location=id)
        return queryset
