## VRモデリング

## → 構造解析

## → 3Dプリンタ

---

## 自己紹介

- 名前：inaba
- 所属：材料メーカー
- かなり前に始めた：電気化学
- 結構前に始めた：数値流体解析
- 最近始めた：VR、構造解析、3Dプリント

---

#### 今日のモチベーション

VRや3Dプリンタで遊びながら有限要素法を勉強してみる

>>>

#### 概要

- VRでモデリングして保存したデータに対して
- 自動で構造解析をしてその結果をもとにVRで修正する
- 最終的には3Dプリンタでそれを出力する
  - というようなことをやってみたい

>>>

###### 今回の内容

<img src="fig/flow2_outline.png" height="580">

---

# 背景説明① 3Dプリンタ

>>>

## 購入したもの

### ELEGOO MARS PRO

<img src="fig/ELEGOO_l.png" alt="ELEGOO MARS PRO" width="280">

>>>

<font size=5em>

- <font color="blue">ELEGOO MARS PRO</font>
    - 種類：UV SLA型 3Dプリンタ
    - 価格：35000円(2020.8.12現在, Amazon)
    - 造形サイズ：68 mm×120 mm×150 mm
    - 装置サイズ：200 mm×200 mm ×420mm
    - 層の厚さ：0.01 mm - 0.2 mm
    - 造形速度：225.5 mm/h
    - データ通信：USBメモリ経由

- 良かった点
  - 思ったよりコンパクト
  - かなりきれいに出力される
  - 臭くない（対処が必要）
- 気になる点
  - 洗浄用のアルコールを使用する必要がある
  - 安定して出力するコツを掴むまで苦労する
  - 購入直後に新型が出た(MARS PRO 2)

</font>

<img src="fig/ELEGOO_l.png" alt="ELEGOO MARS PRO" width="400">

>>>

## SLA型 3Dプリンタ ???

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

SLA型 3Dプリンタ
<font size=4.5em>

- 仕組み
    0. 底面透明なバットに<font color="red">液状の光硬化樹脂</font>を入れる
    1. 少し隙間を開けて<font color="blue">プラットフォーム</font>をセット
    2. 底面にUV照射
    3. <font color="orange">硬化した部分</font>を引き剥がす
    4. ①〜③を繰り返す

- メリット
    - アンチエイリアスによる滑らかな曲面
    - UV硬化レジンの塗布による精密な後処理
    - 強度の指向性が少ないとされる
- デメリット
    - 溶剤による洗浄が必要
    - 使用できる材質がFDMに比べて少ない
    - 熱を用いた後処理ができない
    - 日光に晒される場所での使用には適さない

</font>
</div>

<div class="col" style="width: 50%; float: right;">
<video src="fig/LDA.mp4" autoplay loop></video>
</div>
<div class="col" style="width: 40%; float: right;">
<font size=3em>

<br><br>
- 補足
  - SLA(光造形法)：光硬化樹脂を紫外線レーザーなどで一層ずつ硬化することによって積層して立体形状を作成する。
  - FDM(材料溶解積層法)：熱可塑性樹脂のフィラメントを高温(200℃付近)で融かし、積層させることで立体形状を作成する。有限差分法ではない。
  - インクジェット方式：液体を上から射出し紫外線で硬化する。SLAよりも高速。ちょっと高い。

</font>
</div>

</div>

---

# 背景説明② VR-HMD

>>>

## 購入したもの
### Oculus Quest

<img src="fig/oculusQuest.png" width="300">

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=4.5em>

- <font color="blue" size="8em">Oculus Quest</font>
    - スタンドアローン型HMD
    - 価格：49,800円（2020.8.12現在, 公式サイト）
    - 開発元：Facebook社
    - 完全なスタンドアローン型でPC接続なしに遊ぶことができる
    - ケーブルを繋げばPCVRゲーム(Steamなど)を遊ぶことも可能
    - 新型が出るとの噂も（要出典）

- 良かった点
    - 音ゲーはケーブルなしだとかなり快適
    - グラボ搭載デスクトップPCを用意しなくていいと考えるとかなり安価
- 気になる点
    - Oculus Quest非対応のゲームも結構ある
    - 結局PCに繋いで遊びたくなるのでグラボ搭載PCはほしい
    - 何かがあっていないのか目がすぐ疲れる

</font>
</div>

