from fastapi import fastapi

app = fastapi()

@app.get("/get_data")
async def get_data():
    return {'body': 'Hello World'}