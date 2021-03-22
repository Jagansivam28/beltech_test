# Beltech Assignment

* Created a Django App with has 3 REST GET API's.
* GET API: **/getall** - send all data as json.
* GET API: **/search?station=xyz** - send data of station names that match "xyz".
* GET API: **/distance?from=id1&to=id2** - send distance between two given 
  station codes on the same line.
___
###  GET API: **/getall** - send all data as json.
* Returns Data which is stored in a global variable(hash map). This global variable has already converted the data 
into JSON format upon the Django app Initialization.
* **Time complexity = O(1)**
___
### GET API: **/search?station=xyz** - send data of station names that match "xyz".

* Returns Station Data which is stored in a global variable(hash map). This global variable has already converted the data 
into JSON format upon the Django app Initialization.
* **Time complexity = O(1)**
* Since we are preprocessing and  using  a hash map to store the station's data in an optimized way, 
  the key search can be done in O(1)
___
###  GET API: **/distance?from=id1&to=id2** - send distance between two given
param : id1 - from stations code
param : id2 - to stations code
* id1 and id2 should present in same line else api will respond with 400 Error Code
* Station code, and their distance will be stored in hash map 
* Return the distance between the id1 and id2 
* Negative distance denotes the backward direction
* **Time complexity = O(1)**
* Also here. we are preprocessing and  using  a hash map to store the station's data in an optimized way, 
  the key search can be done in O(1)
___

###  Framework
Since we are creating an API based upon a file IO. the backend framework must be robust enough to handle large file sizes and queries. and Django is a robust framework and is Immensely Scalable
```
 django == 3.1.7
 
```
###  Requirements
The following are the requirements for the project,
```
 Python3
 django == 3.1.7
 djangorestframework == 3.12.2
```
___
### Django API end points

* GET api for get all data
    * api : getall/
    *  url : http://localhost:8000/getall
  
* GET API to search for station data
    * api : /search?station=xyz
    *  url : http://localhost:8000/search?station=xyz
    * parameter : station name
  
* GET API to find the distance between two given station codes on the same line.
    * api :  /distance?from=id1&to=id2
    *  url : http://localhost:8000//distance?from=id1&to=id2
    * parameter : from station id and to station id
  
### how to run the django app
* prerequisite : Python3
### Step 1:
Installing dependency for the project fom Python pip
```
pip3 install -r requirements.text
```
###Step 2:
Running Django Application
```
python3 manage.py runserver
```

  










