# SF_FoundationTemplates.blend
This readme breaks down specifics about this file!

***This file is currently a Beta and needs testing. I will be doing this while using it for myself; however, it never hurts to share.***

This is a collection of templates that are the correct dimensions and orientations for the base foundation shapes found in Vanilla Satisfactory.

As always they have been recreated from scratch but are only intended for use with Satisfactory. Of important note, these are not UV'd, vanilla textures are mirrored and UV outside 0-1 in a tricky fashion. Check it out. But UV isn't important for these, they are template shapes for use in adding new building materials to the ingame building material system (ficsit, concrete, asphalt, etc). If the dimensions or orientations of your new building material don't match vanilla, then in game upgrades will cause issues. Should you wish to use extraordinarily simple shapes for your blocks I recommend retexturing the Concrete set rather than exporting these meshes.

My best recommendation for workflow is to model the LODs and collisions into this file, use the appropriate unreal naming conventions like an LOD suffice and UCX prefix, and then import all the files through a single FBX. This will provide you with a very clean workflow.