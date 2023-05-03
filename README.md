# Satisfactory Modeling Tools
Community modding tools and utilities specifically for modeling assets intended for Coffee Stain Studios game Satisfactory. Need help? Read the modding docs or ask on discord.

Docs: https://docs.ficsit.app/

Discord: https://discord.gg/xkVJ73E

Please browse the files in the repo as many may be useful to you.

## License
This content was built from scratch by referencing assets ripped from the game and is ONLY for free use with Satisfactory mods, memes, videos, content, reviews, etc. Any other use (paid or otherwise) is against my and probably the developers desires and will be terminated.

## Blender Setup
1. Install Blender 2.8 or greater (Steam has it)
2. Clone, or download, the repo onto your computer
3. Setup any of the additional systems as listed below!
4. Find the .blend files in the root folder. If unsure try `SF_CommonParts.blend`
5. First time opened in Blender it may ask to run [scripts](https://github.com/DavidHGillen/Satisfactory_ModelingTools/blob/master/BlenderScripts.md), allow them. They're safe
6. Use the content!

## Blender Usage
1. Open your new machine/prop in Blender
2. Go to `File > Append` in the top application menu
3. Browse to and double click a file like `SF_CommonParts.blend`
4. Double click `Objects` from the list that comes up
5. Pick an object from the list (If unsure what is what, cancel and [browse the file](https://github.com/DavidHGillen/Satisfactory_ModelingTools/blob/master/SF_CommonParts.md))
6. The content should now import into your file
7. In your file, make sure the new object is selected
8. Find the `Properties` panel and the `Material Properties` tab
9. To streamline importing swap the materials to a single set. No need to have any of them more than once

Success you now have properly imported the content. For help getting it into the game and using correct shaders please see the [general modding guidelines](https://docs.ficsit.app/)

## Advanced setup
Because Satisfactory uses complex procedural shaders on their meshes and distributing ripped content is illegal we'll need to manage with lookalikes and stand-ins for their materials and textures.
We'll have to see our mesh in-game to preview the final result, but that's pretty standard practice for advanced setups.
Just keep your UV stretching low and avoid obvious seams, then it'll probably work out.
Below are some instructions for more specific setups to make this is as good as we can.
Most assume you know how to rip content so let's cover it here, ripping for personal use is legal, just avoid distributing what you rip, just like me not giving you these texture files.

1. Get [Umodel](https://www.gildor.org/en/projects/umodel) and open it up
2. Browse to the root of your Satisfactory install in Steam or Epic and `Select Folder`
3. Check `Override Game Detection` and set it to UE 4.26
4. Now hit `OK`, this may take a few moments to finish
5. Browse through the folders to find whatever asset you're interested in. If you know it's name `Flat View` can get you to it much quicker

### Setup decal material proxies for Blender
Meshes are coated in decals to add detail the repeating textures can't manage.
The blender file has a spot where it knows to look for them, so let's export them there.

1. We need to boot up UModel to rip two assets
2. Use the explorer panel and find these two textures
    * `Game > FactoryGame > Buildable > ~Shared > Texture > ColorAtlas_Alb.uasset`
    * `Game > FactoryGame > Buildable > ~Shared > Texture > PanelAtlas_Nor.uasset`
3. Export these as .TGAs, place them directly into the root folder for this project
4. Once the export is done the root should have a new folder called `Game` and matching sub folders to the paths above
5. Reopen the blender files and it should show the decals textures now. Unfortunately it's not setup to actually show the normal only decals as just normals.

Our files use relative paths so this should be it and the content will be as good as it can be.
A third image is part of the download. It has been remade, labelled and given a UV grid for reference, with a plain alternative if preferred.

### Setup Substance Designer .sbar of factory metals
Not everything can use FactoryBase and sometimes we need to reluctantly paint unique Textures.
But we still want them to look like the materials the game uses, we're going to rip some content from the game and then configure Substance to use it

1. Boot up UModel and rip the following folder, you can right click and export the whole folder all at once
    * `Game > FactoryGame > Buildable > ~Shared > Material > Resources`
2. The output location doesn't matter