from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from django.contrib.auth import get_user_model

from directories.models import  PhoneNumber, Department, Faculty


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
    PhoneNumberCreateUpdateSerializer, 
    PhoneNumberDetailSerializer,
    PhoneNumberListSerializer,
    DepartmentDetailSerializer,
    FacultyDetailSerializer,
    )


#Creating an ApplyMedical
class PhoneNumberCreateAPIView(CreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an ApplyMedical
class PhoneNumberUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an ApplyMedical
class PhoneNumberDeleteAPIView(DestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]


# All ApplyMedicals List
class PhoneNumberDetailAPIView(RetrieveAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


class DepartmentDetailAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Department.objects.all()
        id = self.request.query_params.get('faculty_id', None)
        if id is not None:
            queryset = queryset.filter(faculty_id=id)
        return queryset

class FacultyDetailAPIView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

class PhoneNumberListAPIView(ListAPIView):
    serializer_class = PhoneNumberListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['phone', 'department']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = PhoneNumber.objects.all()
        id = self.request.query_params.get('department_id', None)
        if id is not None:
            queryset = queryset.filter(department_id=id)
        return queryset
