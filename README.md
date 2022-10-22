# Deepgram technical prompt

Build a simple API server to handle user audio projects. Your server should provide endpoints that allow a user to perform the following actions: 

- POST raw audio data and store it. 

Eg: $ curl -X POST --data-binary @myfile.wav 

http://localhost/post 

- GET a list of stored files, GET the content of stored files, and GET metadata of stored files, such as the duration of the audio. The GET endpoint(s) should accept a query parameter that allows the user to filter results. Results should be returned as JSON. 

Eg: $ curl http://localhost/download?name=myfile.wav 

Eg: $ curl http://localhost/list?maxduration=300 

Eg: $ curl http://localhost/info?name=myfile.wav 

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