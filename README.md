# hvalla-item-roller
> an item roller for Hvalla, a DND/TTRPG style rpg game
> This repo doesn't contain the tables required for the activities and may not be the final version that is deployed.
> Regardless, this is README does contain the relevant command and tag information for the bot
 
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
`$roll [ID | NAME] --[activity] --[prey|optional] --[FG/DEBUFF|optional]`

with `healing`, `exploring`, `scavenging`, `hunting` as the `[activity]` more details are listed below:


### Healing
this is pretty universal for all warg, there is only one tag for this.

The command:
> `$roll [ID | NAME] --healing` is the base command
> 
> `--DEBUFF` is the only tag available for healing. This simply rolls to see if that debuff is removed or not.

### Exploring/Scavenging
Currently only available to `Ljosa` or `Iringard`.

The command:
> `$roll [ID | NAME] --exploring/scavenging` is the base command
> 
> `--FG` is the only tag available for exploring. This tag changes the number of items a player is likely to receive.
> Case does not matter, `--fg` or `--Fg` or `--fG` are all valid syntax.

### Hunting
available to all warg, this is the only activity that has some specific tags to it. The bot does not check for whether
or not the warg is in the right city as that is checked before the items are rolled.

The command:
> `$roll [ID | NAME] --hunting --[prey]` is the base command
> 
> `--FG` changes the number of items a player is likely to receive.
> Case does not matter, `--fg` or `--Fg` or `--fG` are all valid syntax.

**Prey Tags Available**

| CITY | PREY | TAG |
| ---- | ---- | --- |
|LJOSA | Arthro | `--arthro`|
|LJOSA | Clipper Ant | `--clipper ant`|
|LJOSA | Gryllo | `--gryllo`|
|WARGRUN | Fjell Goat | `--goat`|
|WARGRUN | Elk | `--elk`|
|WARGRUN | Deer | `--deer`|
|IRINGARD | Caribou | `--caribou`|
|IRINGARD | Fox | `--fox`|
|IRINGARD | Grunox | `--grunox`|

### Example Rolls

|ACTIVITY | ROLL WITH TAGS | ROLL WITHOUT TAGS|
|----------|-----------------------------------|------------------------------ |
|scavenging|`$roll W46 Selby --scavenging --FG`| `$roll W46 Selby --scavenging`|
|exploring |`$roll W46 Selby --exploring --FG` |`$roll W46 Selby --exploring` |
|hunting |`$roll W46 Selby --hunting --goat --FG`|`$roll W46 Selby --hunting`|
|healing| `$roll W46 Selby --healing --DEBUFF` | `$roll W46 Selby --healing`|

## Discord Bot Help
Help command is: `$help`


    
