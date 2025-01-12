# Application de Quiz en Informatique

Une application Python de quiz conçue pour tester vos connaissances en informatique sur différents sujets comme les Mathématiques, Python, Java, C et la Cybersécurité.

---

## Fonctionnalités

- **Système de connexion utilisateur** : Inscription pour les nouveaux utilisateurs et connexion pour les utilisateurs existants.
- **Quiz minuté** : Chaque quiz dure 1 minute, avec des ajustements dynamiques du chronomètre en fonction des réponses correctes/incorrectes.
- **affichage du score** : affichage du score apres chaaque quiz, et le temps pris,ainsi qu'un feedback sur chaque reponse correctes/incorrecte .
- **Historique des scores** : L'application enregistre l'historique des scores, les sujets choisis et le temps pris pour chaque utilisateur.
- **Support multi-sujets** : Ajoutez facilement de nouveaux sujets en créant des fichiers JSON pour les questions.

---

## Installation

1. **Clonez le dépôt GitHub** :
   ```bash
   git clone https://github.com/AkliSara/AP-Exam.git
   cd AP-Exam
   executer le fichier main.py

---
## Comment utiliser l'application 
**Étape 1 : Bienvenue** :
Lorsque vous démarrez l’application, un menu s'affiche :
Welcome to the Computer Science Quiz!
1. Log in
2. Exit
Tapez 1 pour vous connecter ou créer un nouveau compte.
Tapez 2 pour quitter l'application.

**Étape 2 : Connexion/Inscription**:
Enter your username (name or ID): 
//entrer votre username ou id
New user detected. Creating profile.
Set a password: 
Profile created successfully!

et si vous etes un utilisateur deja existant :
Enter your username (name or ID): sara
Welcome, sara!
Enter your password: sss
Login successful!

**Étape 3 : Menu utilisateur**
Après connexion, choisissez une action :
What would you like to do?
1. View history
2. Take a quiz
3. Log out
**1.Voir l’historique** : Si vous choisissez 1, l’application affichera votre historique par exemple :
History of sara:
- Date: 2024-12-30, Subject: C, Score: 6
**2.Prendre un quiz** : Si vous choisissez 2, l’application vous demandera de sélectionner un sujet :
  Choose a subject:
1. Mathematics
2. Python
3. Java
4. C
5. Cybersecurity
Your choice: 4
**Étape 4 : Répondre aux questions**
Une fois un sujet choisi, l’application commence le quiz. Vous avez 1 minute pour répondre aux questions.
Exemple d'exécution d’un quiz :
Question 1: What is the return type of the `main` function in C?
a) void
b) int
c) float
Votre réponse : b
Bonne réponse !

Question 2: Which library is required to use `printf` in C?
a) stdio.h
b) stdlib.h
c) string.h
Votre réponse : c
Mauvaise réponse. La bonne réponse était : a


Lorsque le temps est écoulé :
Time's up!
Quiz terminé. Temps total : 0:59s
Your final score: 1/2
Thank you for participating!

**Étape 5 : Déconnexion**
Si vous choisissez 3 dans le menu utilisateur, vous serez déconnecté et retournerez au menu principal.

Contact
Pour toute question ou suggestion :












