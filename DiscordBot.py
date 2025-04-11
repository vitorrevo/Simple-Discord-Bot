from discord.ext import commands
bot = commands.Bot(command_prefix='!')

def main():
    # Bot está em execução
    print("Bot está funcionando.")

if __name__ == "__main__":
    bot.run('TOKEN')
