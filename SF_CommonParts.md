# SF_CommonParts.blend
This readme breaks down specifics about this file!

There are many minor discrepencies or optimizations in many meshes between machines.
The versions presented here represent a baseline that follows consistent rules.
Because each usage varies feel free to customize away with UV changes, shape tweaks, or decals.

## File Organization
Top level meshes are preconstructed setups that mirror the usage of the parts in game.
The collections are groups of parts used to make the prefabs and shouldn't be used without collapsing down to less objects.
In several places splines or other helpers are used to help us make shapes (prefixed with aaa_), but only meshes can be used in game so convert your splines to meshes before export.
In several places non content, non helper objects exist like the info text or directional light, these are prefixed with zzz_ and can be ignored.

## Belt/Pipe Inputs/Outputs
These are the classic machine input and output meshes.
Some releases of the game have had separate meshes, but they're usually part of the main mesh.
Their origin is placed so you can use the same position for the input/output components in editor.
Unfortunately the exact depth into the machine varies a lot and will need to be customized per machine.

#### BeltConnector_In/Out
Position these 1.00m above the floor of your mesh to match the standard height.
Visual differences between in and out are mostly the arrows and flange details.

##### PipeConnecter_In/Out/Both
Position these 1.75m above the floor of your mesh to match the standard height.
Visual differences between versions are mostly the arrows and flange details.

## Power Connectors
These are the points where your factory is connected to the power network.
Their origin is placed so you can use the same position for the power connector component in editor.
There are three distinct styles based upon the usage and representation in game.

#### PowerConnecter_Plain
These connectors are the plainest and do not use any decals.
Recommended usage is large machines where detail would be wasted like a train station or nuclear plant, or a small machine where extra detail would be too much, like the JumpPads.

#### PowerConnecter_Hazard
These connectors have simple masked hazard decals added up top and a touch of chrome.
Recommended usage is on medium to large machines where the detail can be noticed but is often not directly adjacent to a player like Assemblers or Refineries.

#### PowerConnecter_Detailed
These connectors have the most detail, more chrome, and use both types of decal.
Recommended usage is on small but detailed machines like Smelters and Forges where the detail is close to the player.

## Foot supports
There's no prefab mesh for these because it is not a component based setup. While every machine uses the same design it's a unique shape every time.
Look inside the `Factory Footing Parts` collection, in there you will find meshes you can kit-bash into something specific for your machines' dimensions.
Distance off the ground for these meshes varies from 0.1m to 0.2m.

## Misc
These are other meshes or mesh sets that are useful and common like lights or ladders. More to come.

#### MiniLight
Often found decorating factory machine footing these also show up on the machine itself to provide extra detail.
