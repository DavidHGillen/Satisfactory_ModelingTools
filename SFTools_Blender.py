# This code is released under CC-0, no rights are retained or warranties provided
# David "Angry Beaver" Gillen - 2020

import bpy
import bmesh



# Declarations
uvDiv = 2048 # texture size
physMod = 1.0/9.2 # feel right number
class EdgeRect:
    def __init__(self, t, l, b, r):
        self.t = t
        self.l = l
        self.b = b
        self.r = r
        
class SFTools_TextMapRef:
    def __init__(self, rect, baseline):
        self.uvrect = EdgeRect(
            b = 1 - (rect[1] / uvDiv),
            l = rect[0] / uvDiv,
            t = 1 - ((rect[1] + rect[3]) / uvDiv),
            r = (rect[0] + rect[2]) / uvDiv
        )
        self.physrect = EdgeRect(
            t = (rect[3]/-2.0 + baseline) * physMod,
            b = (rect[3]/2.0 + baseline) * physMod,
            l = 0,
            r = rect[2] * physMod
        )
        self.offset = (rect[2] * physMod)

texthash = dict()

texthash['a'] = SFTools_TextMapRef([  18, 1541, 62,62], 0);
texthash['b'] = SFTools_TextMapRef([ 100, 1541, 62,62], 0);
texthash['c'] = SFTools_TextMapRef([ 182, 1541, 62,62], 0);
texthash['d'] = SFTools_TextMapRef([ 263, 1541, 62,62], 0);
texthash['e'] = SFTools_TextMapRef([ 345, 1541, 58,62], 0);
texthash['f'] = SFTools_TextMapRef([ 423, 1541, 58,62], 0);
texthash['g'] = SFTools_TextMapRef([ 497, 1541, 62,62], 0);
texthash['h'] = SFTools_TextMapRef([ 580, 1541, 62,62], 0);
texthash['i'] = SFTools_TextMapRef([ 663, 1541, 18,62], 0);
texthash['j'] = SFTools_TextMapRef([ 697, 1541, 62,62], 0);
texthash['k'] = SFTools_TextMapRef([ 778, 1541, 62,62], 0);
texthash['l'] = SFTools_TextMapRef([ 858, 1541, 62,62], 0);
texthash['m'] = SFTools_TextMapRef([ 937, 1541, 69,62], 0);
texthash['n'] = SFTools_TextMapRef([1026, 1541, 62,62], 0);
texthash['o'] = SFTools_TextMapRef([1108, 1541, 62,62], 0);
texthash['p'] = SFTools_TextMapRef([1190, 1541, 62,62], 0);

texthash['q'] = SFTools_TextMapRef([  29, 1627, 68,62], 0);
texthash['r'] = SFTools_TextMapRef([ 114, 1627, 62,62], 0);
texthash['s'] = SFTools_TextMapRef([ 196, 1627, 62,62], 0);
texthash['t'] = SFTools_TextMapRef([ 274, 1627, 62,62], 0);
texthash['u'] = SFTools_TextMapRef([ 354, 1627, 62,62], 0);
texthash['v'] = SFTools_TextMapRef([ 435, 1627, 77,62], 0);
texthash['w'] = SFTools_TextMapRef([ 529, 1627, 89,62], 0);
texthash['x'] = SFTools_TextMapRef([ 636, 1627, 62,62], 0);
texthash['y'] = SFTools_TextMapRef([ 714, 1627, 67,62], 0);
texthash['z'] = SFTools_TextMapRef([ 798, 1627, 62,62], 0);
texthash['å'] = SFTools_TextMapRef([ 879, 1608, 62,81], 9.5); #alt+0229
texthash['ä'] = SFTools_TextMapRef([ 961, 1613, 62,76], 7.0); #alt+0228
texthash['ö'] = SFTools_TextMapRef([1043, 1627, 62,76], 7.0); #alt+0246
texthash['0'] = SFTools_TextMapRef([1125, 1627, 62,62], 0);
texthash['1'] = SFTools_TextMapRef([1203, 1627, 34,62], 0);

