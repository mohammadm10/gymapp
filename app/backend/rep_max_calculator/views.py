from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from pymongo import MongoClient
from rest_framework.response import Response
from datetime import datetime

class DataSerializer(serializers.Serializer):
    weight = serializers.FloatField(max_value=None, min_value=None)
    reps = serializers.IntegerField(max_value=None, min_value=None)

class CalculateRepAPIView(APIView):
    def post(self, request):
        
        serializer = DataSerializer(data=request.data)
        
        if serializer.is_valid():
            
            weight = serializer.validated_data['weight']
            reps = serializer.validated_data['reps']
            
            # Epley's formula
            one_rep_max = float(weight*(1+(0.0333*reps)))
            rounded_one_rep_max = round(one_rep_max, 1)
            
            # calculate 5x5 weight
            rounded_five_by_five = round(float(one_rep_max*0.85), 1)
            
            # hypertrophy calculation
            hypo_low_side = round(float(one_rep_max*0.6), 1)
            hypo_high_side = round(float(one_rep_max*0.8), 1)
        return Response({
                "one_rep_max": rounded_one_rep_max,
                "five_by_five": rounded_five_by_five,
                "hypertrophy_low": hypo_low_side,
                "hypertrophy_high": hypo_high_side
            }, status=200)