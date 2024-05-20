# views.py
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Serra  # Import the Serra model
from register.forms import RegisterForm
from rest_framework.views import APIView

TOKEN = "Miy6mxoa8dJvhOU6YIRMa33A9Qs57obYRMIbHb1EET16fqKLoz4DfVJ2BfBACpG7UooKDyYAu7qkDMck"

@api_view(['GET'])
def get_user_password(request, username):
    token = request.headers.get('Authorization')

    if token != f"Bearer {TOKEN}":
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(username=username)
        return Response({"password": user.password})
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_user_serre(request, username):
    token = request.headers.get('Authorization')

    if token != f"Bearer {TOKEN}":
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(username=username)
        serre = Serra.objects.filter(user=user)
        serre_data = [{"code": s.code} for s in serre]
        return Response({"serre": serre_data})
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user_serra(request, username, serra_code):
    token = request.headers.get('Authorization')

    if token != f"Bearer {TOKEN}":
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(username=username)
        serra = Serra.objects.get(user=user, code=serra_code)
        serra.delete()
        return Response({"success": "Serra deleted"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Serra.DoesNotExist:
        return Response({"error": "Serra not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_user_serra(request, username):
    token = request.headers.get('Authorization')

    if token != f"Bearer {TOKEN}":
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(username=username)
        serra_code = request.data.get('code')

        if not serra_code:
            return Response({"error": "No serra code provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the new Serra object
        serra = Serra.objects.create(user=user, code=serra_code)
        return Response({"success": "Serra added", "serra": {"code": serra.code}}, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

class RegisterUser(APIView):
    def post(self, request):
        form = RegisterForm(request.data)
        if form.is_valid():
            user = form.save()
            return Response({"success": "User created successfully", "username": user.username}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
