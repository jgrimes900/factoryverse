using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using WriteTrashToFile;

namespace WriteTrashToFile.Content.Items
{ 
	// This is a basic item template.
	// Please see tModLoader's ExampleMod for every other example:
	// https://github.com/tModLoader/tModLoader/tree/stable/ExampleMod
	public class itemHook : GlobalItem
	{
		// The Display Name and Tooltip of this item can be edited in the 'Localization/en-US_Mods.WriteTrashToFile.hjson' file.
		public override void UpdateInventory(Item item, Player ply)
		{
			if (ply.trashItem.stack != 0){
				WriteTrashToFile.AddToTrashed_Items(ply.trashItem.Name,ply.trashItem.stack);
				ply.trashItem.TurnToAir();
			}
		}
	}
}
