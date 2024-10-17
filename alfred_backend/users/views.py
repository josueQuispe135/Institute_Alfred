from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from .serializers import LoginSerializer

class LoginView(APIView):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'message': 'Login successful', 'token': 'abc123'})  # Ejemplo de token
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
