from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from laptopreg.models import LaptopsRegister


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
    LaptopsRegisterCreateUpdateSerializer,
    LaptopsRegisterListSerializer,
    LaptopsRegisterDetailSerializer, 
    )

#Creating an LaptopsRegister
class LaptopsRegisterCreateAPIView(CreateAPIView):
    queryset = LaptopsRegister.objects.all()
    serializer_class = LaptopsRegisterCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class LaptopsRegisterUpdateAPIView(RetrieveUpdateAPIView):
    queryset = LaptopsRegister.objects.all()
    serializer_class = LaptopsRegisterCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an LaptopsRegister
class LaptopsRegisterDeleteAPIView(DestroyAPIView):
    queryset = LaptopsRegister.objects.all()
    serializer_class = LaptopsRegisterDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# LaptopsRegister Details
class LaptopsRegisterDetailAPIView(RetrieveAPIView):
    queryset = LaptopsRegister.objects.all()
    serializer_class = LaptopsRegisterDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All LaptopsRegister List
class LaptopsRegisterListAPIView(ListAPIView):
    serializer_class = LaptopsRegisterListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['model','make', 'macaddress', 'color', 'serialnumber', 'user']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = LaptopsRegister.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset