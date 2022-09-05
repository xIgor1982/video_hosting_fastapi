import shutil
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from schemas import UploadVideo, User, GetVideo, Message

video_router = APIRouter()

@video_router.post("/")
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
	with open(f'static/{file.filename}', "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)

	return {"file_name" : file.filename}

@video_router.get("/video", response_model=GetVideo, responses={404: {"model": Message}})
async def get_video():
	user = User(**{'id': 25, 'name': 'Ivan'})
	video = UploadVideo(title='Test', description='Description')
	all_data = {'user':user, 'video':video}
	# return GetVideo(**all_data)
	return JSONResponse(status_code=404, content={'message':'Not found'})