# Create a working web server that handles three different types of incoming GET requests.

# A root endpoint (/) that returns a basic welcome dictionary.

# A user endpoint (/users/{user_id}) that extracts the user's ID directly from the URL path.

# A search endpoint (/search) that accepts optional filtering arguments at the end of the URL.

from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI server!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"User_Id": user_id}

@app.get("/search")
def search_items(query : str = None , limit : int = 10):
    return {"Query" : query , "limit" : limit}