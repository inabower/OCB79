
#!/bin/bash

FBX_FILE_PATTERN='.*\.fbx$'
inotifywait -m -q -e CLOSE_WRITE -r . --format "%w%f" | while read newFile
    echo "${newFile} detected"
    [[ $newFile =~ ${FBX_FILE_PATTERN} ]] || continue
    fileName=`basename ${newFile}`
    name=`${fileName%.*}`
    newDir=${name}_tmp
    mkdir -p ${newDir}
    caseDir=$newDir/case
    logFile=$newDir/log
    cp -r foamCase $caseDir

    echo "Blender process fbx -> stl"
    echo "Blender process fbx -> stl" >> $logFile 2>&1
    blender -b makeStl.py ${newFile} $caseDir/tmp.stl >> $logFile 2>&1

    echo "OpenFOAM process stl -> vtu"
    echo "OpenFOAM process stl -> vtu" >> $logFile 2>&1
    tetMesh -case $caseDir >> $logFile 2>&1
    renumberMesh -overwrite -case $caseDir >> $logFile 2>&1
    foamToVTK -case $caseDir >> $logFile 2>&1

    echo "meshio process vtu -> msh22"
    echo "meshio process vtu -> msh22" >> $logFile 2>&1
    meshio-convert ${caseDir}/VTK/case_0/internal.vtu --output-format gmsh22 ${newDir}/tmp22.msh >> $logFile 2>&1

    echo "Gmsh process msh22 -> msh1"
    echo "Gmsh process msh22 -> msh1" >> $logFile 2>&1
    gmsh -3 ${newDir}/tmp22.msh -format msh1 ${newDir}/tmp1.msh >> $logFile 2>&1

    echo "GetFEM calculating"
    echo "GetFEM calculating" >> $logFile 2>&1
    python calcLinear ${newDir}/tmp1.msh ${newDir}/mises.vtk >> $logFile 2>&1
    paraview --data=${newDir}/mises.vtk
done