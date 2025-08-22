
local has_init = false

local write_factorio_trash = function()
	if storage["factorio_trash"] then
		local out = ""
		for k,v in pairs(storage["factorio_trash"]) do
			out = out .. k .. "," .. v .. "\n"
		end
		helpers.write_file("factorio_trash.txt", out)
	end
end
script.on_event(defines.events.on_built_entity, function(event)
	game.print(event.entity.name)
	if event.entity.name == "output-chest" then
		if storage["output-chests"] == nil then storage["output-chests"] = {} end
		table.insert(storage["output-chests"], event.entity)
	end
	if event.entity.name == "input-chest" then
		if storage["input-chests"] == nil then storage["input-chests"] = {} end
		table.insert(storage["input-chests"], event.entity)
	end
end)

script.on_nth_tick(30, function(event)
	local update = {}
	if has_init then
		if storage["factorio_trash"] and storage["output-chests"] then
			for _, out in pairs(storage["output-chests"]) do
				if out.valid then
					local inv = out.get_inventory(defines.inventory.chest)
					for __, item in pairs(inv.get_contents()) do
						if storage["factorio_trash"][item.name] then
							storage["factorio_trash"][item.name] = storage["factorio_trash"][item.name] + item.count
						else
							storage["factorio_trash"][item.name] = item.count
						end
						if update[item.name] then
							update[item.name] = update[item.name] + item.count
						else
							update[item.name] = item.count
						end
					end
					inv.clear()
				end
			end
		end
		if storage["factorio_trash"] and storage["input-chests"] then
			for _, out in pairs(storage["input-chests"]) do
				if out.valid then
					local inv = out.get_inventory(defines.inventory.chest)
					local filter = inv.get_filter(1)
					if filter ~= nil then
						if storage["factorio_trash"][filter.name] > 0 then
							local inserted = inv.insert({name=filter.name, count=storage["factorio_trash"][filter.name]})
							storage["factorio_trash"][filter.name] = storage["factorio_trash"][filter.name] - inserted
							if update[filter.name] then
								update[filter.name] = update[filter.name] - inserted
							else
								update[filter.name] = 0 - inserted
							end
						end
					end
				end
			end
		end
		if update ~= {} then
			local out = ""
			for k,v in pairs(update) do
				out = out .. k .. "," .. v .. "\n"
			end
			helpers.write_file("factorio_trash_update.txt", out)
		end
	end
end)

--script.on_nth_tick(60*60, write_factorio_trash)

--commands.add_command("write_factorio_trash", nil, write_factorio_trash)

commands.add_command("init_factorio_trash", nil, function(command)
	storage["factorio_trash"] = {}
	if command.parameter ~= nil then
		for word in string.gmatch(command.parameter, '([^;]+)') do
			i = 0
			j = ""
			k = 0
			for item in string.gmatch(word, '([^,]+)') do
				if i == 0 then
					j = item
					i = 1
				else
					k = tonumber(item)
					i = 0
				end
			end
			storage["factorio_trash"][j] = k
		end
	end
	has_init = true
end)