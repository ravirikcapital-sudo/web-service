

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import UserRegistration
from .serializers import UserRegistrationSerializer
from django.contrib.auth.hashers import make_password

class RegisterUser(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        users = UserRegistration.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("Received data:", request.data)  # Log incoming data
        data = request.data.copy()  # Make a mutable copy

        serializer = UserRegistrationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()  # Serializer already hashes password in validate_password
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)  # ✅ Log errors to terminal
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
