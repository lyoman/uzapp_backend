from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.parsers import (
                                    JSONParser,
                                    MultiPartParser,
                                    FormParser,
                                    )

from rest_framework.generics import (
    CreateAPIView,
      ListAPIView,
    )

from students.models import Student



from .serializers import (
    StudentLoginSerializer,
    StudentCreateSerializer,
    StudentListSerializer,
    )
 
from django.db.models import Q
 
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
) 
 

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )


#Student Login
class StudentLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = StudentLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StudentLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


#Register Student
class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()
    permission_classes = [AllowAny]



class StudentListAPIView(ListAPIView):
    serializer_class = StudentListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Student.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset