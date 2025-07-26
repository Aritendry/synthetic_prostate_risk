from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

# Chemins fixés par toi
templates = Jinja2Templates(directory=r"C:\Users\ramah\Documents\Projet\synthetic_prostate_risk\web\templates")

model = joblib.load(r"C:\Users\ramah\Documents\Projet\synthetic_prostate_risk\model\model.pkl")
label_encoder = joblib.load(r"C:\Users\ramah\Documents\Projet\synthetic_prostate_risk\model\label_encoder.pkl")

app = FastAPI()

def preprocess_input(
    age: float,
    bmi: float,
    sleep_hours: float,
    smoker: str,
    alcohol: str,
    diet: str,
    physical: str,
    family_history: str,
    mental_stress: str,
    checkup: str,
    prostate_exam: str,
):
    input_dict = {
        'age': age,
        'bmi': bmi,
        'sleep_hours': sleep_hours,
        'smoker_Yes': 1 if smoker == "Yes" else 0,
        'alcohol_consumption_Moderate': 1 if alcohol == "Moderate" else 0,
        'diet_type_Healthy': 1 if diet == "Healthy" else 0,
        'diet_type_Mixed': 1 if diet == "Mixed" else 0,
        'physical_activity_level_Low': 1 if physical == "Low" else 0,
        'physical_activity_level_Moderate': 1 if physical == "Moderate" else 0,
        'family_history_Yes': 1 if family_history == "Yes" else 0,
        'mental_stress_level_Low': 1 if mental_stress == "Low" else 0,
        'mental_stress_level_Medium': 1 if mental_stress == "Medium" else 0,
        'regular_health_checkup_Yes': 1 if checkup == "Yes" else 0,
        'prostate_exam_done_Yes': 1 if prostate_exam == "Yes" else 0,
    }
    X = np.array([list(input_dict.values())])
    return X

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/analyze")
async def analyze_form(request: Request):
    return templates.TemplateResponse("Analyze.html", {"request": request})

@app.post("/analyze")
async def analyze_result(
    request: Request,
    age: float = Form(...),
    bmi: float = Form(...),
    sleep_hours: float = Form(...),
    smoker: str = Form(...),
    alcohol: str = Form(...),
    diet: str = Form(...),
    physical: str = Form(...),
    family_history: str = Form(...),
    mental_stress: str = Form(...),
    checkup: str = Form(...),
    prostate_exam: str = Form(...),
):
    X = preprocess_input(age, bmi, sleep_hours, smoker, alcohol, diet, physical, family_history, mental_stress, checkup, prostate_exam)
    pred_num = model.predict(X)[0]
    pred_label = label_encoder.inverse_transform([pred_num])[0]
    return templates.TemplateResponse("Analyze.html", {"request": request, "result": pred_label})
