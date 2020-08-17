## 3DプリントのためにVRでモデリングする時にデータを保存したら自動で構造解析をしてくれるのでゴーグルを持ち上げるとディスプレイにはコンター図が表示されている件

---

## 自己紹介

- 名前：inaba
- 所属：材料メーカー
- かなり前に始めた：電気化学
- 結構前に始めた：数値流体解析
- 最近始めた：VR、構造解析、3Dプリント

---

## 今回の内容

3DプリントのためにVRでモデリングする時にデータを保存したら自動で構造解析をしてくれるのでゴーグルを持ち上げるとディスプレイにはコンター図が表示されていて欲しい

>>>

###### 今回の内容

<img src="fig/flow_00_introduction.png" height="580">

---

# 背景説明① 3Dプリンタ

>>>

## 購入したもの

### ELEGOO MARS PRO

<img src="fig/ELEGOO_l.png" alt="ELEGOO MARS PRO" width="280">

>>>

## ELEGOO MARS PRO
- 種類：<font color="blue">UV LDA型 3Dプリンタ</font>
- 価格：35000円(2020.8.12現在, Amazon)
- 造形サイズ：68 mm×120 mm×150 mm
- 装置サイズ：200 mm×200 mm ×420mm
- 層の厚さ：0.01 mm - 0.2 mm
- 造形速度：225.5 mm/h
- データ通信：USBメモリ経由

<img src="fig/ELEGOO_l.png" alt="ELEGOO MARS PRO" width="280">

>>>

## LDA型 3Dプリンタ ???

>>>

底面が透明フィルムになったバットに液状の<font color="red">光硬化樹脂</font>を入れて

1. 少し隙間を開けて<font color="blue">プラットフォーム</font>をセット
2. 底面にUV照射
3. <font color="orange">硬化した部分</font>を引き剥がす
4. ①〜③を繰り返す

<video src="fig/LDA.mp4" autoplay loop width="400"></video>

>>>

- メリット
    - アンチエイリアスによる滑らかな曲面
    - UV硬化レジンの塗布による精密な後処理
    - 強度の指向性が少ないとされる
- デメリット
    - 溶剤による洗浄が必要
    - 使用できる材質がFDMに比べて少ない
    - 熱を用いた後処理ができない
    - 日光に晒される場所での使用には適さない

---

# 背景説明② VR-HMD

>>>

## 購入したもの
### Oculus Quest

<img src="fig/oculusQuest.png" width="300">

>>>

## Oculus Quest

- スタンドアローン型HMD
- 価格：49,800円（2020.8.12現在, 公式サイト）
- 開発元：Facebook社
- 完全なスタンドアローン型でPC接続なしに遊ぶことができる
- ケーブルを繋げばPCVRゲーム(Steamなど)を遊ぶことも可能
- 新型が出るとの噂も（要出典）

<img src="fig/oculusQuest.png" width="300">

>>>

- 良かった点
    - 音ゲーはケーブルなしだとかなり快適
    - グラボ搭載デスクトップPCを用意しなくていいと考えるとかなり安価
- 気になる点
    - Oculus Quest非対応のゲームも結構ある
    - 結局PCに繋いで遊びたくなるのでグラボ搭載PCはほしい
    - 何かがあっていないのか目がすぐ疲れる

---

# 背景説明③ VRモデリング

>>>

## 購入したもの

### Oculus Medium

>>>

## Oculus Medium
- VR制作ツール
- 価格：2,990円（2020.8.12現在, Oculus Store）
- 開発元：Adobe社
- スカルプトモデリングやペイントなどが可能
- PC接続必須
- fbx, ply形式で入出力可能

<video src="fig/oculusMedium.mp4" autoplay loop muted width="400"></video>

>>>

- 良かった点
    - かなり直感的に操作できる
    - 入出力が可能なので今回の用途にぴったり
- 気になる点
    - メモリをかなり食う。現状スペックではカクつく。
    - 操作によって3Dモデルの基準座標を変えてしまうので慣れが必要
    - まだ全然使いこなせていない

<video src="fig/oculusMedium.mp4" autoplay loop muted width="400"></video>

---

# 背景説明④ 構造解析

>>>

## 構造解析系オープンCAE

