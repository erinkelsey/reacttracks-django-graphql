# reacttracks-django-graphql
Django GraphQL backend for ReactTracks app

## About
This is a very simple project called ReactTracks. The backend stack is Python/Django/SQLite/GraphQL/Graphene. The frontend for this project is reacttracks-graphql-apollo.

## Features
Auth:
  - Registration
  - Login
  - Signout
  
Tracks:
  - Create Track
  - Update Track
  - Delete Track
  - Track Information
  - Like Track
  - Play Track
  
Profile:
  - User Information
  - Created Tracks
  - Liked Tracks 

## Install
Install Dependencies (in same folder as Pipfile):

    pipenv install 
    
## Setup
DB Settings:
- Add your DB details to settings.py

DB Migrations:

    python manage.py migrate

## TODO
- unit tests
- integration tests
