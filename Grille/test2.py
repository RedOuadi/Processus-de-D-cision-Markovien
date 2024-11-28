import numpy as np

# Définition des paramètres de la grille
GRID_SIZE = 4
GOAL_STATE = (3, 3)
OBSTACLES = [(1, 1), (2, 2)]
REWARD_GOAL = 10
PENALTY_OBSTACLE = -5
PENALTY_STEP = -1

# Définition des actions possibles : haut, bas, gauche, droite
ACTIONS = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

# Initialisation de la fonction de récompense
def initialize_rewards(grid_size, goal_state, obstacles):
    rewards = np.full((grid_size, grid_size), PENALTY_STEP)
    rewards[goal_state] = REWARD_GOAL
    for obs in obstacles:
        rewards[obs] = PENALTY_OBSTACLE
    return rewards

# Transition vers le prochain état
def get_next_state(state, action):
    next_state = (state[0] + ACTIONS[action][0], state[1] + ACTIONS[action][1])
    if 0 <= next_state[0] < GRID_SIZE and 0 <= next_state[1] < GRID_SIZE:
        return next_state
    return state  # Reste dans la même position si hors de la grille

# Politique aléatoire pour illustration
def random_policy(state, rewards):
    action = np.random.choice(list(ACTIONS.keys()))
    next_state = get_next_state(state, action)
    reward = rewards[next_state]
    return next_state, reward

# Simulation d'un épisode pour l'agent
def run_episode(start_state, rewards, max_steps=10):
    state = start_state
    total_reward = 0
    print(f"État de départ : {state}")

    for step in range(max_steps):
        state, reward = random_policy(state, rewards)
        total_reward += reward
        print(f"Étape {step + 1}: action prise -> nouvel état {state}, récompense {reward}")

        if state == GOAL_STATE:
            print("L'agent a atteint le but!")
            break
        elif state in OBSTACLES:
            print("L'agent a heurté un obstacle!")

    print(f"Récompense totale pour cet épisode: {total_reward}\n")

# Initialisation de la grille de récompenses
rewards = initialize_rewards(GRID_SIZE, GOAL_STATE, OBSTACLES)

# Exécution de plusieurs épisodes
start_state = (0, 0)
for episode in range(5):
    print(f"Épisode {episode + 1}")
    run_episode(start_state, rewards)
