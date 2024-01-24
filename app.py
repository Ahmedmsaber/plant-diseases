from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import prediction, getModel

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Load your pre-trained model
# Replace this with your actual model loading code


@app.get("/", response_class=HTMLResponse)
async def home(request: HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        model = getModel()
        test = prediction(model, file.file)
        return {"prediction": str(test)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
