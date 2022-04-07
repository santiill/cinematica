from rest_framework import serializers

from .models import NewUser, Feedback


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = NewUser
        fields = ["username", "email", "password", "role"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("Email is already in use")}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return NewUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ["email", "password", "username"]


class FeedbackSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'client', 'feedback']