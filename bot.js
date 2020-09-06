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

//とりあえずコピペhttps://liginc.co.jp/370260