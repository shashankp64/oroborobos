from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from typing import Dict, Any, Optional
from persistence.memory import MemoryStorage

app = FastAPI(title="Skeleton FastAPI App")

# Persistence layer instance
storage = MemoryStorage()

# Dependency to get storage instance
def get_storage():
    return storage

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

@app.post("/data/{key}")
async def save_data(key: str, value: Dict[str, Any], store: MemoryStorage = Depends(get_storage)):
    await store.save(key, value)
    return {"message": f"Data saved for {key}"}

@app.get("/data/{key}")
async def get_data(key: str, store: MemoryStorage = Depends(get_storage)):
    data = await store.get(key)
    if data is None:
        return {"error": "Not found"}, 404
    return data

@app.get("/data")
async def list_data(store: MemoryStorage = Depends(get_storage)):
    return await store.list_all()

@app.delete("/data/{key}")
async def delete_data(key: str, store: MemoryStorage = Depends(get_storage)):
    deleted = await store.delete(key)
    if not deleted:
        return {"error": "Not found"}, 404
    return {"message": f"Data deleted for {key}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=12000)
