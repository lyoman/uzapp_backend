from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.serializers import (
    CharField, 
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    HiddenField,
    CurrentUserDefault
    )


User = get_user_model()

#User Details
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'first_name',
            'last_name', 
            'is_staff',
            'is_superuser',
            'is_active',
            'id',
        ]


#user Login
class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    user = UserDetailSerializer(read_only=True)
    # email = EmailField(label='Email Address', required=True, allow_blank=False)
    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
            'password',
            'token',
            'user',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            } 
    def validate(self, data):
        user_obj = None
        # email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("Reg Number is required to login.")

        user = User.objects.filter(
                Q(username=username)
        ).distinct()
        # user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Reg Number is not valid.")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        data["token"] = "SOME RANDOM TOKEN"
        return data

#Create Album
class UserCreateSerializer(ModelSerializer):
    email = EmailField(label = 'Email Address')
    first_name = CharField()
    last_name = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name', 
            # 'phone',
            'password',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        username = data['username']
        user_qs = User.objects.filter(username = username)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        username = data.get("username")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
            'is_active',
            'id',
        ]