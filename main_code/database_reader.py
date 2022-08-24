import pygame
from database import get_data
from sound import get_sound

# Imports the data from the database.
path = get_data.get_path().replace('\\', '/')
sound_path = get_sound.get_path().replace('\\', '/')
atomic_number = open(path + '/atomic_number.txt').read().split('\n')
english_names = open(path + '/english_names.txt').read().split('\n')
latin_names = open(path + '/latin_names.txt').read().split('\n')
year_of_discovery = open(path + '/year_of_discovery.txt').read().split('\n')
electron_shell = open(path + '/electron_shell.txt').read().split('\n')
atomic_mass = open(path + '/atomic_mass.txt').read().split('\n')
atomic_density = open(path + '/atomic_density.txt').read().split('\n')
element_group = open(path + '/element_group.txt').read().split('\n')
melting_point = open(path + '/melting_point.txt').read().split('\n')
boiling_point = open(path + '/boiling_point.txt').read().split('\n')
atomic_letters = open(path + '/atomic_letters.txt').read().split('\n')
pygame.init()
wrong_audio = pygame.mixer.Sound(sound_path + "/donald-trump-wrong-sound-effect.wav")
correct_audio = pygame.mixer.Sound(sound_path + "/ding-correct-sound-effect.wav")


def get_path():
    return path


def open_statistics():
    statistics_file_r = open(path + '/statistics.txt')
    return statistics_file_r
