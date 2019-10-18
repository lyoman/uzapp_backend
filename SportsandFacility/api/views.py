from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from django.contrib.auth import get_user_model

from SportsandFacility.models import  SportsandClub, Facility, Category, Event


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
    EventCreateUpdateSerializer, 
    EventDetailSerializer,
    EventListSerializer,
    FacilityDetailSerializer,
    SportsandClubDetailSerializer,
    CategoryDetailSerializer,
    )


#Creating an ApplyMedical
class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an ApplyMedical
class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an ApplyMedical
class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]


# All ApplyMedicals List
class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


class FacilityDetailAPIView(ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilityDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Facility.objects.all()
        id = self.request.query_params.get('location', None)
        if id is not None:
            queryset = queryset.filter(location=id)
        return queryset

class CategoryDetailAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Category.objects.all()
        id = self.request.query_params.get('name', None)
        if id is not None:
            queryset = queryset.filter(name=id)
        return queryset


class SportsandClubDetailAPIView(ListAPIView):
    queryset = SportsandClub.objects.all()
    serializer_class = SportsandClubDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = SportsandClub.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset

class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'facility', 'location']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Event.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
