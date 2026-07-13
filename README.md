# 🔴 Pokédex — Générateur d'équipe Pokémon

<p align="center">
  <img src="images/pokedex_logo.webp" alt="Pokédex" width="400">
</p>

Application Python en ligne de commande permettant de rechercher des Pokémon via l'**API publique PokéAPI**, d'afficher leurs caractéristiques et de constituer une mini-équipe.

Projet réalisé dans le cadre de la formation **CD2IA** à Metz Numeric School — TP Python.

---

## 🎯 Fonctionnalités

- 🔍 Recherche d'un Pokémon par son nom via l'API PokéAPI
- 📇 Affichage d'une fiche détaillée (nom, taille, poids, types, statistiques)
- 👥 Construction d'une équipe de **3 Pokémon** maximum
- 🚫 Gestion des doublons (un Pokémon ne peut pas être ajouté deux fois)
- ⚠️ Gestion des erreurs (Pokémon introuvable → code HTTP 404)
- 📋 Affichage du résumé final de l'équipe

---

## 🛠️ Stack technique

- **Python 3.12**
- **requests** — appels HTTP à l'API PokéAPI
- **API** : [PokéAPI](https://pokeapi.co/) — API publique et gratuite

---

## 🌐 API utilisée

```
https://pokeapi.co/api/v2/pokemon/{nom}
```

Exemple : `https://pokeapi.co/api/v2/pokemon/pikachu`

---

## 🚀 Installation

```powershell
# Cloner le repo
git clone https://github.com/FantoniStephane/pokedex-python.git
cd pokedex-python

# Créer et activer le venv
python -m venv venv
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

---

## ▶️ Utilisation

```powershell
python pokedex.py
```

Exemple d'exécution :

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

Ajouter à l'équipe ? (o/n) : o
Pokémon ajouté à l'équipe.

...

=== Équipe finale ===
1. pikachu
   Types   : electric
   PV : 35 | Attaque : 55 | Défense : 40

2. charizard
   Types   : fire, flying
   PV : 78 | Attaque : 84 | Défense : 78

3. bulbasaur
   Types   : grass, poison
   PV : 45 | Attaque : 49 | Défense : 49
```

---

## 📁 Structure

```
pokedex-python/
├── pokedex.py         # Programme principal
├── pokedex.ipynb      # Version notebook (sujet + expérimentation)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💡 Notions mobilisées

- Appels HTTP avec `requests`
- Manipulation de données JSON
- Gestion des codes de réponse HTTP (200, 404)
- Fonctions et séparation des responsabilités
- Structures de contrôle (boucles, conditions)
- Manipulation de listes (équipe)

---

## 👤 Auteur

**Stéphane FANTONI**
Formation CD2IA — Metz Numeric School
Titre visé : Concepteur Développeur d'Applications - Niveau 6

🔗 [GitHub](https://github.com/FantoniStephane)

---

*Sujet du TP : Nicolas NUNGE — Metz Numeric School*
