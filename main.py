import logging

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


class Image(BaseModel):
    url: str


class Video(BaseModel):
    url: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/image-link/")
def replace_image_link(image: Image):
    """Replace image link with another link"""
    logging.info(f"got new image: {image}")
    return {"link": "https://cdn.pixabay.com/photo/2012/04/23/16/12/click-38743_960_720.png"}


@app.post("/video-link/")
def replace_video_link(video: Video):
    """Replace video link with another link"""
    logging.info(f"got new video: {video}")
    return {"link": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"}