<div class="col" style="width: 50%; float: right;">
<img src="fig/oculusQuest.png" width="400">
</div>
<div class="col" style="width: 40%; float: right;">
<font size=3em>

<br><br>
- 補足
  - HMD(ヘッドマウントディスプレイ)：VRゴーグルと呼ぶよりHMDと読んだ方がわかってる感が出る
  - VR音ゲー：BeatSaberという飛んでくる箱を曲に合わせて斬るゲーム。最初はほぼこれだけのためにHMDを買った。
  - Valve Index：現在ハイエンドのHMD。13万円程度。解像度やフレームレートが段違いらしい。欲しい。　

</font>
</div>

</div>

---

# 背景説明③ VRモデリング

>>>

## 購入したもの

### Oculus Medium

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=4.5em>

- <font color="blue" size="8em">Oculus Medium</font>
    - VR制作ツール
    - 価格：2,990円（2020.8.12現在, Oculus Store）
    - 開発元：Adobe社
    - スカルプトモデリングやペイントなどが可能
    - PC接続必須
    - fbx, ply形式で入出力可能

- 良かった点
    - かなり直感的に操作できる
    - 入出力が可能なので今回の用途にぴったり
- 気になる点
    - メモリをかなり食う。現状スペックではカクつく。
    - 操作によって3Dモデルの基準座標を変えてしまうので慣れが必要
    - まだ全然使いこなせていない

</font>
</div>

<div class="col" style="width: 50%; float: right;">
    <video src="fig/oculusMedium.mp4" autoplay loop muted width="400"></video>
</div>
<div class="col" style="width: 40%; float: right;">
<font size=3em>

<br><br>
- 補足
  - .fbx：Autodesk社製の拡張子。面、テクスチャ、リグのデータを保有可能
  - .ply：Stanford大学製の拡張子。点、辺、面のデータを保有可能

</font>
</div>

</div>

---

# 背景説明④ 構造解析

>>>

<font size=6em>

- <font color="blue" size="7em">構造解析系オープンCAE</font>
    - <a href="https://frontistr-commons.gitlab.io/FrontISTR/manual_ja/ihtml">FrontISTR</a> : 国産、大規模計算に向いている
    - <a href="http://adventure.sys.t.u-tokyo.ac.jp/jp/">Adventure</a> : 国産、大規模計算に向いている
    - <a href="https://www.code-aster.org/V2/spip.php?article303">Salome-Meca</a> : CAD、メッシャ、GUIが付いているのでわかりやすい
    - <a href="http://www.calculix.de/">Calculix</a> : Abaqusと形式が似ている
    - <a href="https://www.csc.fi/web/elmer">Elmer</a> : 流体との連成が可能
    - <b><a href="http://getfem.org/">GetFEM</a></b> : Python, Matlab そして Scilabのインタフェースを使用可能なC++の汎用有限要素法ライブラリ。このライブラリの目的は有限要素法を用いて線形および非線形偏微分方程式を解くフレームワークを提供することである。有限要素近似や数値積分法の選択の柔軟性が特徴の一つである。


</font>
</div>

<div class="col" style="width: 40%; float: right;">
<font size=3em>

<br><br>
- 参考
  - <a href="https://www.hpcwire.jp/archives/9130">HPC JAPAN/CAEシリーズ：第11回 OpenCAEの代表的ツールと関連情報 (その2)</a>
  -<a href="http://opencae.gifu-nct.ac.jp/pukiwiki/index.php?plugin=attach&refer=%C2%E8%A3%B3%A3%B9%B2%F3%CA%D9%B6%AF%B2%F1%A1%A7H270509&openfile=Opencae%CA%D9%B6%AF%B2%F1OSS%B4%D8%CF%A2SH.pdf">SH氏/オープンソースCAEソフト一覧調査</a>

</font>
</div>

</div>

>>>

## 今回はGetFEMを使用

<img src="fig/logogetfem.png" width="300">

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=5.5em>

- <font color="blue" size="8em">GetFEM</font>
    - Pythonで呼び出して使用することが可能。
    - 積分法や有限要素法を自分で指定して組み立てていく
    - 有限要素法の勉強になりそう

- 良かった点
    - 頑張ればPython内でプリからポストまで完結できる
    - Jupyter内で動かせばデバッグもやりやすい
    - 式を作るところから行うので勉強になる

</font>
</div>

<div class="col" style="width: 50%; float: right;">

