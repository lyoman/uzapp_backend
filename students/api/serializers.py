from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db.models import Q
from students.models import Student

from rest_framework.serializers import (
    CharField, 
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    HiddenField,
    )


# Student = get_user_model()

#Student Details
class StudentDetailSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'regnumber',
            'email', 
            'first_name',
            'last_name', 
            # 'is_staff',
            # 'is_superuser',
            # 'is_active',
            'id',
        ]


#user Login
class StudentLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    regnumber = CharField()
    user = StudentDetailSerializer(read_only=True)
    # email = EmailField(label='Email Address', required=True, allow_blank=False)
    class Meta:
        model = Student
        fields = [
            'regnumber',
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
        regnumber = data.get("regnumber", None)
        password = data["password"]
        if not regnumber:
            raise ValidationError("Reg Number is required to login.")

        user = Student.objects.filter(
                Q(regnumber=regnumber)
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
class StudentCreateSerializer(ModelSerializer):
    email = EmailField(label = 'Email Address')
    first_name = CharField()
    last_name = CharField()
    class Meta:
        model = Student
        fields = [
            'regnumber',
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
        regnumber = data['regnumber']
        user_qs = Student.objects.filter(regnumber = regnumber)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        regnumber = data.get("regnumber")
        return value

    def create(self, validated_data):
        regnumber = validated_data['regnumber']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        user_obj = Student(
                regnumber = regnumber,
                email = email,
                password = password,
                first_name = first_name,
                last_name = last_name,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class StudentListSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'regnumber',
            'email',
            'first_name',
            'last_name',
            # 'is_staff',
            # 'is_superuser',
            # 'is_active',
            'id',
        ]