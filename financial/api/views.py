from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from financial.models import FinancialStatement


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
    FinancialStatementCreateUpdateSerializer,
    FinancialStatementListSerializer,
    FinancialStatementDetailSerializer, 
    )

#Creating an FinancialStatement
class FinancialStatementCreateAPIView(CreateAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class FinancialStatementUpdateAPIView(RetrieveUpdateAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an FinancialStatement
class FinancialStatementDeleteAPIView(DestroyAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# FinancialStatement Details
class FinancialStatementDetailAPIView(RetrieveAPIView):
    queryset = FinancialStatement.objects.all()
    serializer_class = FinancialStatementDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All FinancialStatement List
class FinancialStatementListAPIView(ListAPIView):
    serializer_class = FinancialStatementListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'description']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = FinancialStatement.objects.all()
        id = self.request.query_params.get('user_id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset