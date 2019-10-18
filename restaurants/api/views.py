from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from restaurants.models import Restaurant, Meal


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
    RestaurantCreateUpdateSerializer,
    RestaurantListSerializer,
    RestaurantDetailSerializer, 

    MealCreateUpdateSerializer,
    MealListSerializer,
    MealDetailSerializer, 
    )

#Creating an Restaurant
class RestaurantCreateAPIView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Restaurant
class RestaurantDeleteAPIView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Restaurant Details
class RestaurantDetailAPIView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Restaurant List
class RestaurantListAPIView(ListAPIView):
    serializer_class = RestaurantListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'location']
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset




# Meals

#Creating an Meal
class MealCreateAPIView(CreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an new
class MealUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealCreateUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Meal
class MealDeleteAPIView(DestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer
    lookup_field = 'pk'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrReadOnly]

# Meal Details
class MealDetailAPIView(RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

# All Meal List
class MealListAPIView(ListAPIView):
    serializer_class = MealListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['price', 'restaurant', "name"]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Meal.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset