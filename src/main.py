from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from sqlalchemy.orm import Session
from fastapi import Depends
from . import models

app = FastAPI()
openai = OpenAI(api_key="")

CHATGPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class InteractionCreate(BaseModel):
    question: str

async def ask_chatgpt(question: str) -> str:
    messages = [
        {"role": "user",
         "content": question},
    ]
    
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": question},
  ]
)
    reply = completion.choices[0].message.content
    return reply

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/llm/interaction")
async def create_interaction(interaction: InteractionCreate):
    try:
        response_text = await ask_chatgpt(interaction.question)
       
        return {"question": interaction.question, "answer": response_text}
    except HTTPException as e:
        return {"error": e.detail}
    
@app.post("/llm/interaction")
async def create_interaction(interaction: InteractionCreate, db: Session = Depends(get_db)):
    try:
        response_text = await ask_chatgpt(interaction.question)
        db_interaction = models.Interaction(question=interaction.question, answer=response_text)
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)
        return {"question": interaction.question, "answer": response_text}
    except Exception as e:
        return {"error": str(e)}

@app.get("/llm/history")
def read_history(db: Session = Depends(get_db)):
    interactions = db.query(models.Interaction).all()
    return interactions



