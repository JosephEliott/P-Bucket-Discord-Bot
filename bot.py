# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("Successfully running the bot!\n실행 안료.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("SERVER HELP"))


#채팅청소 기능
@client.event
async def on_message(message):
    if message.content.startswith ("/채팅청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[5:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="!▩! 메시지 삭제 알림 !▩!", description="디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다.".format(amount, message.author), color=0xffb7c4)
            embed.set_footer(text="Bot Made by. 윤뚱뚱 (윤승주) #7508")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다!".format(message.author.mention))


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('NzY0MTA2MDk1NjE0MjMwNTQ5.X4BbQQ.xyFNad2tc4Gooh4RsNqGZYJX-M8')