- <a href="https://frontistr-commons.gitlab.io/FrontISTR/manual_ja/ihtml">FrontISTR</a> : <font size="5">国産、大規模計算に向いている</font>
- <a href="http://adventure.sys.t.u-tokyo.ac.jp/jp/">Adventure</a> : <font size="5">国産、大規模計算に向いている</font>
- <a href="https://www.code-aster.org/V2/spip.php?article303">Salome-Meca</a> : <font size="5">CAD、メッシャ、GUIが付いているのでわかりやすい</font>
- <a href="http://www.calculix.de/">Calculix</a> : <font size="5">Abaqusと形式が似ている</font>
- <a href="https://www.csc.fi/web/elmer">Elmer</a> : <font size="5">流体との連成が可能</font>
- <b><a href="http://getfem.org/">GetFEM</a></b> : <font size="5">Python, Matlab そして Scilabのインタフェースを使用可能なC++の汎用有限要素法ライブラリ。このライブラリの目的は有限要素法を用いて線形および非線形偏微分方程式を解くフレームワークを提供することである。有限要素近似や数値積分法の選択の柔軟性が特徴の一つである。</font>

>>>

## 今回はGetFEMを使用

<img src="fig/logogetfem.png" width="300">

>>>

## GetFEM

- Pythonで呼び出して使用することが可能。
- 積分法や有限要素法を自分で指定して組み立てていく
- 有限要素法の理解のために良さそうと思い使用

```python
# メッシュの読み込み
m = gf.Mesh('import', 'gmsh', 'tmp.msh') # Gmsh形式のメッシュを読込
# 場の作成
mfu=gf.MeshFem(m,3) # 3次元の変位
# 有限要素法の作成
mfu.set_fem(gf.Fem('FEM_PK(3,2)')) # 四面体上の2次のLagrange要素
# 立体求積法の作成
mim=gf.MeshIm(m, gf.Integ('IM_TETRAHEDRON(5)')) # 四面体要素の5次のGauss積分
```

---

# 今回のお題

>>>

## 机の横にマイクを置く場所を作る

- Amazonのwebマイクを購入したが机の上ではなく横以外に設置したい
- 机の横のネジを外してそこに挟み込む形で設置する

(写真)

>>>

## 下準備

- 必要な部分と通ってはいけない部分を用意する
- これをBlenderで読み込みfbx形式にする
- これをOculus Mediumで読み込む

---

# 実際にモデリングを行う

>>>

動画など

>>>

fbx形式で保存された

---

# サーフェスメッシュの変換

>>>

## メッシュの変換

- VRモデリングで出力されるデータはply形式かfbxのサーフェスメッシュ。
- 3Dプリントをするためにはこれをstl形式に変換する必要がある
- また構造解析を行うためにはボリュームメッシュに変換する必要がある。

>>>

###### メッシュの変換

<img src="fig/flow_0_introduction_2.png" height="580" class="absolute" >

>>>

## まずはサーフェスメッシュ（stl）へ変換　→

---

## Blenderによるサーフェスメッシュの変換

<img src="fig/Blender_logo.svg.png" height="200">

>>>

## Blender

- CGモデリングソフト
- 商用ソフトに劣らない幅広い機能と拡張性が魅力
- ブーリアン機能で加算と除外も可能
- 様々なサーフェスメッシュのimport/exportが可能
- PythonによるCUI実行も可能

<img src="fig/blender_working.png" height="300">

>>>

## Blenderによる後処理

1. 必要な部分と除外する部分をimport
2. fbx形式をimport
3. リメッシュ機能でfbxのサーフェスをある程度整える
4. ブーリアン機能で（モデリング部分+必要部分）-除外する部分
5. stl形式でexport

>>>

###### Blenderによるサーフェスメッシュの変換

<img src="fig/flow_1_blender.png" height="580">

---

# ボリュームメッシュの作成

>>>

- GetFEMが読み込み可能なのは以下のメッシュ
  - Gmsh (format1.0)
  - gid
  - cdb
  - am_fmt
- 今回はテトラメッシュでOK

## 今回はgmsh形式を目指す

>>>

## サーフェスメッシュからボリュームメッシュへの変換

>>>

ボリュームメッシュがサーフェスメッシュの線に引っ張られてしまう問題

>>>

## 解決法（Gmshの場合）

- Compound Surface機能
  - サーフェスメッシュの線に依存しないメッシュを作成できる

>>>

## うまくいかない・・・

>>>

## 困った・・・

>>>

## ？？？「ふむ・・・ならばOpenFOAMを使ったらどうだろう」

---

## OpenFOAM

- 世界一使用されているOSSの数値流体解析ツールボックス
- 熱流体や圧縮性流体、混相流など幅広い対象を解析可能
- メッシュの作成や変換などの機能も充実している
- cfMeshの*"tetMesh"*でテトラメッシュを作成可能

