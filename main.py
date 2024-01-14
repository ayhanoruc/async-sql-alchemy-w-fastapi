from fastapi import FastAPI

#linkedin account = Ayhanoruc www.linkedin.com/in/ayhan-oruç-601224184
app = FastAPI(
    title="MyNotes API",
    version="1.0.0",
    description="MyNotes API with FastAPI using async database connectors",
    contact={
        "name": "Ayhan Oruc",
        "url": "http://www.linkedin.com/in/ayhan-oruç-601224184",
    }
)




# home route
@app.get("/")
def root():
    return {"message": "OK"}

@app.get("/notes")
def get_all_notes():
    pass 

@app.get("/notes/{note_id}")
def get_note_by_id(note_id):
    pass

@app.post("/notes")
def create_note():
    pass

@app.put("/notes/{note_id}")
def update_note(note_id):
    pass

@app.delete("/notes/{note_id}")
def delete_note(note_id):
    pass



