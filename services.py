import os
from uuid import uuid4
import shutil
import aiofiles
from fastapi import UploadFile
from schemas import UploadVideo, GetVideo, Message
from models import Video, User
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, BackgroundTasks

class Video:
	pass


async def save_video(
	background_tasks: BackgroundTasks,
	title: str = Form(...), 
	description: str = Form(...), 
	file: UploadFile = File(...)
):
	# file_name = Path("media", str(user.dict().get('id')), f'{str(uuid4())}.mp4')
	id_user = user.dict().get('id')

	# Временная мера - лучше создавать каталог пользователя при создании пользователя 1 раз (мое решение)
	if not os.path.isdir(f'media/{id_user}'):
		os.mkdir(f'media/{id_user}')

	file_name = f"media/{id_user}/{uuid4()}.mp4"

	if file.content_type == 'video/mp4':
		background_tasks.add_task(write_video, file_name, file)
	else:
		raise HTTPException(status_code=418, detail="Файл не соответствует формату - mp4")

	info = UploadVideo(title=title, description=description)
	user = await User.objects.first()

	return await Video.objects.create(file=file_name, user=user, **info.dict())


def write_video(file_name: str, file: UploadFile):
    # async with aiofiles.open(file_name, "wb") as buffer:
    #     data = await file.read()
    #     await buffer.write(data)
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)