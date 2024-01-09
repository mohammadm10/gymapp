import json
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from django.core.mail import send_mail
import secrets  # For generating secure tokens
from rest_framework import generics

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
            
            # Check if the username already exists in the database
            existing_username = collection.find_one({"username": username})

            if existing_username:
                return Response("Username already exists", status=409)

            # Check if the email already exists in the database
            existing_email = collection.find_one({"email": email})

            if existing_email:
                return Response("Email already associated with an account", status=409)

            # Generate a unique verification token
            verification_token = secrets.token_urlsafe(32)

            # Prepare the data to be inserted into MongoDB
            user_data = {
                "username": username,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "password": new_hashed_password,
                "verification_token": verification_token,
                "is_verified": False  # Initially set to False until user verifies email
            }
            
            # Insert the data into MongoDB
            result = collection.insert_one(user_data)

            # Check if the insertion was successful
            if result.inserted_id:
                # Send email with verification link, uncomment later on
                # verification_link = f"http://127.0.0.1:8000/verify/?token={verification_token}"
                # send_mail(
                #     "Verify Your Email",
                #     f"Click the following link to verify your email: {verification_link}",
                #     "",  # Sender email
                #     ["mohammadali_10@hotmail.com"],  # Recipient email
                #     fail_silently=False,
                # )
                return Response("Data received and inserted successfully. Check your email for verification instructions.", status=201)
            else:
                return Response("Failed to insert data into MongoDB", status=500)
        else:
            # Return validation errors if the incoming data is not valid
            return Response(serializer.errors, status=400)
        
class VerifyView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        
        # Extract the token from the query parameters
        verification_token = request.query_params.get('token')

        if verification_token:
            # Connect to MongoDB and check if the token exists
            db = client['GymAppDB']
            collection = db['Users']

            user = collection.find_one({"verification_token": verification_token, "is_verified": False})
            
            if user:
                # Update the user document to mark it as verified
                collection.update_one(
                    {"_id": user["_id"]},
                    {"$set": {"is_verified": True, "verification_token": None}}
                )

                return Response("Email verification successful", status=200)
            else:
                return Response("Invalid or expired verification token", status=400)
        else:
            return Response("Token not provided", status=400)
