# evreka
# Blog-Api
This is a blog api that I made with Python. I use Django Rest Framework as a runtime.
## Build and run
You can run the server with
`
docker-compose up --build -d
`
## Endpoints

### Question-1
-   We have two models named navigation record and vehicle
-   In 'GET' method, the last navigation data from the last 48 hours is returned for each vehicle.
-   method: `GET`
-   path: `"http://localhost:8000/last-points/"`
-   body: 

-   response:
    ```js
    {
    "vehicle": integer,
    "datetime":string,
    "latitude": float,
    "longitude": float
    }
    ```

### Question-2
-   method: `GET`
-   We have three models named Bin, Operation and BinOperation.
-   Bin class has latitude and longitude fields. BinOperation class has collection_frequency and last_collection fields. Endpoint that returns the collection_frequency list for each BinOperation pair
-   path: `http://localhost:8000/collection-frequency/`


