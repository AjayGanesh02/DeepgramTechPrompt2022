# Deepgram technical prompt

Build a simple API server to handle user audio projects. Your server should provide endpoints that allow a user to perform the following actions: 

- POST raw audio data and store it. 
 - Eg: $ curl -X POST --data-binary @myfile.wav 

http://localhost/post 

- GET a list of stored files, GET the content of stored files, and GET metadata of stored files, such as the duration of the audio. The GET endpoint(s) should accept a query parameter that allows the user to filter results. Results should be returned as JSON. 
 - Eg: $ curl http://localhost/download?name=myfile.wav 
 - Eg: $ curl http://localhost/list?maxduration=300 
 - Eg: $ curl http://localhost/info?name=myfile.wav 

## Setup Instructions
### Install
- Have Python 3.8 or later installed
- Run the following commands from the project folder's root:
```
sudo apt-get install sqlite3 curl
./bin/audioserverinstall
```
### Run
- Run the following command from the project folder's root:
```
./bin/audioserverrun
```

### Database
- The ./bin/audioserverdb script can be used with create/destroy/reset/dump options to configure the database

## File structure walkthrough

#### Files/Directories used for Python setup and module installation
- env/
- pyproject.toml
- requirements.txt
- setup.py

#### Scripts
- bin/*

#### Python Server Code
- audioserver/*

#### Database setup
- sql/*

#### Database temporary folder/uploads
- var/*

## Reflection Questions/Design Decisions
 - Handle user auth and data security
   - Would need to add another table of users in sql schema, stores usernames and salted + hashed passwords.
     - Could use something like HTTP Basic Access Auth, where user provides username and password in request headers
     - More modern/prevalent option is bearer token
   - Added side effect of allowing users to only see files that they uploaded, could add an 'uploaded by' field to files that references users table
 - Browser UI to interface with API
   - Form to add and upload files, sends post req to /upload on submit
   - page to list files
     - forms/buttons to filter list, would change arguments in request
     - download button next to each item in list, would make request to appropriate download
     - clicking on each file would lead to a file page with metadata about the file and a button to download
   - relatively simple in React
 - Store audio data
   - Stored as files on memory locally, renamed using uuid filenames so no conflicts
   - Sql database maps file names to uuid names, and holds metadata
   - fine for the scale of this project, but would want to store them on the cloud: Amazon S3 filestorage, Google cloud storage for firebase
   - instead of storing uuid filename, could store link to retrieve resource from a cloud provider's storage bucket
 - Data integrity
   - rogue data in the form of non-audio files
     - checked for in upload process, both by tinytag library and file extension check