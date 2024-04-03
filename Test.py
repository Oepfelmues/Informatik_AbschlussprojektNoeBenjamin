# Informatik_AbschlussprojektNoeBenjamin

import gym

# Importiere supermario
import gym_super_mario_bros
# Importiere Joypad wrapper
from nes_py.wrappers import JoypadSpace
# Importieren von bewegungen
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT


# Setup game
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)


# Variable um den restart zu checken
done = True
# Schleife durch jeden Frame des Spiels (um zu später zu scannen)
for step in range(100000): 
    # spiel aufstarten
    if done: 
        # Runde starten
        env.reset()
    # zufällige bewegung ausfüren
    state, reward, done, info = env.step(env.action_space.sample())
    # spiel anzeigen 
    env.render()
# runde beenden
env.close()