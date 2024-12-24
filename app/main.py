from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

from app.internals.slack_utils import slack_message

app = FastAPI(
    title="Broken API",
    description="This is an API with broken endpoints that need to be fixed",
    version="0.0.1",
    license_info={
        "name": "MIT",
        "identifier": "MIT",
    },
)


@app.exception_handler(500)
def internal_server_error(request, exc):
    slack_message(
        channel=os.environ["SLACK_CHANNEL"], message=f"Internal Server Error: {exc}"
    )
    return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)


@app.get("/healthz", include_in_schema=False)
async def return_ok_status():
    return JSONResponse(content={"status": "All Good!"}, status_code=200)


@app.get("/error")
def error():
    # This will raise a 500 error
    data = {"hello": "world"}
    return datar