>>>

## tetMesh（OpenFOAMのユーティリティ）

- 表面メッシュからテトラメッシュを生成する
- 境界層がない場合は以下のような単純な設定で生成可能
- メッシュ品質としてはsnappyで生成されたポリヘドラメッシュをテトラに分解したもの

>>>

## foamToVTK（OpenFOAMのユーティリティ）

- OpenFOAMのデータをVTK形式に変換する
- セル情報のvtuと境界情報のvtpに分割されることになる
- 今回はセル情報のvtuを使用する

>>>

###### OpenFOAMによりvtu形式のボリュームメッシュに変換できた

<img src="fig/flow_2_OpenFOAM.png" height="580">

---

# ボリュームメッシュの変換

>>>

- GetFEMで使用するためにGmsh形式への変換が必要

# ↓

## meshioとGmshを使用する

>>>

## meshio

- Pythonのライブラリの一つ
- かなり多くのメッシュについてimport/exportができる

<img src="fig/meshio.png" width="400">

>>>

## meshioとGmshのインストールと実行例

```bash
# meshioをインストール
$ pip install meshio
# Gmshをインストール
$ sudo apt-get install gmsh
$
# gmsh22形式に変換
$ meshio-convert VTK/case_0/internaal.vtu --output-format gmsh22 tmp22.msh
# gmsh1形式に変換
$ gmsh -3 tmp22.msh -format msh1 tmp1.msh
```

>>>

###### meshioとGmshによりgmsh1形式に変換できた

<img src="fig/flow_3_GetFEM.png" height="580">

>>>

いよいよGetFEMへ

---

## GetFEMによる解析

>>>

<section data-background-iframe="md/faomToGmsh.html" data-background-interactive>
</section>

>>>

>>>

計算できそうなら.py形式にして実行できるようにする。

```Python
import sys
import getfem as gf
import numpy as np

def main(mesh_file, output_name):
    degree = 2
    E = 1e3
    Nu = 0.3
    Lambda = E*Nu / ((1+Nu)*(1-2*Nu))
    Mu = E/(2*(1+Nu))

    m = gf.Mesh('import', 'gmsh', mesh_file)
    
    mfu = gf.MeshFem(m,3)
    mfp = gf.MeshFem(m,1)

    mfu.set_fem(gf.Fem('FEM_PK(3,2)'))
    mfp.set_fem(gf.Fem('FEM_PK(3,0)'))

    mim = gf.MeshIm(m, gf.Integ('IM_TETRAHEDRON(5)'))

    topfaces = m.outer_faces_in_box([0.0,-0.01,0.011], [0.025, 0.08, 0.019])
    btmfaces = m.outer_faces_in_box([0.0,-0.01,-0.0061], [0.025, 0.08, -0.0059])
    NEUMANN_BOUNDARY = 1
    DIRICHLET_BOUNDARY = 2

    m.set_region(NEUMANN_BOUNDARY,   topfaces)
    m.set_region(DIRICHLET_BOUNDARY, btmfaces)

    md = gf.Model('real')
    md.add_fem_variable('u', mfu)
    md.add_initialized_data('cmu', Mu)
    md.add_initialized_data('clambda', Lambda)
    md.add_isotropic_linearized_elasticity_brick(mim, 'u', 'clambda', 'cmu')
    md.add_fem_variable('p', mfp)
    md.add_linear_incompressibility_brick(mim, 'u', 'p')
    md.add_initialized_data('VolumicData', [0,-1,0])
    md.add_source_term_brick(mim, 'u', 'VolumicData')

    # Attach the tripod to the ground
    md.add_Dirichlet_condition_with_multipliers(mim, 'u', mfu, 2)

    print('running solve...')
    md.solve('noisy', 'max iter', 1);
    U = md.variable('u');
    print('solve done!')
    
    sl.export_to_vtk(output_name, 'ascii', mfdu,  VM, 'Von Mises Stress', mfu, U, 'Displacement')
    
    print(f'Result is exported to {output_name}')
    
if __name__ == "__main__":
    mesh_name = sys.argv[1]
    output_name = sys.argv[2]
    
    main(mesh_name, output_name)

```

---

# 自動化スクリプト

>>>

## 待受ディレクトリ構造

>>>

## スクリプトの中身

```bash
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
```

>>>

## 実行例

---

## まとめ

>>>

- fbxを保存すると応力の解析結果が出力された
- 時間がかかってしまうのはメモリの不足が原因か
- メッシュ周りに苦労しすぎて全然有限要素法の勉強ができていない



  