import os
from re import template

from typing import List
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, BackgroundTasks
from uuid import uuid4
from pathlib import Path

from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates


from schemas import UploadVideo, GetVideo, Message
from models import Video, User
from services import save_video


video_router = APIRouter()
templates = Jinja2Templates(directory='templates')


@video_router.post("/")
async def create_video(
	background_tasks: BackgroundTasks,
	title: str = Form(...), 
	description: str = Form(...), 
	file: UploadFile = File(...)
):
	user = await User.objects.first()
	return await save_video(
		user=user, 
		file=file, title=title, 
		description=description, 
		background_tasks=background_tasks
	)


# @video_router.get("/video/{video_pk}", responses={404: {'model':Message}})
# async def get_video(video_pk: int):
# 	file = await Video.objects.select_related('user').get(pk=video_pk)
# 	file_link = open(file.dict().get('file'), mode='rb')
# 	return StreamingResponse(file_link, media_type='video/mp4')


@video_router.get("/video/{video_pk}", responses={404: {'model':Message}})
def get_video(video_pk: int):
	file_link = open('media/Big_Buck_Bunny_1080_10s_5MB.mp4', mode='rb')
	return StreamingResponse(file_link, media_type='video/mp4')