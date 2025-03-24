### Introduction
#### Bookit
A trip planing and Event Discovery App.

This app is for organising your vacation and group plans that require booking 
coordination and group commitment planning, as well as for discovering city events
tailored to your preferences.

### Tech Stack
1. PostgresSQL database (Running in Docker on local/cloud server)
2. Python backend codebase (FastAPI app, runs with Uvicorn, running in Docker on local/cloud server)
3. Redis (Caching/temp data for Python backend, running in Docker on local/cloud server)
4. Swift frontend (To be available on the App Store for iOS download)


### Developer Setup Instructions
#### Backend

1.	Create a local keys.list file with environment variables, and configure your Python run settings to use it.
2.	Install dependencies from requirements.txt.
3.	Clone the Git repository and create a development branch based on main.
4.	Push changes to the development branch and open a merge request to merge into main upon review.


#### Frontend