<font size=5em>

```python
# メッシュの読み込み
m = gf.Mesh('import', 'gmsh', 'tmp.msh') # Gmsh形式のメッシュを読込
# 場の作成
mfu=gf.MeshFem(m,3) # 3次元の変位
# 要素の作成
mfu.set_fem(gf.Fem('FEM_PK(3,2)')) # 四面体上の2次のLagrange要素
# 立体求積法の作成
mim=gf.MeshIm(m, gf.Integ('IM_TETRAHEDRON(5)')) # 四面体要素の5次のGauss積分
```

</font>

</div>

<div class="col" style="width: 40%; float: right;">
<font size=3em>

<br><br>
- 参考になるサイト
  - 公式サイト：<a href="http://getfem.org/">getfem.org</a>
  - ドキュメント和訳：<a style="" href="https://getfem.readthedocs.io/ja/latest/contents.html">getfem.readthedocs.io/ja/latest</a>
    - <a href="https://getfem.readthedocs.io/ja/latest/userdoc/appendixA.html">付録A.有限要素法リスト</a></li>
    - <a href="https://getfem.readthedocs.io/ja/latest/userdoc/appendixB.html">付録B.立体求積法のリスト</a>

</font>
</div>

</div>

---

# 今回のお題

>>>


<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=5em>

<br>
<br>
<br>

## 今回のお題

<br>

### 机の横にマイクを置く場所を作りたい

<br>
<br>

- Amazonのwebマイクを購入したが机の上ではなく横以外に設置したい
- 机の横のネジを外してそこに挟み込む形で設置する

</font>
</div>


<div class="col" style="width: 40%; float: right;">
<img src="fig/photoimage.png">
</div>

</div>

---

# STEP①

## 下準備

>>>

###### SALOMEで必要部分と不必要部分を作成

<img src="fig/flow2_salome.png" height="580">

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=5em>

- <font color="green">必要部分</font>と<font color="red">障害物部分</font>
    - 実際の実在する部分を<font color="red">障害物</font>、3Dプリントしたときに最低限この形になってほしいという場所を<font color="green">必要部分</font>とする
    - 役割としては
      - VRでモデリングするための指標
      - モデリングではみ出した場合にカットする
    - 形式としては最終的にfbx形式にする必要がある
      - 今回はBlenderを使うので読み込める形式の中で一番扱いやすいSTL形式で出力した

</font>
</div>


<div class="col" style="width: 40%; float: right;">
<img src="fig/work_salome2.png" width="600">
</div>

</div>

>>>

## Blenderで変換

- STLをimport
- FBXでexport


>>>

### これを元にVRでモデリング→

---

# STEP②

## VRモデリング

>>>

<video src="fig/step1.mp4" autoplay loop muted width=800></video>

描いていく

>>>

<video src="fig/step2.mp4" autoplay loop muted width=800></video>

描いていく

>>>

<video src="fig/step3.mp4" autoplay loop muted width=800></video>

形状もいろいろ

>>>

<video src="fig/step4.mp4" autoplay loop muted width=800></video>

できたらエクスポートする

>>>

### fbx形式で保存されたので整形していく→

---

# STEP③

## Blenderで形状を整える

<img src="fig/Blender_logo.svg.png" height="200">

>>>


<div class="container">

<div class="col" style="width: 40%; float: left;">

<font size=5.5em>

- <font color="blue" size="6em">Blenderによる処理手順</font>
    1. 必要な部分と除外する部分をimport
    2. fbx形式をimport
    3. リメッシュ機能でfbxのサーフェスをある程度整える
    4. ブーリアン機能で（モデリング部分+必要部分）-除外する部分
    5. stl形式でexport

という処理を→のようにPythonで書く

</font>

</div>

<div class="col" style="width: 60%; float: right;">

<font size=6em>

