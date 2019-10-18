from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from news.models import New, Reader


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
    NewsCreateUpdateSerializer,
    NewsListSerializer,
    NewsDetailSerializer, 
    ReaderDetailSerializer,
    ReaderListSerializer
    # NewCreateUpdateSerializer,
    )

# Reader Details
class ReaderDetailAPIView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'id']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = New.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


#Creating an New
class NewCreateAPIView(CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewsCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class NewUpdateAPIView(RetrieveUpdateAPIView):
    queryset = New.objects.all()
    serializer_class = NewsCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an New
class NewDeleteAPIView(DestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# New Details
class NewDetailAPIView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All News List
class NewListAPIView(ListAPIView):
    serializer_class = NewsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'reader']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = New.objects.all()
        id = self.request.query_params.get('reader_id', None)
        if id is not None:
            queryset = queryset.filter(reader_id=id)
        return queryset