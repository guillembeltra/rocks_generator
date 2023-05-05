## Crear set de rocks ##

import hou
import os
path_cache = os.path.join(os.environ["HIP"], "cache", "Roks_cache")
pathNodeGenerator = "obj/Roks/Roks_generator"
pathNodeCache = "/obj/Roks/filecache_Rocks/"

inicialSeed = 0
seeds = 4              # Numero de intancies

minim = 90               # cm
maxim = 120              # cm
increment = 10           # cm

# definitions: 

def saveFile(seed, size, quality,):
        folderPath = "size_"+str(size)+"/seed_"+str(seed)+"/"
        fileName = "Rock_size_"+str(size)+"_cm_seed_"+str(seed)+"_quality_"+str(quality)+".bgeo"
        
        cacheNode = hou.node(pathNodeCache)
        cacheNode.parm("file").set(pathCache+folderPath+fileName)
        # save booton:
        cacheNode.parm("execute").pressButton()
        

def createExample(seed, size):
        nodeGenerator = hou.node(pathNodeGenerator)
        nodeGenerator.parm("seed").set(seed)
        nodeGenerator.parm("size").set(size/100.)
        # Quality :
        qualityNumber = 4
        for quality in range(qualityNumber):
                nodeGenerator.parm("quality").set(quality)
                saveFile(seed, size,quality)

# execurta

for element in range(inicialSeed,seeds):
    for size in range(minim,maxim,increment):
        createExample(element, size)
