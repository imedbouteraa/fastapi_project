from pydantic import BaseModel

class OCRResponse(BaseModel):
    prenom: str
    nom: str
    numero_permis: str
    date_naissance: str
    lieu_naissance: str
    date_delivrance: str
    date_expiration: str
    categorie_permis: str
    N_immatriculation: str
    date_de_premiere_immatriculation: str
    nom_et_prenom: str
    marques: str
    version: str
    VIN: str
    modele: str
    Adresse_du_titulaire: str
    nom: str
    prenom: str
    sexe: str
    nationalite: str
    date_de_naissance: str
    lieu_de_naissance:str
    numero_de_document: str
    date_expiration: str
    code: str


