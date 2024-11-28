import numpy as np

# Paramètres du jeu
initial_balance = 100
actions = ["dépenser", "épargner", "investir"]
reward_spend = -10
reward_save = 0
reward_invest_win = 20
reward_invest_lose = -15
prob_invest_win = 0.5  # Probabilité de succès pour l'investissement

# Fonction pour choisir une action aléatoire et calculer la récompense
def choose_action(state):
    action = np.random.choice(actions)
    if action == "dépenser":
        reward = reward_spend
    elif action == "épargner":
        reward = reward_save
    elif action == "investir":
        reward = reward_invest_win if np.random.rand() < prob_invest_win else reward_invest_lose
    return action, reward

# Fonction pour exécuter un épisode
def run_game(initial_balance, max_steps=10):
    balance = initial_balance
    print(f"Balance initiale: {balance}")

    for step in range(max_steps):
        action, reward = choose_action(balance)
        balance += reward
        print(f"Étape {step + 1}: Action -> {action}, Récompense -> {reward}, Nouvelle balance -> {balance}")

        if balance <= 0:
            print("Le joueur est à court d'argent!")
            break

    print(f"Balance finale après {max_steps} étapes: {balance}\n")

# Lancement du jeu pour un épisode
run_game(initial_balance)
