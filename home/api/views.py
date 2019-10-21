from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from home.models import Home


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
    HomesCreateUpdateSerializer,
    HomesListSerializer,
    HomesDetailSerializer, 
    )


#Creating an Home
class HomeCreateAPIView(CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomesCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class HomeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomesCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Home
class HomeDeleteAPIView(DestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomesDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Home Details
class HomeDetailAPIView(RetrieveAPIView):
    queryset = Home.objects.all()
    serializer_class = HomesDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Homes List
class HomeListAPIView(ListAPIView):
    serializer_class = HomesListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['link_url', 'title', 'content']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Home.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset