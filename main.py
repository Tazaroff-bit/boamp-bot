# main.py

import time
from boamp_client import search_boamp
from notifier import send_telegram
from config import CHECK_INTERVAL

sent_ids = set()

def format_message(a):
    titre = a.get("objet", "Sans titre")
    reference = a.get("id", "N/A")
    lien = a.get("url", "")

    return (
        f"📌 <b>Nouveau marché détecté (BOAMP)</b>

"
        f"<b>Titre :</b> {titre}
"
        f"<b>Référence :</b> {reference}
"
        f"<b>Lien :</b> {lien}"
    )

def run():
    print("Démarrage du bot BOAMP…")

    while True:
        annonces = search_boamp()

        for a in annonces:
            annonce_id = a.get("id")

            if annonce_id not in sent_ids:
                msg = format_message(a)
                send_telegram(msg)
                sent_ids.add(annonce_id)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run()

