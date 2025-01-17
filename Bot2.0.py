#BOT DE RAREZAS
import discord
from discord.ext import commands
import random
import requests

description = '''This is a basic bot. I just hope it helps.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

# Diccionario para almacenar las URLs y su rareza
animal_images = {
    'duck': [
        {'url': 'https://random-d.uk/api/random', 'rarity': 'common'},
        {'url': 'https://some-rarer-duck-image.com/rare_duck.jpg', 'rarity': 'rare'},
        {'url': 'https://some-epic-duck-image.com/epic_duck.jpg', 'rarity': 'epic'}
    ],
    'dog': [
        {'url': 'https://random.dog/woof.json', 'rarity': 'common'},
        {'url': 'https://some-rarer-dog-image.com/rare_dog.jpg', 'rarity': 'rare'},
        {'url': 'https://some-epic-dog-image.com/epic_dog.jpg', 'rarity': 'epic'}
    ],
    'fox': [
        {'url': 'https://randomfox.ca/floof/', 'rarity': 'common'},
        {'url': 'https://some-rarer-fox-image.com/rare_fox.jpg', 'rarity': 'rare'},
        {'url': 'https://some-epic-fox-image.com/epic_fox.jpg', 'rarity': 'epic'}
    ]
}

# Función para elegir una imagen basada en su rareza
def get_random_image(animal):
    rarity_weights = {'common': 80, 'rare': 15, 'epic': 5}  # Probabilidades en porcentajes
    images = animal_images[animal]
    choices = random.choices(images, weights=[rarity_weights[img['rarity']] for img in images], k=1)
    return choices[0]['url']

@bot.command('animal')
async def animal(ctx, animal_type: str):
    """Devuelve una imagen aleatoria basada en el tipo de animal y su rareza."""
    if animal_type not in animal_images:
        await ctx.send("Animal no soportado. Prueba 'duck', 'dog' o 'fox'.")
        return

    image_url = get_random_image(animal_type)
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----------')

bot.run('token')
