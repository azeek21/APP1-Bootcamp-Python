# Testing
Firs of all, run the server by doing
```$ python3 credentials.py``` it'll be listening at port 8888 at localhost.

Then you can go to http://127.0.0.1:8888 to see the result.
You can go to http://127.0.0.1:8888/?species=searchTerm make sure to replace the searchTerm with what you want to get from the database. Have a look at the db.py to see requestable datasets.

Run test.py to for more tests. You can play with urls inside endpoints array for testing purposes.