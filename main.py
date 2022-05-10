import discord
from messages import Messages


class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.messages = Messages()


    async def on_message(self, message):
        self.file = open("Name.txt", "r", encoding="utf8")
        self.name = self.file.read()
        self.file.close()
        if message.author == self.user:
            return

        if message.content.lower() in ("Привет".lower(), "Здравствуй".lower(), "Hi".lower(), "Hello".lower()):
            answer = f"Здравствуй {self.name}!\nКак тебя зовут?\n(Правила пользования: писать без знаков припинания, если" \
                     " не сказанно обратного, отвечать на вопросы лучше: да или нет, если это не вопросы требующие др" \
                     "угого ответа)"
            await message.channel.send(answer)

        elif message.content.lower() in ("Хорошо".lower(), "Плохо".lower(), "Нормально".lower(), "Пойдёт".lower()):
            answer = "Моё предложение точно будет тебе по вкусу.\nХочешь сыграть?"
            await message.channel.send(answer)

        elif message.content.lower() in ("Да".lower(), "Хочу".lower(), "Давай".lower()):
            answer = "Тогда увидимся, когда я буду готов, а пока, пока!"
            await message.channel.send(answer)

        elif message.content.lower() in ("Нет".lower(), "Не хочу".lower(), "Да нет".lower()):
            answer = "Тогда пока путник\nУдачи!"
            await message.channel.send(answer)

        else:
            answer = "Хорошое имя\nКак дела?"
            await message.channel.send(answer)
            file = open("Name.txt", "w", encoding="utf8")
            file.write(message.content)


TOKEN = "OTY3NzAzMTU0OTMyMjE5OTc0.Gdi9ZN.XQD4iuU5D79XaftIDlu4O7d8kJ3ix6W8Alvxzo"
client = MyClient()
client.run(TOKEN)
