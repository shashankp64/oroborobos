from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Skeleton FastAPI App")

@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}

@app.get("/status")
def status():
    return {
        "status": "operational",
        "service": "skeleton-api"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=12000)
