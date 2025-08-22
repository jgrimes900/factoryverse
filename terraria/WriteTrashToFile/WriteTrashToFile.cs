using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Terraria.Utilities;
using Terraria.ModLoader;
using Terraria;
using Terraria.DataStructures;
using System.Drawing.Printing;

namespace WriteTrashToFile
{
	// Please read https://github.com/tModLoader/tModLoader/wiki/Basic-tModLoader-Modding-Guide#mod-skeleton-contents for more information about the various files in a mod.
	public class WriteTrashToFile : Mod
	{
		public static Dictionary<string, int> trashed_items = new Dictionary<string, int>();
		public static void AddToTrashed_Items(string name, int amount){
			
			try {
				trashed_items.Add(name, amount);
			} catch (ArgumentException) {
				trashed_items[name] += amount;
			}

            using (StreamWriter sw = File.AppendText("C://Users//jgrim//Documents//terraria_trash.txt"))
            {
                sw.WriteLine(name + "," + amount);
            }

        }
		public static bool RemoveFromFactorio_Items(string name, int amount){
			if (trashed_items[name] >= amount)
			{
				trashed_items[name] -= amount;
				using (StreamWriter sw = File.AppendText("C://Users//jgrim//Documents//terraria_trash.txt"))
				{
					sw.WriteLine(name + ",-" + amount);
				}
				return true;
			}
			
			return false;
		}

		public static void Load_this(){

            trashed_items = new Dictionary<string, int>();

            using var watcher = new FileSystemWatcher(@"C://Users//jgrim//Documents");

            watcher.NotifyFilter = NotifyFilters.Attributes
                                 | NotifyFilters.CreationTime
                                 | NotifyFilters.DirectoryName
                                 | NotifyFilters.FileName
                                 | NotifyFilters.LastAccess
                                 | NotifyFilters.LastWrite
                                 | NotifyFilters.Security
                                 | NotifyFilters.Size;

            watcher.Changed += OnChanged;

            watcher.Filter = "terraria_trash_update.txt";
            watcher.IncludeSubdirectories = false;
            watcher.EnableRaisingEvents = true;

            using (StreamWriter sw = File.AppendText("C://Users//jgrim//Documents//terraria_trash.txt"))
            {
                sw.WriteLine("SYNC");
            }

        }

        private static void OnChanged(object sender, FileSystemEventArgs e)
        {
            if (e.ChangeType != WatcherChangeTypes.Changed)
            {
                return;
            }

            string read = System.Text.Encoding.ASCII.GetString(FileUtilities.ReadAllBytes("C://Users//jgrim//Documents//terraria_trash_update.txt", false));
            string[] keyvalue = read.Split('\n');
            foreach (string line in keyvalue)
            {
                string[] kv = line.Split(',');
				if (kv.Length == 2)
				{
					try
					{
                        trashed_items.Add(kv[0].ToLower(), Int32.Parse(kv[1]));
					}
					catch (ArgumentException)
					{
                        trashed_items[kv[0].ToLower()] += Int32.Parse(kv[1]);
                    }
				}
            }

        }
	}
	public class WriteTrashToFileUnload : ModSystem 
	{
		public override void OnWorldLoad (){
			WriteTrashToFile.Load_this();
		}
	}

	public class GiveFactorioItem : ModCommand
	{
		public static string UsageText;
		public static string DescriptionText;

		public override void SetStaticDefaults() {
			UsageText = "/take_factorio <name> <amount>\nname - factorio item name\namount - stack size to take";
			DescriptionText = "Takes an item from factorio.";
		}

		// CommandType.Chat means that command can be used in Chat in SP and MP
		public override CommandType Type
			=> CommandType.Chat;

		// The desired text to trigger this command
		public override string Command
			=> "take_factorio";

		// A short usage explanation for this command
		public override string Usage
			=> UsageText;

		// A short description of this command
		public override string Description
			=> DescriptionText;

		public override void Action(CommandCaller caller, string input, string[] args) {
			// Checking input Arguments
			if (args.Length <= 1)
				throw new UsageException("Not enough args.");

            Main.NewText($"Made it to a");

            int.TryParse(args[1], out int amount);
			if (!WriteTrashToFile.RemoveFromFactorio_Items(args[0].Replace("_", " "), amount*10))
				throw new UsageException("Item not avalible.");
			// If we can't parse the int, it means we have a name (or a wrong use of the command)
			// In that case type be equal to 0
				// Replacing the underscore in an element name with spaces
			string name = args[0].Replace("_", " ");


            Main.NewText($"Made it to b");

            // We go through all the subjects to find the required typeId
            // Only if the name of the item matches the desired one in the current localization (no case sensitive) 
            int type = 0;
			for (int k = 1; k < ItemLoader.ItemCount; k++) {
				if (name.ToLower() == Lang.GetItemNameValue(k).ToLower()) {
					type = k;
					break;
				}
			}

            Main.NewText($"Made it to c");

            if (type <= 0 || type >= ItemLoader.ItemCount)
				throw new UsageException("Item not found.");

			Main.NewText($"Made it to d");
            // Spawn the item where the calling player is
            caller.Player.QuickSpawnItem(new EntitySource_DebugCommand("{WriteTrashToFile}_{GiveFactorioItemCommand}"), type, amount);

            Main.NewText($"Made it to e");
        }
	}
	public class load_trash : ModCommand
	{
		public static string UsageText;
		public static string DescriptionText;

		public override void SetStaticDefaults() {
			UsageText = "/load_trash";
			DescriptionText = "load trash.";
		}

		// CommandType.Chat means that command can be used in Chat in SP and MP
		public override CommandType Type
			=> CommandType.Chat;

		// The desired text to trigger this command
		public override string Command
			=> "load_trash";

		// A short usage explanation for this command
		public override string Usage
			=> UsageText;

		// A short description of this command
		public override string Description
			=> DescriptionText;

		public override void Action(CommandCaller caller, string input, string[] args) {
			WriteTrashToFile.Load_this();
		}
	}
}
