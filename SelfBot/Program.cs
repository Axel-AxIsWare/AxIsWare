using System;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;

class Program
{
    private static DiscordSocketClient _client;
    private static ulong _guildId;
    private static ulong _channelId;

    static async Task Main(string[] args)
    {
        PrintAsciiArt();

        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("Enter your bot token: ");
        string token = Console.ReadLine();

        _client = new DiscordSocketClient();
        _client.Log += Log;

        await _client.LoginAsync(TokenType.Bot, token);
        await _client.StartAsync();

        _client.Ready += OnReady;
        _client.MessageReceived += OnMessageReceived;

        await Task.Delay(-1);
    }

    private static void PrintAsciiArt()
    {
        Console.ForegroundColor = ConsoleColor.Magenta;
        Console.WriteLine(@"
   _____         .___        
  /  _  \ ___  __|   | ______
 /  /_\  \\  \/  /   |/  ___/
/    |    \>    <|   |\___ \ 
\____|__  /__/\_ \___/____  >
        \/      \/        \/");
    }

    private static Task Log(LogMessage arg)
    {
        Console.WriteLine(arg);
        return Task.CompletedTask;
    }

    private static async Task OnReady()
    {
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Bot connected!");

        await SetGuildAndChannel();
        await InputLoop();
    }

    private static async Task SetGuildAndChannel()
    {
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.Write("Enter Guild ID and Channel ID (e.g., 123456789012345678 123456789012345678): ");
        string input = Console.ReadLine();

        string[] ids = input.Split(' ');

        if (ids.Length == 2 && ulong.TryParse(ids[0], out _guildId) && ulong.TryParse(ids[1], out _channelId))
        {
            Console.WriteLine($"Set channel to {_guildId}/{_channelId}.");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter valid Guild ID and Channel ID.");
            await SetGuildAndChannel();
        }
    }

    private static async Task InputLoop()
    {
        while (true)
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Write("Enter message to send: ");
            string input = Console.ReadLine();

            await SendMessage(input);
        }
    }

    private static async Task SendMessage(string message)
    {
        if (_guildId == 0 || _channelId == 0)
        {
            Console.WriteLine("Guild ID or Channel ID not set. Please use '?change' to set them.");
            return;
        }

        var channel = _client.GetGuild(_guildId)?.GetTextChannel(_channelId);
        if (channel == null)
        {
            Console.WriteLine($"Guild or channel not found. Please enter valid Guild ID and Channel ID.");
            return;
        }

        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine($"Sending message to {_guildId}/{_channelId}: {message}");

        await channel.SendMessageAsync(message);
    }

    private static Task OnMessageReceived(SocketMessage arg)
    {
        if (arg.Content.Equals("?change", StringComparison.OrdinalIgnoreCase))
        {
            SetGuildAndChannel().Wait();
        }

        return Task.CompletedTask;
    }
}