```python
#!python

import bpy
import sys
from pathlib import Path

# ファイル名は引数で渡せるように
stlAddFileName = Path(sys.argv[-3])
stlDiffFileName = Path(sys.argv[-2])
fbxFileName = Path(sys.argv[-1])

# stl(必要部分)の読み込み
bpy.ops.import_mesh.stl(filepath=str(stlAddFileName))
ob_stl_add = bpy.context.scene.objects[-1]
ob_stl_add.name = 'addStl'

# stl(障害物部分)の読み込み
bpy.ops.import_mesh.stl(filepath=str(stlDiffFileName))
ob_stl_diff = bpy.context.scene.objects[-1]
ob_stl_diff.name = 'diffStl'

# fbx(VRで作った部分)の読み込み
bpy.ops.import_scene.fbx(filepath=str(fbxFileName))
ob_fbx = bpy.context.scene.objects[-1]
ob_fbx.name = 'newFbx'
# OculusMediumだとなぜか90回転したものができているので戻す
ob_fbx.rotation_euler[0] = 3.141592653589 / 2.0

for ob in bpy.context.scene.objects:
    ob.select_set(False)
    
# 必要部分にリメッシュモディフィアーを適用
ob_stl_add.select_set(True)
bpy.context.view_layer.objects.active = ob_stl_add

bpy.ops.object.modifier_add(type='REMESH')
mod = ob_stl_add.modifiers[-1]
mod.mode = 'SHARP'
mod.octree_depth = 8
mod.use_remove_disconnected = False
bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

# VRで作った部分にリメッシュモディフィアーを適用
ob_stl_add.select_set(False)
ob_fbx.select_set(True)
bpy.context.view_layer.objects.active = ob_fbx

bpy.ops.object.modifier_add(type='REMESH')
mod = ob_fbx.modifiers[-1]
mod.mode = 'SMOOTH'
mod.octree_depth = 7
bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

# ブーリアンモディフィアーで　VR部+必要部
bpy.ops.object.modifier_add(type='BOOLEAN')
mod = ob_fbx.modifiers[-1]
mod = ob_fbx.modifiers[-1]
mod.name = 'FBX+STL'
mod.operation = 'UNION'
mod.object = ob_stl_add
bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

# ブーリアンモディフィアーで　（VR部+必要部）-障害物
bpy.ops.object.modifier_add(type='BOOLEAN')
mod = ob_fbx.modifiers[-1]
mod.name = 'FBX+STL-STL'
mod.operation = 'DIFFERENCE'
mod.object = ob_stl_diff
bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

# stlでエクスポート
newStlFileName = str(fbxFileName).replace('.fbx', '.stl')
print(f'export to {newStlFileName}')
bpy.ops.export_mesh.stl(filepath=newStlFileName, use_selection=True)

```

</font>


<font size=3em>

- 使用バージョン：Blender 2.8.3
- BlenderAPIはバージョン2.8.0を境に激変したので調べるときなどは注意が必要

</font>
</div>

</div>

>>>

### これを元にボリュームメッシュを作っていく→

---

# STEP④

## ボリュームメッシュの作成

>>>

- GetFEMが読み込み可能なのは
  - Gmsh (format1.0)
  - gid
  - cdb
  - am_fmt
- 今回はテトラメッシュでOK？

# 

### → Gmsh形式がよさそう

>>>

<div class="container">

<div class="col" style="width: 55%; float: left;">

<font size=5.5em>

<font color="blue" size="6em">GmshによるSTLからボリュームメッシュの作成</font>

- Compound Surface
  - サーフェスメッシュの線に依存しないメッシュを作成することができる

</div>

<div class="col" style="width: 45%; float: right;">

<img src="fig/bunny.png" height="500">

</div>

</div>


>>>

## うまくいかない・・・

>>>

## 困った・・・

>>>

## そうだ！OpenFOAMを使おう！

>>>

<!-- .element: data-background-iframe="https://ja.wikipedia.org/wiki/OpenFOAM" -->

>>>

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=4.5em>

- <font color="blue" size="6em">tetMesh</font>
    - OpenFOAMのメッシングツールの中の一つ
    - 表面メッシュからテトラメッシュを生成する
    - 境界層がない場合は以下のような単純な設定で生成可能
    - octree形式なのでメッシュ品質としてはそこまでよくない
- <font color="blue" size="6em">foamToVTK</font>
    - OpenFOAMのデータをVTK形式に変換する
    - セル情報のvtuと境界情報のvtpに分割されることになる
    - 今回はセル情報のvtuを使用する

</font>

<font size=6em>

<font size=4.5em>境界層をつけないのであれば設定はとても簡単</font>

```cpp
/*--- header ---*/

surfaceFile "tmp.stl";

minCellSize 1.5;
maxCellSize 7.0;
boundaryCellSize 1.0; // STL面と重複している場所のサイズ

localRefinement{}
```

<font size=4.5em>system/meshDict</font>

