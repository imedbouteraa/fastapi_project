import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from paddleocr import PaddleOCR
from serializers import OCRResponse
import cv2
import numpy as np

router = APIRouter()

# Create the media directory if it doesn't exist
media_root = "media"
if not os.path.exists(media_root):
    os.makedirs(media_root)

# Utility function to save uploaded files
def save_uploaded_file(uploaded_file: UploadFile) -> str:
    image_path = os.path.join(media_root, uploaded_file.filename)
    with open(image_path, "wb+") as destination:
        for chunk in iter(lambda: uploaded_file.file.read(1024 * 1024), b""):
            destination.write(chunk)
    return image_path

# Utility function to initialize the OCR module
def initialize_ocr(lang: str = 'fr'):
    return PaddleOCR(
        lang=lang,
        use_angle_cls=True,  # Enable angle classifier
    )

@router.post("/ocr/driver_license/", response_model=OCRResponse)
async def ocr_driver_license(image: UploadFile = File(...)):
    image_path = save_uploaded_file(image)

    ocr_module = initialize_ocr(lang='fr')
    result = ocr_module.ocr(image_path)

    text = [line[1][0] for line in result[0]]

    if len(text) < 13:
        raise HTTPException(status_code=400, detail="OCR extraction failed. Please provide a clearer image.")

    data = {
        'prenom': text[3][2:],
        'nom': text[4][2:],
        'numero_permis': text[9][2:],
        'date_naissance': text[5][2:12],
        'lieu_naissance': text[5][12:],
        'date_delivrance': text[6][3:],
        'date_expiration': text[11],
        'categorie_permis': text[12][2:],
    }

    return JSONResponse(content=data)

@router.post("/ocr/carte_crise/", response_model=OCRResponse)
async def ocr_carte_crise(image: UploadFile = File(...)):
    image_path = save_uploaded_file(image)

    ocr_module = initialize_ocr(lang='fr')
    result = ocr_module.ocr(image_path)

    text = [line[1][0] for line in result[0]]

    data = {
        'N_immatriculation': text[3][2:],
        'date_de_premiere_immatriculation': text[5][1:],
        'nom_et_prenom': text[7][4:],
        'marques': text[14][3:],
        'version': text[15][3:],
        'VIN': text[16][4:],
        'modele': text[19],
        'Adresse_du_titulaire': text[11] + ' ' + text[12] + ' ' + text[13]
    }

    return JSONResponse(content=data)

@router.post("/ocr/idcard/", response_model=OCRResponse)
async def ocr_idcard(image: UploadFile = File(...)):
    image_path = save_uploaded_file(image)

    ocr_module = initialize_ocr(lang='fr')
    result = ocr_module.ocr(image_path)

    text = [line[1][0] for line in result[0]]

    data = {
        "nom": text[4],
        "prenom": text[7],
        "sexe": text[10],
        "nationalite": text[11],
        "date_de_naissance": text[12],
        "lieu_de_naissance": text[14],
        "numero_de_document": text[19],
        "date_expiration": text[20],
        "code": text[-1]
    }

    return JSONResponse(content=data)
