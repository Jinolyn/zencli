# 🧘 ZenCLI — Votre Assistant Personnel Minimaliste en Ligne de Commande

ZenCLI est un assistant en ligne de commande personnalisable, écrit en Python.  
Il vous aide à rester concentré et organisé au quotidien — avec des notes, des tâches, un journal personnel, la météo, l'heure et bien plus.


## ✨ Fonctionnalités

- 📝 Créer et lister vos notes personnelles
- ✅ Gérer votre liste de tâches (to-do)
- 📔 Écrire dans un journal quotidien
- 🌤️ Afficher la météo selon votre ville
- 🕒 Afficher l’heure selon votre format préféré
- ⚙️ Configurer votre nom, votre ville, et vos préférences
- 📁 Stockage local des données au format JSON


## ⚙️ Installation

> Requiert Python 3.9+

```bash
git clone https://github.com/votre-utilisateur/ZenCLI.git
cd ZenCLI
pip install -r requirements.txt
```

Si requirements.txt n'existe pas, installez les dépendances manuellement :
    $ pip install typer rich requests


🚀 Utilisation
Lancez l’assistant CLI :
    $ python3 main.py [commande]


Exemples :
    python3 main.py note add-note "Acheter du pain"
    python3 main.py todo add-task "Nettoyer la maison"
    python3 main.py time get-current-time

