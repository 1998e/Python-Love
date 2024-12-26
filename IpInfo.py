
--//Ip Info With Toekn Ipinfo.io \\--


import requests

def get_ip_info(ip_address, api_token):
    url = f"https://ipinfo.io/{ip_address}?token={api_token}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "Non disponible"),
                "Ville": data.get("city", "Non disponible"),
                "Région": data.get("region", "Non disponible"),
                "Pays": data.get("country", "Non disponible"),
                "Code Postal": data.get("postal", "Non disponible"),
                "Localisation": data.get("loc", "Non disponible"),
                "ISP": data.get("org", "Non disponible"),
                "Hôte": data.get("hostname", "Non disponible"),
            }
        else:
            return {"Erreur": "Impossible Ta fais une erreur bg."}
    except Exception as e:
        return {"Erreur": f"Tu fais quoi frr : {e}"}

def main():
    print("Script d'analyse d'IP")
    api_token = input("Entrez votre token API ipinfo : ").strip()
    ip_address = input("Entrez une adresse IP à analyser : ").strip()
    
    if not api_token:
        print("Token API manquant. Veuillez fournir un jeton valide.")
        return

    info = get_ip_info(ip_address, api_token)

    print("\n=== Informations sur l'adresse IP ===")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