texthash['2'] = SFTools_TextMapRef([  23, 1714, 62,62], 0);
texthash['3'] = SFTools_TextMapRef([ 105, 1714, 62,62], 0);
texthash['4'] = SFTools_TextMapRef([ 183, 1714, 60,62], 0);
texthash['5'] = SFTools_TextMapRef([ 261, 1714, 62,62], 0);
texthash['6'] = SFTools_TextMapRef([ 343, 1714, 62,62], 0);
texthash['7'] = SFTools_TextMapRef([ 420, 1714, 54,62], 0);
texthash['8'] = SFTools_TextMapRef([ 494, 1714, 62,62], 0);
texthash['9'] = SFTools_TextMapRef([ 576, 1714, 62,62], 0);
texthash['!'] = SFTools_TextMapRef([ 658, 1714, 18,62], 0);
texthash['?'] = SFTools_TextMapRef([ 694, 1714, 55,62], 0);
texthash['"'] = SFTools_TextMapRef([ 767, 1714, 30,26], 18);
texthash['#'] = SFTools_TextMapRef([ 814, 1714, 64,62], 0);
texthash['%'] = SFTools_TextMapRef([ 894, 1714, 66,62], 0);
texthash['+'] = SFTools_TextMapRef([ 975, 1723, 48,46], 0);
texthash['-'] = SFTools_TextMapRef([1039, 1745, 28,16], -2);
texthash['/'] = SFTools_TextMapRef([1082, 1716, 31,60], 0);
texthash['\\']= SFTools_TextMapRef([1125, 1716, 31,60], 0);
texthash['['] = SFTools_TextMapRef([1173, 1717, 26,72], 0);
texthash[']'] = SFTools_TextMapRef([1215, 1717, 26,72], 0);

#These letters aren't strictly written but we can get clever with reuse
texthash['.'] =       SFTools_TextMapRef([ 658, 1758, 18,18], -22);
texthash['colonLo'] = SFTools_TextMapRef([ 658, 1758, 18,18], -16);
texthash['colonHi'] = SFTools_TextMapRef([ 658, 1758, 18,18],  16);

class SFTools_Props(bpy.types.PropertyGroup):
    LastMachineLabel: bpy.props.StringProperty(default = "M4:CH1N3 - N4M3!")
    LabelKerning:     bpy.props.FloatProperty(default = 0.2)
    LabelMaterial:    bpy.props.PointerProperty(type = bpy.types.Material)
    LabelAlignment:   bpy.props.EnumProperty(items = [
        ("NONE", "None", "Spawn at world origin left aligned", 'EMPTY_DATA', 0),
        ("LEFT", "Left", "Spawn at 3D Cursor left aligned", 'ANCHOR_LEFT', 1),
        ("CENTER", "Center", "Spawn at 3D Cursor center aligned", 'ANCHOR_CENTER', 2),
        ("RIGHT", "Right", "Spawn at 3D Cursor right aligned", 'ANCHOR_RIGHT', 3)
    ], default = "LEFT")



