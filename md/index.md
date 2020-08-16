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

## 今回はgmsh形式を目指す

>>>

## サーフェスメッシュからボリュームメッシュへの変換

>>>

一般的にサーフェスメッシュ






  