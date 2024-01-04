import json
from django.http import HttpResponse
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
import bcrypt

# Assuming MongoDB server is running on localhost:27017
client = MongoClient('localhost', 27017)
@csrf_exempt

def test(request):
    if request.method == 'POST':
        try:
            # Load data from frontend
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            entered_password = data.get('hashedPassword')  # Send plain text password from the frontend

            # Connect to the MongoDB database and users collection
            db = client['GymAppDB']
            collection = db['Users']

            # Check if the username exists in the Users collection
            existing_user = collection.find_one({"username": username})
            
            if existing_user:
                # Get the stored hashed password from the database
                stored_password = existing_user.get('password')

                # Compare the entered password with the stored hashed password
                if bcrypt.checkpw(entered_password.encode('utf-8'), stored_password):
                    return HttpResponse("Login successful", status=200)
                else:
                    return HttpResponse("Incorrect password", status=401)  # Unauthorized status code
            else:
                return HttpResponse("User does not exist", status=404)  # Not Found status code

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return HttpResponse("Invalid JSON data", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)
