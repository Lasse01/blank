from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesAvatars = mc.player.getPos()
x = positionDesAvatars.x
y = positionDesAvatars.y
z = positionDesAvatars.z

Material = int(input("Geben Sie die Material ID ein: "))
laenge = int(input("Geben Sie die Länge ein: "))
hoehe = int(input("Geben Sie die Höhe ein: "))
breite = int(input("Geben Sie die Breite ein: "))
mc.setBlocks(x, y, z, x+laenge, y+hoehe, z+breite, Material)
mc.setBlocks(x+1, y+1, z+1, x+laenge-1, y+hoehe-1, z+breite-1, 0)
