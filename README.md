# Satisfactory Modeling Tools
Community modding tools and utilities specifically for modeling assets intended for Coffee Stain Studios game Satisfactory. Need help? Read the modding docs or ask on discord.

Docs: https://docs.ficsit.app/

Discord: https://discord.gg/xkVJ73E

## License
This content was built from scratch by referencing assets ripped from the game and is ONLY for free use with Satisfactory mods, memes, videos, content, reviews, etc. Any other use (paid or otherwise) is against my and probably the developers desires and will be terminated.

## Setup
1. Blender 2.8 or greater
2. A vertex normal editing plugin, like [Y.A.V.N.E.](https://github.com/fedackb/yavne)
3. Clone or download the repo
4. Setup the material proxies (read below)
5. First time opened in Blender it may ask to run [scripts](https://github.com/DavidHGillen/Satisfactory_ModelingTools/blob/master/BlenderScripts.md), allow them. They're safe 
6. Use the content!

### Setup material proxies
Because Satisfactory uses complex procedural shaders on their meshes and distributing ripped content is illegal we'll need lookalike standins for their materials.
We'll have to see our mesh ingame to preview the final result, but that's pretty standard practice. Just keep your UV stretching/seams low and it'll probably work out.
But for things like decals we'll need to rip a copy of some content from the game as this repo cannot legally host it. It's fine to do for yourself though so follow along.

1. Get [Umodel](https://www.gildor.org/en/projects/umodel) and open it up
2. Browse to the root of your Satisfactory install in Steam or Epic and `Select Folder`
3. Check `Override Game Detection` and set it to UE 4.22
4. Now hit `OK`, this may take a few moments to finish
5. Use the explorer panel to browse and find these two textures
    * `Game > FactoryGame > Buildable > ~Shared > Texture > ColorAtlas_Alb.uasset`
    * `Game > FactoryGame > Buildable > ~Shared > Texture > PanelAtlas_Nor.uasset`
6. We'll need to export these as .TGAs into the place where we downloaded or cloned this repo
7. Once exported our folder should have a new folder called `Game`

Our files use relative paths so this should be it and the content will be as good as it can be.
A third image is part of the download. It has been remade, labeled and given a UV grid for reference, with a plain alternative if preferred.

## Usage
1. Open your new machine/prop in Blender
2. Go to `File > Append` in the top application menu
3. Browse to and double click a file like `SF_CommonParts.blend`
4. Double click `Objects` from the list that comes up
5. Pick an object from the list (If unsure what is what, cancel and [browse the file](https://github.com/DavidHGillen/Satisfactory_ModelingTools/blob/master/SF_CommonParts.md))
6. The content should now import into your file
7. In your file, make sure the new object is selected
8. Find the `Properties` panel and the `Material Properties` tab
9. Swap the materials to your equivalents (or swap other meshes to their materials)

Success you now have properly imported the content. For help getting it into the game and using correct shaders please see the [general modding guidelines](https://docs.ficsit.app/)
