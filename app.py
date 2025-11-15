from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AutoComparePro API fonctionne 🚗🔥"}

@app.get("/compare")
def compare(carre):
    # Exemple simple, tu pourras me dire ce que tu veux vraiment comparer
    return {"result": f"Comparaison du véhicule {carre} effectuée"}
