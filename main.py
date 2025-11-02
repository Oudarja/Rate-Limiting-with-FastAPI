from fastapi import FastAPI , Request

from rate_limiter import rate_limited


app=FastAPI()


@app.get("/")
@rate_limited(max_calls=10,time_frame=60)

async def read_root(request:Request):
    return {"message": "Hello world"}

@app.get("/test")
@rate_limited(max_calls=5,time_frame=30)
async def test_route(request:Request):
    return {"message":"This is another endpoint with it's own limit"}
