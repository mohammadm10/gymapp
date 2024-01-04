import json
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
import bcrypt

# MongoDB connection setup
client = MongoClient('localhost', 27017)

# Serializer to validate and parse incoming data
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)

# API view for handling user sign-up
class SignUpAPIView(APIView):
    def post(self, request):
        # Initialize the serializer with the incoming data
        serializer = UserSerializer(data=request.data)
        
        # Check if the incoming data is valid
        if serializer.is_valid():
            # Extract validated data from the serializer
            username = serializer.validated_data['username']
            firstName = serializer.validated_data['firstName']
            lastName = serializer.validated_data['lastName']
            email = serializer.validated_data['email']
            password = request.data['hashedPassword']
            
            salt = bcrypt.gensalt()
            new_hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            # Connect to the MongoDB database and users collection
            db = client['GymAppDB']
            collection = db['Users']

            # Prepare the data to be inserted into MongoDB
            user_data = {"username": username, "firstName": firstName, "lastName": lastName, "email": email, "password": new_hashed_password}
            
            # Insert the data into MongoDB
            result = collection.insert_one(user_data)

            # Check if the insertion was successful
            if result.inserted_id:
                return Response("Data received and inserted successfully", status=201)
            else:
                return Response("Failed to insert data into MongoDB", status=500)
        else:
            # Return validation errors if the incoming data is not valid
            return Response(serializer.errors, status=400)
