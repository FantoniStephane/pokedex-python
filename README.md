# 🎮 Pokédex Python

> Outil en ligne de commande pour composer une équipe Pokémon à partir de données récupérées en temps réel via l'API PokéAPI.

---

## 🚀 Ce que fait ce programme

- Recherche un Pokémon par son nom via une **API REST publique**
- Affiche une fiche complète : nom, taille, poids, types, statistiques
- Gère les erreurs de saisie (Pokémon introuvable)
- Empêche les doublons dans l'équipe
- Affiche un résumé final de l'équipe constituée

---

## 📦 Technologies utilisées

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

- `requests` — requêtes HTTP vers l'API
- [PokéAPI](https://pokeapi.co/) — API REST publique et gratuite

---

## 🖥️ Exemple de déroulé

```
Bienvenue dans le générateur d'équipe Pokémon.
Votre équipe peut contenir 3 Pokémon.

Nom du Pokémon à rechercher : pikachu

--- Fiche Pokémon ---
Nom      : pikachu
Taille   : 4
Poids    : 60
Types    : electric
PV       : 35
Attaque  : 55
Défense  : 40

Voulez-vous ajouter ce Pokémon à votre équipe ? oui
pikachu a été ajouté à votre équipe.
```

---

## ⚙️ Installation

```bash
# 1. Cloner le repo
git clone https://github.com/FantoniStephane/pokedex-python.git
cd pokedex-python

# 2. Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Installer les dépendances
pip install -r requirements.txt
```

---

## ▶️ Lancement

```bash
# Via Jupyter
jupyter notebook tp_pokedex.ipynb

# Ou directement si tu as un fichier .py
python pokedex.py
```

---

## 📁 Structure du projet

```
pokedex-python/
├── pokedex.py          ← programme principal
├── tp_pokedex.ipynb    ← notebook principal
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎓 Contexte

Projet réalisé dans le cadre de la formation **CD2IA** à la Metz Numeric School.  
Notions mobilisées : requêtes HTTP, JSON, fonctions, boucles, gestion d'erreurs.

---

*Fait avec curiosité et quelques Pokéballs. 🔴⚪*
