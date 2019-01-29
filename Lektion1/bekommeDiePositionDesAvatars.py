from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    positionDesAvatars = mc.player.getPos()
    x = positionDesAvatars.x
    y = positionDesAvatars.y
    z = positionDesAvatars.z
    mc.setBlocks(x-1, y+2, z-1, x+1 , y-6 , z+1, 0)
    #Macht Tiefen Fall
    



