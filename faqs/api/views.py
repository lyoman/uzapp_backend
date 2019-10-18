from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from faqs.models import Faq


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
    FaqsCreateUpdateSerializer,
    FaqsListSerializer,
    FaqsDetailSerializer, 
    )


#Creating an Faq
class FaqCreateAPIView(CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqsCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class FaqUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqsCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Faq
class FaqDeleteAPIView(DestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqsDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Faq Details
class FaqDetailAPIView(RetrieveAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Faqs List
class FaqListAPIView(ListAPIView):
    serializer_class = FaqsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'question', 'answer']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Faq.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset