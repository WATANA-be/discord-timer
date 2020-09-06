import discord
import datetime

client = discord.Client()
pretime_dict = {}

@client.event
async def on_voice_state_update(before, after):
  print("ボイスチャンネルで変化がありました")

  if((before.voice.self_mute is not after.voice.self_mute) or (before.voice.self_deaf is not after.voice.self_deaf)):
    print("ボイスチャンネルでミュート設定の変更がありました")
    return

  if(before.voice_channel is None):
    pretime_dict[after.name] = datetime.datetime.now()
  else(after.voice_channel is None):
    duration_time = pretime_dict[before.name] - datetime.datetime.now()
    duration_time_adjust = int(duration_time.total_seconds()) * -1

    reply_channel_name = "general"
    reply_channel = [channel for channel in before.server.channels if channel.name == reply_channel_name][0]
    reply_text = after.name + "　が　"+ before.voice_channel.name + "　から抜けました。　通話時間は" + str(duration_time_adjust) +"秒です"

    await client.send_message(reply_channel ,reply_text)

    // discord.js モジュールのインポート
const Discord = require('discord.js');

// Discord Clientのインスタンス作成
const client = new Discord.Client();

// トークンの用意
const token = 'ここにアクセストークン';

// 準備完了イベントのconsole.logで通知黒い画面に出る。
client.on('ready', () => {
    console.log('ready...');
});


// 後でここに追記します。


// Discordへの接続
client.login(token);

client.run("token")#ボットのトークンです
