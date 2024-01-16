from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from pymongo import MongoClient
from rest_framework.response import Response
from datetime import datetime

# MongoDB connection setup
client = MongoClient('localhost', 27017)

class WeightSerializer(serializers.Serializer):
    weight = serializers.FloatField(max_value=None, min_value=None)

# Add weight API view
class AddWeightAPIView(APIView):
    def post(self, request):
        serializer = WeightSerializer(data=request.data)
        
        if serializer.is_valid():
            
            # Retract weight field from serializer
            weight = serializer.validated_data['weight']
            
            # Connect to DB
            db = client['GymAppDB']
            collection = db['personal_weight']
            
            # Get the current user
            username = 'user1'  # Replace with logic to get the current user, just for testing now
            
            # Create a weight data entry with the current date
            weight_data_entry = {'weight': weight, 'date': datetime.now().strftime('%Y-%m-%d')}
            
            # Find the user's document in the collection
            user_document = collection.find_one({'username': username})
            
            if user_document:
                # Update the existing user document with the new weight data
                collection.update_one(
                    {'username': username},
                    {'$push': {'weight_data': weight_data_entry}}
                )
            else:
                # Create a new user document if it doesn't exist
                collection.insert_one({
                    'username': username,
                    'weight_data': [weight_data_entry]
                })

            return Response("Weight added successfully", status=200)
        else:
            return Response(serializer.errors, status=400)