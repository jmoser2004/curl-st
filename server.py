import os
import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import Response, PlainTextResponse, FileResponse
import uvicorn

server = FastAPI(title="curl-st", default_response_class=PlainTextResponse)

@server.get("/")
def root():
    return """
    Server is up and an internet connection exists.

    To test ping:

        curl -o /dev/null -w "%{time_connect}\\n" http://curl-st.fyi/ | awk '{printf "Ping: %.2f ms\\n", $1 * 1000}'

    To test for download speed:

        curl -o /dev/null -w "%{speed_download}\\n" http://curl-st.fyi/download | awk '{printf "Download: %.2f Mbps\\n", $1 * 8 / 1000000}'

    To test for upload speed:

        dd if=/dev/zero bs=1M count=10 2>/dev/null | curl -X POST --data-binary @- -o /dev/null -w "%{speed_upload}\\n" http://curl-st.fyi/upload | awk '{printf "Upload: %.2f Mbps\\n", $1 * 8 / 1000000}'

    To download a quick script that tests for both:

        curl -O http://curl-st.fyi/speedtest.sh
        chmod +x speedtest.sh
        ./speedtest.sh

    Created by Joe Moser.

"""

@server.get("/download")
def download():
    return FileResponse("dummy_data/dummy_gig.bin", media_type="application/octet-stream")

@server.get("/speedtest.sh")
def download_script():
    return FileResponse("script/speedtest_v1.sh", filename="speedtest.sh")

@server.post("/upload")
async def upload(request: Request):
    async for _ in request.stream():
        pass
    return "OK\n"

if __name__ == "__main__":
    uvicorn.run("server:server", host="0.0.0.0", port=80, reload=True)