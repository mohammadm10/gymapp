from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
import json
import requests
import os

class WorkoutGenSerializer(serializers.Serializer):
    muscleSelect = serializers.CharField()
    levelSelect = serializers.CharField()
    goalSelect = serializers.CharField()
    APINotes = serializers.CharField(required=False, allow_blank=True)

class APIWorkoutGenAPIView(APIView):
    def post(self, request):
        serializer = WorkoutGenSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract validated data from the serializer
            muscle = serializer.validated_data['muscleSelect']
            experience = serializer.validated_data['levelSelect']
            goal = serializer.validated_data['goalSelect']
            notes = serializer.validated_data['APINotes']
            
            
            try:
                prompt = f'Please provide me with personalized gym exercises by filling in the following information: 1. The muscle group you want to target (e.g., chest, legs, back): {muscle} 2. Your level of gym experience (e.g., beginner, intermediate, advanced): {experience} 3. Your fitness goal (e.g., muscle gain, weight loss, overall fitness): {goal} Also consider these notes from the user for their workout: {notes} For each exercise, specify the number of sets and reps using the format \'X to Y reps.\' Number the exercises as follows: 1., 2., etc. Please use spaces instead of dashes in compound exercises (e.g., push ups instead of push-ups). Example input: 1. Chest 2. Intermediate 3. Muscle gain Based on this information, provide a sentence with the numbered exercises, a brief description of each workout, and one helpful tip for each exercise in the format \'Tip: .\''
                model = 'gpt-3.5-turbo-0613'
                
                response = requests.post(
                    'https://api.openai.com/v1/chat/completions',
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {os.environ.get("OPENAI_KEY")}',
                    },
                    data=json.dumps({
                        'model': model,
                        'messages': [{'role': 'system', 'content': prompt}],
                    })
                )
                
                # Process the response
                result = response.json()
                print(result)
                return Response({'result': result}, status=200)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
            
        else:
            # Handle invalid serializer data
            return Response(serializer.errors, status=400)