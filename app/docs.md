## Requirements & User Stories
- User must be able to create an account:
    - Given a user is on the registration page
    - When the user fills out the required information and clicks on the "Create Account" button
    - Then the user's account should be successfully created and they should be redirected to the homepage.
- User must be able to sign in:
    - Given that the user is on the sign-in page,
    - When the user enters their username and password,
    - Then the system verifies the credentials and allows the user to sign in to their account.
- User must have a unique username:
    - Given that a user is registering for an account
    - When they enter a username 
    - Then the system should check if the username is already taken And display an error message if it is taken And proceed with the registration process if the username is unique
- User must be able to record their progress for each exercise that they choose to record:
    - Given that the user is logged into their account
    - When the user selects an exercise from the available options
    - Then the user should be able to record their progress for that exercise
- User can track their weight with a graph showing their fluctuation:
    - Given that I am a registered user on the weight tracking page
    - When I enter my weight data into the application on a regular basis And I have at least two data points recorded, 
    - Then I should be able to view a graph that displays my weight fluctuation over time.
- User can request a workout program to be created:
    - Given that the user is logged into their fitness app account
    - When the user navigates to the "Workout Generator" section of the app,
    - Then the user can request a workout program to be created by clicking on the "Create Program" button.
- Create analytics using data and graphs on each workout for progress:
    - Given that I am a registered user of the application
    - When I complete a workout session And record my progress
    - Then the application should store the workout data and generate analytics and graphs to track my progress over time
- Provide push notifications for workout reminders:
    - Given a registered user opted into push notifications
    - When the user sets a workout reminder in their app settings
    - Then the user should receive a push notification on their device at the specified time to remind them of their workout.