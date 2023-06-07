# SF_CommonParts.blend
This readme breaks down specifics about this file!

There are many minor discrepancies or optimizations in many meshes between machines.
They shouldn't be noticeable to anyone who doesn't know what to look for so don't worry about not matching the vanilla game.
The versions presented here represent a baseline that follows consistent rules.
Because each usage varies, feel free to customize away with UV changes, shape tweaks, or decals.

## File Organization
Top level meshes are preassembled setups that mirror the usage of the parts in game.
The collections are groups of parts used to make the prefabs and shouldn't be used without collapsing down to less objects.
In several places splines or other helpers are used to help us make shapes (prefixed with aaa_), but only meshes can be used in game so convert your splines to meshes before export.
In several places non content, non helper objects exist like the info text or directional light, these are prefixed with zzz_ and can be ignored.

## Materials
There are 4 pinned materials with Fake Users in the file.
All 4 are tied to a specific common material in the game

### Decal_Normal/Decal_Masked
These are the two decal material used with floating geometry to add more detail to meshes.

### MI_FactoryMachine
Standard machine texture to be used with most models.
Aim for the same texel density as my example pieces when possible.
Check the https://docs.ficsit.app/satisfactory-modding/latest/Development/Modeling/MainMaterials.html for more info.

### MI_FactoryBaked
Used with a machine that has some kind of unique textured unwrap and bake.
This gets expensive the more machines do it so try to avoid it.
Check the https://docs.ficsit.app/satisfactory-modding/latest/Development/Modeling/MainMaterials.html for more info.

## Belt/Pipe Inputs/Outputs
These are the classic machine input and output meshes.
Some releases of the game have had separate meshes, but they're usually part of the main mesh.
Their origin is placed so you can use the same position for the input/output components in editor.
Unfortunately the exact depth into the machine varies a lot and will need to be customized per machine.
There is also a non vanilla sample of a unique way to merge inputs with the "doubly" variant.

#### FactoryBelt_In/Out
Position these 1.00m above the floor of your mesh to match the standard height.
Visual differences between in and out are mostly the arrows and flange details.

##### FactoryPipe_In/Out/Both
Position these 1.75m above the floor of your mesh to match the standard height.
Visual differences between versions are mostly the arrows and flange details.

##### Extendo Variants
Uniquely named, the Extendo variants are a thought experiment and a common request to allow for more closely packed inputs and outputs on machines.
They do not exist in the vanilla game and are an invention of this repo.
When using them be sure to "join" all the objects into one, and then "merge by distance".
This will remove the vertices I had to duplicate to make the individual parts.

## Power Connectors
These are the points where your factory is connected to the power network.
Their origin is placed so you can use the same position for the power connector component in editor.
There are three distinct styles based upon the usage and representation in game.

Note: Both pipeline pump mk1 & mk2 re-use the Wall PowerPole mk1 mesh. They do not include it in their base mesh.

#### PowerConnecter_Plain
These connectors are the plainest and do not use any decals.
Recommended usage is large machines where detail would be wasted like a train station or nuclear plant, or a small machine where extra detail would be too much.

#### PowerConnecter_Hazard
These connectors have simple masked hazard decals added up top and a touch of chrome.
Recommended usage is on medium to large machines where the detail can be noticed but is often not directly adjacent to a player like Assemblers or Refineries.

#### PowerConnecter_Detailed
These connectors have the most detail, more chrome, and use both types of decal.
Recommended usage is on small but detailed machines like Smelters and Forges where the detail is close to the player.

#### PowerConnecter_Compact
These connectors are similar to Plain but are designed for a much more low lying and compact frame.
Recommended usage is on low lying surfaces or props that the Plain variant feels to big on like JumpPads.

## Walkway parts
Many machines have dedicated walkable sections and a variety of ladders placed around them. Both types of walkway floor are decal based and need manual tiling and the ladders are unique lengths every time. As such there's several part collections and few preassembled pieces.

### Walkway_Deflector
These prefabs represent some common sizes of the angle deflection panels that are on the undersides of walkways. Small, Medium, and Large show different and common ways to assemble the pieces found in the `Deflector Parts` collection. These origins are designed to snap to the middle of the outside edge of a walkway.

### Ladder/Walkway Parts
This collection contains two samples of walkway surfaces and some modifier based ladder pieces.

Do not duplicate the Samples and instead use their sizes and uv mapping as a guideline for your own walkway. There is no standardization of walkway sizes or implementations.

When resizing the ladder be sure to adjust the array modifier on the rungs, and resize the uv's on the side supports when you stretcch or shorten it.

## Footing Supports
There's no prefab mesh for these because it is not a component based setup. While every machine uses the same design it's a unique shape every time.
Look inside the `Footing Parts` collection, in there you will find meshes you can kit-bash into something specific for your machines' dimensions.
Distance off the ground for these meshes varies from 0.1m to 0.2m.

## Lights
These are a collection of common light designs found on several machines.

#### LightCage_Simple
Common cagelight variant, often seen over belt inputs on machines.

#### LightCage_SimpleClamp
Semi-common cagelight accessory, used to mount it to thinner rails for general light.

#### LightCage_Rotatable
Semi-common cagelight variant, often mounted under a walkway but still aimed at a belt.

#### LightCage_Detailed
Rare cagelight variant, mainly seen on walls over doors.

#### LightDualPot
Dual pot lights mounted in a frame using the secondary colour. Added to decorate flat surfacces.

#### LightFramed
Flat light with an ornate black cage. Best used as a pop of detail on a larger machine.

#### LightMini
Often found decorating factory machine footing these also show up on the machine itself to provide extra detail.

#### LightSmall
Larger and darker cousion to the mini light, feel free to resize both of these meshes.