</font>

</div>

<div class="col" style="width: 50%; float: right;">

<img src="fig/mesh_openfoam.png" height="500">

<font size=3em>
stl形式のサーフェスメッシュ（左）からtetMeshで生成したボリュームメッシュ（右）
</font>

</div>

</div>

>>>

vtu形式のボリュームメッシュができたのでgmsh形式に変換する

<img src="fig/mesh_openfoam.png" height="500">


>>>

## meshioとGmshで変換

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

###### gmsh形式のボリュームメッシュができた

<img src="fig/flow2_openfoam.png" height="580">

>>>

いよいよ構造解析へ→

---

## GetFEMによる解析

>>>

<!-- .element: data-background-iframe="md/faomToGmsh.html" -->

>>>

<!-- .element: data-background-iframe="md/mises.html" -->

>>>

計算できそうなら.py形式にして実行できるようにする。

<font size=6.5em>

```Python
import sys
import getfem as gf
import numpy as np

def main(mesh_file, output_name):
    # 物性値
    degree = 2
    E = 1e3   # Young率
    Nu = 0.3  # Poisson比
    Lambda = E*Nu / ((1+Nu)*(1-2*Nu)) # Lame 定数 
    Mu = E/(2*(1+Nu))                 # Lame 定数 

    # メッシュの読み込み
    m = gf.Mesh('import', 'gmsh', mesh_file)
    
    # 変異と応力
    mfu = gf.MeshFem(m,3)
    mfp = gf.MeshFem(m,1)

    # 要素
    mfu.set_fem(gf.Fem('FEM_PK(3,2)'))
    mfp.set_fem(gf.Fem('FEM_PK(3,0)'))

    # 積分法
    mim = gf.MeshIm(m, gf.Integ('IM_TETRAHEDRON(5)'))

    # 境界条件
    topfaces = m.outer_faces_in_box([0.0,-0.01,0.011], [0.025, 0.08, 0.019])
    btmfaces = m.outer_faces_in_box([0.0,-0.01,-0.0061], [0.025, 0.08, -0.0059])
    NEUMANN_BOUNDARY = 1
    DIRICHLET_BOUNDARY = 2

    m.set_region(NEUMANN_BOUNDARY,   topfaces)
    m.set_region(DIRICHLET_BOUNDARY, btmfaces)

    # モデル
    md = gf.Model('real')
    md.add_fem_variable('u', mfu)
    md.add_initialized_data('cmu', Mu)
    md.add_initialized_data('clambda', Lambda)
    md.add_isotropic_linearized_elasticity_brick(mim, 'u', 'clambda', 'cmu')
    md.add_fem_variable('p', mfp)
    md.add_linear_incompressibility_brick(mim, 'u', 'p')
    md.add_initialized_data('VolumicData', [0,-1,0])
    md.add_source_term_brick(mim, 'u', 'VolumicData')

    md.add_Dirichlet_condition_with_multipliers(mim, 'u', mfu, 2)

    # 計算実行
    print('running solve...')
    md.solve('noisy', 'max iter', 1);
    U = md.variable('u');
    print('solve done!')

    # 結果の抽出
    mfdu=gf.MeshFem(m,1)
    mfdu.set_fem(gf.Fem('FEM_PK_DISCONTINUOUS(3,1)'))
    VM = md.compute_isotropic_linearized_Von_Mises_or_Tresca('u','clambda','cmu', mfdu);

    # post-processing
    sl=gf.Slice(('boundary',), mfu, degree)
    
    # VTKで出力
    sl.export_to_vtk(output_name, 'ascii', mfdu,  VM, 'Von Mises Stress', mfu, U, 'Displacement')
    
    print(f'Result is exported to {output_name}')
    
if __name__ == "__main__":
    mesh_name = sys.argv[1]
    output_name = sys.argv[2]
    
    main(mesh_name, output_name)

```

</font>

>>>

###### メッシングから構造解析までができた

<img src="fig/flow2_openfoam.png" height="580">

>>>

### 自動化してみよう→

---

# STEP⑥

## 自動化スクリプト

>>>

<div class="container">

<div class="col" style="width: 60%; float: left;">

<font size=6em>

