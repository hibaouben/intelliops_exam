import re
def masquer_secrets(texte):
    texte = re.sub(r"(?i)\b(password|passwd|token|secret|api_key)([=:])\S+",
                   r"\1\2[SECRET]", texte)
    return re.sub(r"(?i)\bBearer\s+\S+", "Bearer [SECRET]", texte)