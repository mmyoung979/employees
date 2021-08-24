# Matthew Young Code Example August 2021
This project was created as a skill demonstration.

## What is this?
This is a small project that uses the following technologies:
* Flask / Python
* Firestore database
* React
* Docker

In this demonstration, you can create & delete employees from the database.

## How to run this project
Execute the following steps:
1. Upload a `firebase-sdk.json` file for your Firestore database in the `employees` directory.
2. Build the docker containers by running `docker-compose up -d --build` from the root directory
3. Access the homepage on [http://localhost:3000](http://localhost:3000)

## What else can I do with this?
You can run tests with the following command from the root directory: `make run-tests`