```bash
#!/bin/bash

FBX_FILE_PATTERN='.*\.fbx$'
# 監視しているディレクトリにファイルが生成されたら発動
inotifywait -m -q -e CLOSE_WRITE ../ --format "%w%f" | while read newFile
do
    # ファイル名から拡張子を抜いたり同名のディレクトリを作ったり
    [[ $newFile =~ ${FBX_FILE_PATTERN} ]] || continue
    echo "${newFile} detected"
    fileName=`basename ${newFile}`
    name=${fileName%.*}
    newDir=${name}_tmp
    mkdir -p ${newDir}
    caseDir=$newDir/case
    logFile=$newDir/log
    cp -r foamCase $caseDir

    # Blenderによりfbxと元形状からサーフェスメッシュを作成する
    echo "Blender process fbx -> stl"
    blender -b -P makeStl.py -- $PWD/addStl.stl $PWD/diffStl.stl ${newFile} >> $logFile 2>&1
    cp ${newFile%.*}.stl $newDir/case/tmp.stl

    # OpenFOAMによりサーフェスメッシュからボリュームメッシュを作成する
    echo "OpenFOAM process stl -> vtu"
    source ~/OpenFOAM/OpenFOAM-v2006/etc/bashrc
    tetMesh -case $caseDir >> $logFile 2>&1
    transformPoints -scale 0.001 -case $caseDir >> $logFile 2>&1
    renumberMesh -overwrite -case $caseDir >> $logFile 2>&1
    foamToVTK -case $caseDir >> $logFile 2>&1
    checkMesh -case $caseDir >> $logFile.chechMesh 2>&1
    cat $logFile.chechMesh | grep -4 cells:

    # meshioで.msh(Gmsh2.2)に変換
    echo "meshio process vtu -> msh22"
    meshio-convert.exe ${caseDir}/VTK/case_0/internal.vtu --output-format gmsh22 ${newDir}/tmp22.msh >> $logFile 2>&1

    # Gmshで.msh(Gmsh1.0)に変換
    echo "Gmsh process msh22 -> msh1"
    gmsh -3 ${newDir}/tmp22.msh -format msh1 -o ${newDir}/tmp1.msh >> $logFile 2>&1

    # GetFEMで構造解析
    echo "GetFEM calculating"
    python3 calcLinear.py ${newDir}/tmp1.msh ${newDir}/mises.vtk 1>> $logFile 2>/dev/null
    tail -n 10 $logFile 
    echo "Calculation DONE"

    # 結果を表示
    echo "Result : ${newDir}/mises.vtk"
    echo "For example : paraview --data=${newDir}/mises.vtk"
done
```

`autoDetection.sh`

</font>
</div>

<div class="col" style="width: 40%; float: right;">

<img src="fig/directory.png">

</div>
</div>

>>>

<div class="container">

<div class="col" style="width: 40%; float: left;">

<img src="fig/last.png">

</div>

<div class="col" style="width: 40%; float: right;">

<br><br><br><br>

## 完成！

</div>
</div>

---

<div class="container">

<div class="col" style="width: 50%; float: left;">

<font size=5em>

## まとめ

1.  CADで必要部分と障害物を作成
2.  Oculus MediumでVRモデリング
3.  Blenderでサーフェスメッシュを作成
4.  OpenFOAM→meshio→Gmshでボリュームメッシュの作成
5.  GetFEMで弾性解析
6.  3-5を自動化

### 課題

- Windowsのファイル作成をWSLが認識してくれないので自動実行してくれない（別のターミナルでtouchすればそれがトリガーになる）
- メッシュを細かくするとすぐにメモリ不足（VRでも7GBくらい使っているため）
- スクリプト作りに苦労しすぎて全然有限要素法の勉強ができていない

</font>

</div>

<div class="col" style="width: 40%; float: right;">

<font size=4em>

#### 実行環境

- HMD : Oculus Quest (Oculus Link connected)
  - モデリング : Oculus Medium
- 3Dプリンタ : ELEGOO MARS PRO
  - スライサ : Formware3D
  - レジン : ELEGOO Standard
- Hardware
  - CPU : Ryzen 7 2700X
  - GPU : NVIDIA GeForce RTX2070
  - RAM : 16GB (Swap 64GB)
- Software
  - Windows10 (2004, build 20185.1000)
    - SALOME 9.5.0
    - Ubuntu20.04LTS on WSL2
      - GetFEM 5.4.1
      - Blender 2.8.3
      - OpenFOAM v2006
      - Gmsh 4.4.1

</font>
</div>
</div>

---
  