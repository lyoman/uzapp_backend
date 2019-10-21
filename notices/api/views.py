from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from notices.models import Notice


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
    NoticesCreateUpdateSerializer,
    NoticesListSerializer,
    NoticesDetailSerializer, 
    )


#Creating an Notice
class NoticeCreateAPIView(CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticesCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class NoticeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticesCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Notice
class NoticeDeleteAPIView(DestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticesDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Notice Details
class NoticeDetailAPIView(RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticesDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Notices List
class NoticeListAPIView(ListAPIView):
    serializer_class = NoticesListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Notice.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset