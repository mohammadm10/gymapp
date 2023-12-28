import json
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt


# Assuming your MongoDB server is running on localhost:27017
client = MongoClient('localhost', 27017)
@csrf_exempt

def signUp(request):
    if request.method == 'POST':
        try:
            # Load data from frontend
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            firstName = data.get('firstName')
            lastName = data.get('lastName')
            password = data.get('password')

            # Print data for validation
            print(f"Received username: {username}, firstName: {firstName}, lastName: {lastName} password: {password}")

            # Connect to the MongoDB database and users collection
            db = client['GymAppDB']
            collection = db['Users']

            # Insert the username and password into MongoDB
            user_data = {"username": username, "firstName": firstName, "lastName": lastName, "password": password}
            result = collection.insert_one(user_data)

            if result.inserted_id:
                return HttpResponse("Data received and inserted successfully", status=200)
            else:
                return HttpResponse("Failed to insert data into MongoDB", status=500)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)
