# hvalla-item-roller
> an item roller for Hvalla, a DND/TTRPG style rpg game
> FOR USE BY HVALLA ONLY
 
## What does this do?
Currently, the item roller automatically rolls (rng) items for:
- exploring (Ljosa/Iringard)
- scavenging (Wargrun)
- hunting (Everywhere)
- healing (Everywhere)

This version does not take into account addendum rolls, nor does it currently support items that modify probabilities.
I plan to add taggable items ( --[item] in commands) in the future when they are available to players/ready for release.

## The nitty gritty details
What's in this big mess?

Activity roll commands should be in the form of:
`$[activity] [ID | NAME]  [prey|if hunting] [FG/DEBUFF|optional]`

with `heal`, `explore`, `scavenge`, `hunt` as the `[activity]` more details are listed below:


### Healing
this is pretty universal for all warg, there is only one tag for this.

The command:
> `$heal "ID NAME"` is the base command
> 
> `debuff` is the only tag available for healing. This simply rolls to see if that debuff is removed or not.

### Exploring/Scavenging
Exploring currently only available to `Ljosa` or `Iringard`. Scavenging available in `Wargrun`.

The command:
> `$explore/scavenge "ID NAME"` is the base command
> 
> `fg` is the only tag available for exploring. This tag changes the number of items a player is likely to receive.
> Case does not matter, `fg` or `Fg` or `fG` are all valid syntax.

### Hunting
available to all warg, this is the only activity that has some specific tags to it. The bot does not check for whether
or not the warg is in the right city as that is checked before the items are rolled.

The command:
> `$hunt "ID NAME" [prey]` is the base command
> 
> `fg` changes the number of items a player is likely to receive.
> Case does not matter, `FG` or `Fg` or `fG` are all valid syntax.

**Prey Tags Available**

| CITY | PREY | TAG |
| ---- | ---- | --- |
|LJOSA | Arthro | `arthro`|
|LJOSA | Clipper Ant | `clipperant`|
|LJOSA | Gryllo | `gryllo`|
|WARGRUN | Fjell Goat | `goat`|
|WARGRUN | Elk | `elk`|
|WARGRUN | Deer | `deer`|
|IRINGARD | Caribou | `caribou`|
|IRINGARD | Fox | `fox`|
|IRINGARD | Grunox | `grunox`|

## Example Rolls

|ACTIVITY | ROLL WITH TAGS | ROLL WITHOUT TAGS|
|----------|-----------------------------------|------------------------------ |
|scavenging|`$scavenge "W46 Selby" fg`| `scavenge "W46 Selby"`|
|exploring |`$explore "W46 Selby" fg` |`$explore "W46 Selby"` |
|hunting |`$hunt "W46 Selby" goat fg`|`$hunt "W46 Selby" goat`|
|healing| `$heal "W46 Selby" debuff` | `$heal "W46 Selby"`|

## Discord Bot Help
Help command is: `$help + [command]` which will display parameters of the command


    
