from fastapi import FastAPI, File, UploadFile
import whisper
import uvicorn
import os

app = FastAPI()
model = whisper.load_model("base")  # You can change to tiny, medium, large

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    temp_file = f"/tmp/{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(await file.read())
    result = model.transcribe(temp_file)
    os.remove(temp_file)
    return {"transcript": result["text"]}
