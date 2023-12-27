from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  #CSRF protection disabled
def test(request):
    if request.method == 'POST':
        try:
            #load data from frontend
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            
            #print data for validation
            print(f"Received username: {username}, password: {password}")

            return HttpResponse("Data received successfully", status=200)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)

