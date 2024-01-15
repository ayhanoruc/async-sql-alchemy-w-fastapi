

#### FLOW 

1. build & configure the environment

2. install dependencies

3. create fastapi app + index endpoint + run uvicorn for testing

4. define empty endpoints

    ![Alt text](image.png)

5. create database module
    - connect to pgadmin4 -> create a database (e.g. note_app_db)
    - configure your connection strings and related env variables inside .env
    - load your environment variables inside database.py to connect to asyncpg
    - define table schema and its representation when returned inside the models.py 
    - create table by the engine(w/correct connection url) + schema you defined inside create_db, asyncronously.
    - create CRUD operation methods inside crud_operations.py, by async_sessionmaker
    - finally adjust your api endpoints [ parameters, input_schemas(pydantic models), response_models, status_types etc. ]

