from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/image-link/{link}")
def replace_image_link(link: str):
    return {"link": "https://cdn.pixabay.com/photo/2012/04/23/16/12/click-38743_960_720.png"}


@app.get("/video-link/{link}")
def replace_video_link(link: str):
    return {"link": "//samplelib.com/lib/preview/mp4/sample-5s.mp4"}
