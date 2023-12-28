import json
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt

# Assuming MongoDB server is running on localhost:27017
client = MongoClient('localhost', 27017)
@csrf_exempt

def test(request):
    if request.method == 'POST':
        try:
            # Load data from frontend
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')

            # Print data for validation
            print(f"Received username: {username}, password: {password}")

            # Connect to the MongoDB database and users collection
            db = client['GymAppDB']
            collection = db['Users']

            # Check if the username and password already exist in the Users collection
            existing_user = collection.find_one({"username": username, "password": password})

            if existing_user:
                return HttpResponse("User already exists in MongoDB", status=409)  # Conflict status code
            else:
                return HttpResponse("User does not exist in MongoDB, you can proceed", status=200)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)
