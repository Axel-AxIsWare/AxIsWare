const { Client, GatewayIntentBits } = require('discord.js');

const intents = [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildMessageReactions,
];
const client = new Client({ intents });
const prefix = '!';

client.once('ready', async () => {
    console.log(`Logged in as ${client.user.tag}`);

    const channelId = 'channel id';
    const channel = await client.channels.fetch(channelId);

    if (channel) {
        const embed = {
            title: "Verification",
            description: "React below to verify",
            color: 3447003,
            footer: {
                text: "Verification | Made by Axel"
            }
        };

        const sentMessage = await channel.send({ embeds: [embed] });
        sentMessage.react('✅');
    } else {
        console.error(`Channel with ID ${channelId} not found.`);
    }
});

client.on('messageReactionAdd', async (reaction, user) => {
    if (user.bot) return;

    const roleID = 'role id';
    const guild = client.guilds.cache.get(reaction.message.guild.id);
    const role = guild.roles.cache.get(roleID);

    if (role && reaction.emoji.name === '✅') {
        const member = guild.members.cache.get(user.id);

        if (member) {
            await member.roles.add(role);
        }
    }
});

client.login('token');