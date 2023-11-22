import uvicorn
from fastapi import FastAPI

app = FastAPI()

d = {}
file = open("PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)

for line in file:
    data = line.strip().split(";")
    gemeinde = data[3]
    plz = data[1]
    ortschaft = data[0]
    kanton = data[5]
    d[gemeinde] = { "plz": plz,
                "ortschaft": ortschaft,
                "kanton": kanton,
                "gemeinde": gemeinde}
file.close()

#@app.get("/")
#async def root():
   # return{"Version": "1.0"}

@app.get("/search")
async def search(gemeinde: str):
    if gemeinde in d:
        return d[gemeinde]
    else:
        return {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
