import discord, os
from discord import app_commands 
from discord.ext import commands

perms = discord.Intents.all()
bot = commands.Bot(command_prefix="-", intents=perms)

@bot.command(name='limpar', help='Limpa uma quantidade específica de mensagens.')
async def limpar(ctx, quantidade: int):
    if ctx.author != ctx.guild.owner:
        await ctx.send("Você não tem permissão para usar este comando.", delete_after=10)
        return

    if quantidade <= 0:
        await ctx.send("A quantidade de mensagens deve ser maior que zero.", delete_after=10)
        return

    deleted = await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f"{len(deleted) - 1} mensagens foram excluídas com sucesso.", delete_after=10)

bot.run("TOKEN DE SEU BOT")