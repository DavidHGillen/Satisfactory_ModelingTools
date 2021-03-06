# Satisfactory Blender Scripts
Readme for [the blender script](https://github.com/DavidHGillen/Satisfactory_ModelingTools/blob/master/SFTools_Blender.py)

## Installing the script
If you're working in SF_CommonParts it's already installed, if you have another blend file, it's simple to hook up.

1. Download the latest version of the repo or just the python file
2. Open your blender file
3. Switch a view to the TextEditor
4. In the top center click `Open`
5. Find to the `BlenderScripts.py` you downloaded
6. Now, left of the Open button click `Text > Register`
7. Agree if it warns you about running the script
8. When the script ever updates go back to the TextEditor and reload the file

Now the tool is installed and will run whenever you start your blender file.
It may warn you about scripts the first time after that, but I promise its safe.

### Updating the script
Changes to the python file do not automatically reload into the blender file. Once you've downloaded the latest there's an extra step.

1. Switch a view to the TextEditor
2. Select `BlenderScripts.py` from the dropdown at the top
3. Now, on the drop down's left `Text > Reload`

If it needs reloading there will open be red warnings telling you as such on the script page. But reloading won't break anything.

## Using the tools
In the top right of the 3D view is a hidden panel, open it with `n` or the little arrow `<`
The vertical list of panels should contain `SFTools` click on that to open up the panels
The scale of these tools may be off by a factor of 100 due to how blender handles unit scales for importing into UE.

### Label Maker
This generates labels for machines like the Smelter's `H-0TAF800`, it trims the input to valid characters and saves the settings into the blender file.

1. Type in the text you want.
2. Make sure the `Decal Material` is pointing at the colored decal sheet
3. Adjust the letter spacing to taste
4. Generate Label

There should now be a label at 0,0,0 with your desired text if possible, letters it couldn't make will be removed from the existing entry. Spacing is linear and more advanced kerning should be done manually.
