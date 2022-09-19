# Importando as bibliotecas necessárias.
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'audios')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')

# Dados gerais do jogo.
WIDTH = 1024 
HEIGHT = 768 
FPS = 60 # Frames por segundo

# Dados gerais do jogo.
MOTO_WIDTH = 70
MOTO_HEIGHT = 70
GETREADY_WIDTH = 300
GETREADY_HEIGHT = 400

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define estados possíveis do jogador
INIT = 0
ESCOLHA = 1
GAME = 2
QUIT = 3