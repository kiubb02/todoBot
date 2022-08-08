import discord
from discord.ext import commands
import tabulate
from keep_alive import keep_alive

# BOT THAT CREATES A TODO MAP BASED ON SUBJECT AND EVERYTJHING

TOKEN = "MTAwNjE0NzQ4NzI3MjI3MTkxMg.GrYIj0.FFMDP9dtveblUVQ91-MGmDyqSdqqOXe3XmyD_8"

client = discord.Client()
bot = commands.Bot(command_prefix="!")

index = 0

# dict object
todoList = [{
    "subject": "ai",
    "tasks": []
}, {
    "subject": "fprog",
    "tasks": []
}, {
    "subject": "inno",
    "tasks": []
}, {
    "subject": "koku",
    "tasks": []
}, {
    "subject": "rw",
    "tasks": []
}, {
    "subject": "swkom",
    "tasks": []
}, {
    "subject": "swqm",
    "tasks": []
}, {
    "subject": "wia",
    "tasks": []
}, {
    "subject": "game",
    "tasks": []
}, {
    "subject": "app",
    "tasks": []
}, {
    "subject": "uf",
    "tasks": []
}]


@bot.command()
async def showall(ctx):
    missing = 0

    for i in todoList:
        if len(i["tasks"]) != 0:
            header = i["tasks"][0].keys()
            rows = [x.values() for x in i["tasks"]]
            subject = i["subject"]
            await ctx.send(f"**Subject: {subject}**\n\n{tabulate.tabulate(rows, header)}")
        else:
            missing += 1
    if missing == 11:
        await ctx.send("No tasks for any subject are open")


@bot.command()
async def jenkins(ctx):
    await ctx.send(
        f"List of subjects available: \n Rechnungswesen => *rw* \n Unternehmensführung => *uf* \n Innovation Lab 3 => *inno* \n Kommunikation und Kultur => *koku* \n Wissenschaftliches Arbeiten => *wia* \n Funktionale Programmierung => *fprog* \n Softwarekomponentensysteme Labor => *swkom* \n Big Data/ CV / NLP => *ai* \n Mixed Reality / C++ / Game und Level Design => *game* \n Cross PLattform / iOS => *app* \n\n\n \n *How to use*: \n Add : !add subject,title,task,due \n Delete: !delete subject,title \n Specific Class Tasks: !show subject"
    )


@bot.command()
async def add(ctx, *, message):
    object = message.split(", ")

    d = next((d for d in todoList if d.get("subject") == object[0]), None)
    i = todoList.index(d)
    todoList[i]["tasks"] += [{
        "title": object[1],
        "task": object[2],
        "due": object[3]
    }]

    await ctx.send(f"{message} was added to list")


@bot.command()
async def delete(ctx, *, message):
    object = message.split(", ")
    d = next((d for d in todoList if d.get("subject") == object[0]), None)
    task = next((e for e in d["tasks"] if e.get("title") == object[1]), None)
    d["tasks"].remove(task)
    await ctx.send(f"{message} was deleted from list")


@bot.command()
async def show(ctx, *, message):
    # sending all the todos from one subject
    d = next((d for d in todoList if d.get("subject") == message), None)

    if len(d["tasks"]) == 0:
        await ctx.send("Subject has no tasks")
    else:
        header = d["tasks"][0].keys()
        rows = [x.values() for x in d["tasks"]]
        await ctx.send(f"**Subject: {message}**\n\n{tabulate.tabulate(rows, header)}")


keep_alive()
bot.run(TOKEN)