# Functionality
class SFTools_GenerateLabel(bpy.types.Operator):
    bl_idname = "object.sftools_generate_label"
    bl_label = "Generate Label"
    bl_description = "Generate the correctly UV'd geometry to display a decal based label with your text. Impossible characters will be removed."

    def appendVertexData(self, pos, uvs, face, mapRef, offset):
        index = len(pos) # get this early to prevent changes to pos corrupting the value

        pos += [
            (mapRef.physrect.l + offset, mapRef.physrect.t, 0),
            (mapRef.physrect.r + offset, mapRef.physrect.t, 0),
            (mapRef.physrect.r + offset, mapRef.physrect.b, 0),
            (mapRef.physrect.l + offset, mapRef.physrect.b, 0)
        ]
        uvs += [
            (mapRef.uvrect.l, mapRef.uvrect.t),
            (mapRef.uvrect.r, mapRef.uvrect.t),
            (mapRef.uvrect.r, mapRef.uvrect.b),
            (mapRef.uvrect.l, mapRef.uvrect.b)
        ]
        face += [
            (index, index+1, index+2, index+3)
        ]

    def execute(self, context):
        ignored = ''
        result = ''
        offset = 0

        propref = context.scene.SFTools_Props
        source = propref.LastMachineLabel.lower()

        mesh = bpy.data.meshes.new("")
        pos = []
        uvs = []
        face = []

        for element in source:
            if element == ' ': # just add a space
                offset += texthash['i'].offset + propref.LabelKerning
                result += element

            elif element == ':': # add the two "." of a colon
                self.appendVertexData(pos, uvs, face, texthash['colonLo'], offset);
                self.appendVertexData(pos, uvs, face, texthash['colonHi'], offset);

                offset += texthash['.'].offset + propref.LabelKerning
                result += element

            else: # add the letter if found
                mapRef = None
                try: mapRef = texthash[element]
                except: ignored += element
                else:
                    self.appendVertexData(pos, uvs, face, mapRef, offset);

                    offset += mapRef.offset + propref.LabelKerning
                    result += element

        if len(ignored) > 0: print("Ignored chars with no equivalent: " + ignored)

        if len(result) > 0:
            i = 0
            scene = context.scene

            # do we need to move the vertices back, needed full length to calculate this
            align = 0
            if propref.LabelAlignment == "CENTER":
                align = (offset - propref.LabelKerning) / 2.0
            if propref.LabelAlignment == "RIGHT":
                align = offset - propref.LabelKerning

            if align != 0:
                for ind in range(0, len(pos)):
                    pos[ind] = (pos[ind][0] - align, pos[ind][1], pos[ind][2])

            # create mesh and attach
            mesh.from_pydata(pos, [], face)
            mesh.update()
            obj = bpy.data.objects.new("Label: " + result, mesh)
            obj.data = mesh
            scene.collection.objects.link(obj)

            # open object for editing because we have to make changes
            context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            bm = bmesh.from_edit_mesh(mesh)

            obj.data.materials.append(propref.LabelMaterial)

            uv_layer = bm.loops.layers.uv.verify()
            for face in bm.faces:
                for loop in face.loops:
                    loop[uv_layer].uv = uvs[i]
                    i += 1

            # move to cursor
            if propref.LabelAlignment != "NONE":
                obj.location = scene.cursor.location
                obj.rotation_euler = scene.cursor.rotation_euler

            # close mesh now we're done
            bmesh.update_edit_mesh(mesh)
            bpy.ops.object.mode_set(mode='OBJECT')

            propref.LastMachineLabel = result
            mesh.name = "LabelMesh"

        return {'FINISHED'}

class SFTools_LabelMakerPanel(bpy.types.Panel):
    bl_label = "Label Maker"
    bl_idname = "sftools_label_maker"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SFTools'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column()
        col.prop(scene.SFTools_Props, "LastMachineLabel", text="", icon = 'FILE_TEXT')

        # use distinct labels for better ui across all elements
        row = col.row()
        row.label(text = "Letter Spacing:")
        row.prop(scene.SFTools_Props, "LabelKerning", text="")

        row = col.row()
        row.label(text = "Decal Material:")
        row.prop(scene.SFTools_Props, "LabelMaterial", text="")

        row = col.row()
        row.label(text = "Alignment:")
        row.prop(scene.SFTools_Props, "LabelAlignment", text="")

        col.separator() # improves readability

        col.operator("object.sftools_generate_label")



# System
def register():
    bpy.utils.register_class(SFTools_Props)
    bpy.utils.register_class(SFTools_GenerateLabel)
    bpy.utils.register_class(SFTools_LabelMakerPanel)
    bpy.types.Scene.SFTools_Props = bpy.props.PointerProperty(type=SFTools_Props)

def unregister():
    bpy.utils.unregister_class(SFTools_Props)
    bpy.utils.unregister_class(SFTools_GenerateLabel)
    bpy.utils.unregister_class(SFTools_LabelMakerPanel)
    del(bpy.types.Scene.SFTools_Props)

if __name__ == "__main__":
    register()
