import requests
import hashlib

def check_auth(user, password):
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/apolito9321/VantXploit2000/main/auth.json",
            timeout=10
        )
        data = r.json()
        pw_hash = hashlib.sha256(password.encode()).hexdigest()
        return user in data.get("users", {}) and data["users"][user] == pw_hash
    except:
        print("[!] Error de conexión (necesitas internet)")
        return False
