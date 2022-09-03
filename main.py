import shutil
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/")
async def root(file: UploadFile = File(...)):
	with open(f'static/{file.filename}', "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)

	return {"file_name" : file.filename}