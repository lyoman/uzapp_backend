from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from drugs.models import Drug


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
    DrugsCreateUpdateSerializer,
    DrugsListSerializer,
    DrugsDetailSerializer, 
    )


#Creating an Drug
class DrugCreateAPIView(CreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugsCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class DrugUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugsCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Drug
class DrugDeleteAPIView(DestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugsDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Drug Details
class DrugDetailAPIView(RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Drugs List
class DrugListAPIView(ListAPIView):
    serializer_class = DrugsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'price', 'status']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Drug.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset