import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from schemas import UploadVideo, User, GetVideo, Message

video_router = APIRouter()

@video_router.post("/")
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
	with open(f'static/{file.filename}', "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)

	return {"file_name" : file.filename}


@video_router.post("/img", status_code=201)
async def upload_image(files: List[UploadFile] = File(...)):
	for img in files:
		with open(img.filename, "wb") as buffer:
			shutil.copyfileobj(img.file, buffer)
	
	return {"file_name" : "Good"}


@video_router.get("/video", response_model=GetVideo, responses={404: {"model": Message}})
async def get_video():
	user = User(**{'id': 25, 'name': 'Ivan'})
	video = UploadVideo(title='Test', description='Description')
	all_data = {'user':user, 'video':video}
	info = GetVideo(**all_data)
	# return GetVideo(**all_data)
	# return JSONResponse(status_code=404, content={'message':'Not found'})
	return JSONResponse(status_code=200, content=info.dict())


@video_router.get("/test")
async def get_test(req: Request):
	print(req.base_url)
	return {}