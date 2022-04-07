from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import NewUser, Feedback
from users.serializers import \
    UserSerializer,\
    LoginSerializer, \
    FeedbackSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = NewUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer