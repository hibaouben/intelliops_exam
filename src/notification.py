CANAUX = {"CRITICAL": "TEAMS", "HIGH": "TEAMS", "MEDIUM": "EMAIL", "LOW": "DASHBOARD"}
def choisir_canal(criticite):
    if criticite not in CANAUX:
        raise ValueError(f"criticité inconnue : {criticite}")
    return CANAUX[criticite]
def demander_validation(sensible, reponse):
    if not sensible:
        return True
    return reponse.strip().lower() in ("o", "oui", "y", "yes")