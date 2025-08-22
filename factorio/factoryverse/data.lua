local item_sounds = require("__base__.prototypes.item_sounds")
data:extend(
{
	{
    type = "container",
    name = "output-chest",
    icon = "__base__/graphics/icons/wooden-chest.png",
    flags = {"placeable-neutral", "player-creation"},
    minable = {mining_time = 0.1, result = "output-chest"},
    max_health = 100,
    corpse = "wooden-chest-remnants",
    dying_explosion = "wooden-chest-explosion",
    collision_box = {{-0.35, -0.35}, {0.35, 0.35}},
    fast_replaceable_group = "container",
    selection_box = {{-0.5, -0.5}, {0.5, 0.5}},
--    damaged_trigger_effect = hit_effects.entity(),
    inventory_size = 16,
    open_sound = { filename = "__base__/sound/wooden-chest-open.ogg", volume = 0.6 },
    close_sound = { filename = "__base__/sound/wooden-chest-close.ogg", volume = 0.6 },
    impact_category = "wood",
    icon_draw_specification = {scale = 0.7},
    picture =
    {
      layers =
      {
        {
          filename = "__base__/graphics/entity/wooden-chest/wooden-chest.png",
          priority = "extra-high",
          width = 62,
          height = 72,
          shift = util.by_pixel(0.5, -2),
          scale = 0.5
        },
        {
          filename = "__base__/graphics/entity/wooden-chest/wooden-chest-shadow.png",
          priority = "extra-high",
          width = 104,
          height = 40,
          shift = util.by_pixel(10, 6.5),
          draw_as_shadow = true,
          scale = 0.5
        }
      }
    },
    circuit_connector = circuit_connector_definitions["chest"],
    circuit_wire_max_distance = default_circuit_wire_max_distance
  },
  {
    type = "item",
    name = "output-chest",
    icon = "__base__/graphics/icons/wooden-chest.png",
    subgroup = "storage",
    order = "a[items]-a[output-chest]",
    inventory_move_sound = item_sounds.wood_inventory_move,
    pick_sound = item_sounds.wood_inventory_pickup,
    drop_sound = item_sounds.wood_inventory_move,
    place_result = "output-chest",
    stack_size = 50
  },
  {
    type = "recipe",
    name = "output-chest",
    ingredients = {{type = "item", name = "wooden-chest", amount = 1}},
    results = {{type="item", name="output-chest", amount=1}}
  },
  
  {
    type = "container",
    name = "input-chest",
    icon = "__base__/graphics/icons/wooden-chest.png",
    flags = {"placeable-neutral", "player-creation"},
    minable = {mining_time = 0.1, result = "input-chest"},
    max_health = 100,
    corpse = "wooden-chest-remnants",
    dying_explosion = "wooden-chest-explosion",
    collision_box = {{-0.35, -0.35}, {0.35, 0.35}},
    fast_replaceable_group = "container",
    selection_box = {{-0.5, -0.5}, {0.5, 0.5}},
--    damaged_trigger_effect = hit_effects.entity(),
    inventory_size = 16,
    open_sound = { filename = "__base__/sound/wooden-chest-open.ogg", volume = 0.6 },
    close_sound = { filename = "__base__/sound/wooden-chest-close.ogg", volume = 0.6 },
    impact_category = "wood",
    icon_draw_specification = {scale = 0.7},
	inventory_type = "with_filters_and_bar",
    picture =
    {
      layers =
      {
        {
          filename = "__base__/graphics/entity/wooden-chest/wooden-chest.png",
          priority = "extra-high",
          width = 62,
          height = 72,
          shift = util.by_pixel(0.5, -2),
          scale = 0.5
        },
        {
          filename = "__base__/graphics/entity/wooden-chest/wooden-chest-shadow.png",
          priority = "extra-high",
          width = 104,
          height = 40,
          shift = util.by_pixel(10, 6.5),
          draw_as_shadow = true,
          scale = 0.5
        }
      }
    },
    circuit_connector = circuit_connector_definitions["chest"],
    circuit_wire_max_distance = default_circuit_wire_max_distance
  },
  {
    type = "item",
    name = "input-chest",
    icon = "__base__/graphics/icons/wooden-chest.png",
    subgroup = "storage",
    order = "a[items]-a[input-chest]",
    inventory_move_sound = item_sounds.wood_inventory_move,
    pick_sound = item_sounds.wood_inventory_pickup,
    drop_sound = item_sounds.wood_inventory_move,
    place_result = "input-chest",
    stack_size = 50
  },
  {
    type = "recipe",
    name = "input-chest",
    results = {{type="item", name="input-chest", amount=1}},
    ingredients = {{type = "item", name = "wooden-chest", amount = 1}},
  },
})