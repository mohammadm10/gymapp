from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection setup
client = MongoClient('localhost', 27017)

class InfoSerializer(serializers.Serializer):
    reps = serializers.IntegerField()
    weight = serializers.IntegerField()

class SetSerializer(serializers.Serializer):
    exercise = serializers.CharField()
    sets = serializers.CharField()
    info = InfoSerializer(many=True)

class WorkoutSerializer(serializers.Serializer):
    workoutName = serializers.CharField()
    sets = SetSerializer(many=True)

class WorkoutPlanAPIView(APIView):
    def post(self, request):

        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            
            # Access the validated data
            workout_name = serializer.validated_data['workoutName']
            sets = serializer.validated_data['sets']

            # Connect to DB
            db = client['GymAppDB']
            collection = db['workout_plans']
            
            # Get the current user
            username = 'user2'  # Replace with logic to get the current user, just for testing now
            
             # Check if user entry exists
            existing_entry = collection.find_one({'username': username})

            if existing_entry:
                # Update the existing entry with the new workout
                collection.update_one(
                    {'username': username},
                    {'$push': {'workouts': {'workout_name': workout_name, 'sets': sets}}}
                )
            else:
                # Create a new entry for the user
                workout_plan = {
                    'username': username,
                    'workouts': [{'workout_name': workout_name, 'sets': sets}],
                    'date_created': datetime.now(),
                }

                # Insert the workout plan into MongoDB
                result = collection.insert_one(workout_plan)

                if not result.inserted_id:
                    return Response({'error': 'Failed to insert workout plan'}, status=500)


            return Response({'message': 'Data received successfully'}, status=200)
        else:
            print(serializer.errors)
            return Response({'error': 'Invalid data'}, status=400)