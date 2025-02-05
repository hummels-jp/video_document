![alt text](合并PDF_纯图版_00.png) 
![alt text](合并PDF_纯图版_01.png) 
![alt text](合并PDF_纯图版_02.png) 
![alt text](合并PDF_纯图版_03.png) 
![alt text](合并PDF_纯图版_04.png) 
![alt text](合并PDF_纯图版_05.png) 
![alt text](合并PDF_纯图版_06.png) 
![alt text](合并PDF_纯图版_07.png) 
![alt text](合并PDF_纯图版_08.png) 
![alt text](合并PDF_纯图版_09.png) 
![alt text](合并PDF_纯图版_10.png) 
![alt text](合并PDF_纯图版_11.png) 
![alt text](合并PDF_纯图版_12.png) 
![alt text](合并PDF_纯图版_13.png) 
![alt text](合并PDF_纯图版_14.png) 
![alt text](合并PDF_纯图版_15.png) 
![alt text](合并PDF_纯图版_16.png) 
![alt text](合并PDF_纯图版_17.png) 
![alt text](合并PDF_纯图版_18.png) 
1. BevFusion 包含2个部分的内容，Bev 是一个鸟瞰空间， Fusion 是多模态数据融合，例如 Camera图像与LiDar点云的融合。
2. BevFusion中包含3种融合方法： 
3. 点级别的融合： 从点云数据中抽取采样点，根据相机的内参和外参，投影到图片上，提取图片特征，然后再和点云进行拼接。然后利用融合后的点云特征，进行3D检测。
4. 基于特征的融合：将多模态的特征数据，通过内外参数，投影拼接在一起，传递的Query
5. 点级别融合 和 特征级别融合的缺点
6. 都是将点云中的点，投影（通过相机的内参和外参）到图像平面上提取特征。
7. 相机内参是在出厂时就确定不变的， 相机外参，用来确定相机坐标系和 LIDar坐标系之间的映射关系。
8. 当图像不清晰或者点云坐标数据不准确时，例如：传感器校准不准确，外参存在有误差时，会出现映射失败的情况。
9. 点级别融合 和 特征级别融合 都是以点云数据为基准。当点云数据不准确时，3D检测的结果也不准确。以点云数据为主，以摄像头数据为次。
10. BevFusion 分别通过 CameraNetwork 和 LidarNetwork 进行特征提取，将提取后的特征进行融合，而不是进行映射，没有主次之分。
11. BevFusion 有 3个检测头， 有基于融合后特征的3D检测头，有基于图像特征的3D检测头，有基于点云特征的3D检测头，图像特征和点云特征，既可以分别工作，也可以联合工作。
![alt text](合并PDF_纯图版_18.png) 
1. BevFusion consist of two main parts: Bev, which represent a bird eye view space. Fusion, which refers to multimode data fusion, such as camera image data and Lidar pointcloud data.
2. Bevfusion includes three methods
3. point level fusion: sample-data are extracted from point cloud data and projected to the image using the camera's intrinsic and extrinsic parameter. The image feature are then extracted and concatenated with the point cloud data. The fused point cloud data are then used for 3d dectection.
4. feature-level fusion: multimodel feature data is projected and fused using intrinsic and extrinsic parameters, with the information is being passed by the query machinism.
5. Drawbacks of point-level fusion and feature-level fusion
6. Both methods project the point from the Lidar pointcloud data onto the image plain to extract feature ,using intrinsic and extrinsic parameters.
7. camera intrinsic parameter are fixed at the time of manufacturing and remain unchanged. camera extrinsic parameter defined the mapping relationship between the camera coordinate system and the Lidar coordinate system.
8.  when the image is unclear or the point cloud coordinate data is inaccurate, such as due to sensor calibration error or incorrect extrinsic parameter, mapping failture may occures.
9.  Both point-level fusion and feature-level fusion are using the point cloud data as primary. when the point cloud data is inaccurate, 3D detection result will also be inaccurate. Lidar data takes precedence, while image data is secondary.
10. BevFusion extract feature seperately using CameraNetwork and LidarNetwork, then fused the extracted features without direct mapping, meaning there is no primary and secondary data source.
11. BevFusion has three detection head: 1. A 3d detection head based on fused feature. 2 a 3d detection head based on camera image feature . 3 a 3d detection head base on lidar point cloud. Both image and Lidar features can function indepently or work togther in a unified manner. 

![alt text](合并PDF_纯图版_18.png) 
1.  BevFusion は2つの主要な部分で構成されています。Bevは鳥瞰視点の空間を表し、Fusionはカメラ画像とライダー点群の統合などのマルチモーダルデータ融合を指します。
2.  BevFusionには3つの融合方法が含まれています。
3.  点レベルの融合：LiDARの点群データからサンプリングポイントを抽出し、カメラの内部パラメータと外部パラメータを使用して、画像に投影します。その後、画像の特徴を抽出し、点群と結合します。融合後の点群特徴を用いて3D検出を行います。
4.  特徴レベルの融合：マルチモーダルの特徴データを内部パラメータと外部パラメータを用いて投影、結合し、Query　クエリを通じて情報を伝達します。
5.  点レベル融合と特徴レベル融合の欠点
6.  どちらの方法も、LiDar点群の点をカメラの内部パラメータと外部パラメータを使用して、画像平面に投影し、特徴を抽出します。
7.  カメラの内部パラメータは工場出荷時に固定され、変更されません。一方、カメラの外部パラメータは、カメラ座標系とLidar座標系間のマッピング関係を決定します。
8.  画像が不鮮明であたっり、点群の座標データが不正確な場合（例えば、センサーのカリブレーション誤差や外部パラメータの誤差がある場合）、マッピングが失敗する可能性があります。
9.  点レベル融合と特徴レベル融合どちらもLiDARの点群データを基準にしています。そのため、LiDARのデータが不正確だと3D検出の結果も不正確になります。この方法では、LiDARデータが主であり、カメラデータは補充的な役割を果たします。
10. BevFusionは、CameraNetoworkとLidarNetworkを通じてそれぞれ特徴を抽出し、その後、抽出した特徴を融合します。直接的なマッピングは行わず、主従関係がありません。
11. BevFusionには3つの３D検出ヘッドがあります。融合後の特徴に基づく３D検出ヘッド。LiDAR特徴に基づく３D検出ヘッド。画像特徴に基づく３D検出ヘッド。
12. 画像特徴とLiDar特徴は、それぞれ独立して動作することも、統合して動作することも可能です。
    
![alt text](合并PDF_纯图版_19.png) 


![alt text](合并PDF_纯图版_20.png) 
1. 图像处理流程： 输入： 多视角图像， 输出： 图像BEV空间的特征
2. 首先，通过图像特征提取网络，对多视角图像进行处理； 然后：将多视角图像特征从2维转换为3维。 其次： 对三维图像特征进行BEV空间编码，得到图像的BEV空间特征。
3. 可以基于图像的BEV空间特征，进行3D物体检测。
4. 点云处理流程： 输入： 点云数据， 输出： 点云BEV空间的特征
5. 首先，通过点云特征提取网络，得到点云BEV空间特征。常见的点云特征提取网络有PointNet，PointNet++， VoxelNet， PointPillar等。
6. 可以基于点云BEV空间特征，进行3D目标检测。
7. BEVFusion 可以将图像BEV空间的特征和点云BEV空间的特征进行融合，基于融合后的BEV特征，进行3D目标检测。
8. BevFusion 除了支持多模态3D检测，也支持单模态的3D检测。基于图像BEV空间特征的3D检测，基于点云BEV空间特征的3D检测。
   
  ![alt text](合并PDF_纯图版_20.png) 
1. 画像処理フロー：　入力：マルチビュー画像。出力：画像のBEV空間の特徴。
2. まず、画像特徴抽出ネットワークを使用してマルチビュー画像を処理します。次に、抽出されたマルチビュー画像特徴を2dから３ｄに変換します。その後、3d画像特徴をBEV空間にエンコードし、マルチビュー画像のBEV空間の特徴を取得します。
3. 画像のBEV空間の特徴によって、３D物体検出を行うことができます。
4. 点群処理フロー：　入力：点群データ、出力：点群のBEV空間の特徴
5. まず、点群特徴抽出ネットワークを使用して、点群BEV空間特徴を取得します。一般的な点群特徴抽出ネットワークには、PointNet、PointNet＋＋、VoxelNet、PointPillarなどがあります。
6. 点群のBEV空間特徴によって、３D物体検出を行うことができます。
7. BEVFusionは画像のBEV空間特徴と点群のBEV空間特徴を融合し、融合したBEV空間特徴を基づいて、３D物体検出を行うことができます。
8. BEVFusionはマルチモーダル３D物体検出をサポートだけではなく、シングルモーダルの３D物体検出もサポートしています。例えば、画像のBEV空間特徴に基づく３D物体検出や点群のBEV空間特徴に基づく３D物体検出も可能です。

 ![alt text](合并PDF_纯图版_20.png) 

1. Imapge process pipeline: input: multiview image data, output: bev-space features of image
2. first, a feature extraction network process the multi-view images. Then, the extracted multi-view image feature are transformed from 2D to 3D. Next, the 3d images features are encoded into bev space to obtain the bev-space feature of the image.
3. 3D object detection can be performed based on the image bev-space feature.
4. PointCloud process pipline: input: point cloud data; output：bev-space features of the point cloud;
5. First, based on the pointcloud feature extracting network, obtain the bev-space feature of point cloud. Common point cloud feature extraction network contains, pointNet, pointNet++, VoxelNet, PointPillar
6. 3D object detection can be performed based on the point cloud bev-space feature.
7. BevFusion can fused the image bev-space feature and point cloud bev-space feature, based on the fused bev-space feature, 3d object detection can be performed.
8. In addition to supporting multimodal 3d object detection, BevFusion also suports single modal 3d detection, including image-based bev 3d detection and point cloud-based bev 3d detection
 

![alt text](合并PDF_纯图版_21.png) 
1. 通过2维图像特征提取网络，处理各个视角的图像数据。
2. 通过 FPN 和 ADP，进行多尺度融合。 FPN Feature Pyramid Network 特征金字塔。不同尺度的图像特征，通过ADP进行上采样，池化，卷积，可以得到相同大小的特征，从而实现多尺度特征融合。
3.  ADP（Adaptive Deformable Part） ADP 指的是一种自适应形变机制，用于处理不同形态和尺度的目标，以提高目标检测或分割的效果。
4. FPN + ADP 设计流程： 输入：基础图像特征； 输出： 多尺度融合特征。 处理流程： 1 对每层特征使用ADP模块；2 ADP 模块包括上采样，池化，卷积。 3 多层特征融合。
   
![alt text](合并PDF_纯图版_21.png) 
1. process the image from different viewpoint using a 2d image feature extraction network, for example ResNet.
2. Perform multi-scale fusion using FPN Feature Pyramid Network and ADP Adaptive Deformable Part.
3. FPN Feature Pyramid Network, extracts image features at different scale.
4. Different image features are processed through ADP, which performs upsampling, pool, and convolusion to obtain image features at the same scale, which enable multi-scale feature fusion.
5. ADP Adaptive Deformable Part is an adaptvie demormable mechanism used to handle objects of varing shapes and scales, improving object detection and object segmentation.
6. FPN + ADP design process: input: basic image features at different scale; output: multi-scale fusion image features at the same scale. process step: 1 apply the ADP to each different scale feature layer to get correspondent same scale feature layer. 2 ADP includes upsampling, pool and convolution. 3 fuse the feature layers those in the same scale.
  
![alt text](合并PDF_纯图版_21.png) 
1. ２D画像特徴抽出ネットワークを使用して、各視点の画像を処理する。
2. FPNとADPを用いてマルチスケール特徴融合を実施する。　FPNは異なるスケールの画像特徴を抽出する。
3. 異なるスケールの画像特徴をADPで処理し、アップサンプリング、プーリング、畳み込みを行うことで、同じスケールの特徴を取得し、マルチスケール特徴融合を実現する。
4. ADPは適応変形メカリズムであり、異なる形状やスケールの物体に対応し、物体検出やセグメンテーションの精度を向上させる。
5. FPN＋ADPの設計プロセス、入力：異なるスケール画像特徴　出力：同じスケール融合した画像特徴。処理フロー：1　各層の画像特徴にADPモジュールを適用し、異なるスケール画像特徴から同じスケール画像特徴に変換できます。　2　ADPモジュールには、アップサンプリング、プーリング、畳み込みが含まています。　3　複数の層の画像特徴を融合する。
   
![alt text](合并PDF_纯图版_22.png) 
1. 从2D到3D的特征转换。对二维图像上的每个像素点，进行深度预测。会得到一个离散的深度预估概率。
2. 概率作为权重，与图像特征相乘，得到二维图像的3D空间。即是3D伪体素特征。
3. 3D伪体素特征的处理流程： 输入： 多尺度融合特征。 输出： 3D伪体素特征。 1 计算得到深度分布估计。 2 2D 到3D的投影换算。 3 输出3D伪体素特征。

![alt text](合并PDF_纯图版_22.png) 
1. feature transformation from 2d to 3d: predict the depth of each pixel in a 2d image, resulting in a discrete depth estimation probability.
2. use the probability as a weight and multiply it with the image features to obtain the 3D space of the 2D image, forming the 3D-pseudo-voxel feature.
3. Processing 3D-pseudo feature pipline: input: multi-scale fusion feature. output: 3D-pseudo voxel feature. 1 compute the depth distribution estimation 2 perform 2d-to-3d projection conversion. 3 output 3d-pseudo voxel feature.
4. 
5.  
![alt text](合并PDF_纯图版_23.png) 
![alt text](合并PDF_纯图版_24.png) 
![alt text](合并PDF_纯图版_25.png) 
![alt text](合并PDF_纯图版_26.png) 
![alt text](合并PDF_纯图版_27.png) 
![alt text](合并PDF_纯图版_28.png) 
![alt text](合并PDF_纯图版_29.png) 
![alt text](合并PDF_纯图版_30.png) 
![alt text](合并PDF_纯图版_31.png) 
![alt text](合并PDF_纯图版_32.png) 
![alt text](合并PDF_纯图版_33.png) 
![alt text](合并PDF_纯图版_34.png) 
![alt text](合并PDF_纯图版_35.png) 
![alt text](合并PDF_纯图版_36.png) 
![alt text](合并PDF_纯图版_37.png) 
![alt text](合并PDF_纯图版_38.png) 
![alt text](合并PDF_纯图版_39.png) 
![alt text](合并PDF_纯图版_40.png) 
![alt text](合并PDF_纯图版_41.png) 
![alt text](合并PDF_纯图版_42.png) 
![alt text](合并PDF_纯图版_43.png) 
![alt text](合并PDF_纯图版_44.png) 
![alt text](合并PDF_纯图版_45.png) 
![alt text](合并PDF_纯图版_46.png) 
![alt text](合并PDF_纯图版_47.png) 
![alt text](合并PDF_纯图版_48.png) 
![alt text](合并PDF_纯图版_49.png) 
![alt text](合并PDF_纯图版_50.png) 
![alt text](合并PDF_纯图版_51.png) 
![alt text](合并PDF_纯图版_52.png) 
![alt text](合并PDF_纯图版_53.png) 
![alt text](合并PDF_纯图版_54.png) 
![alt text](合并PDF_纯图版_55.png) 
![alt text](合并PDF_纯图版_56.png) 
![alt text](合并PDF_纯图版_57.png) 
![alt text](合并PDF_纯图版_58.png) 
![alt text](合并PDF_纯图版_59.png) 
![alt text](合并PDF_纯图版_60.png) 
![alt text](合并PDF_纯图版_61.png) 
![alt text](合并PDF_纯图版_62.png) 
![alt text](合并PDF_纯图版_63.png) 
![alt text](合并PDF_纯图版_64.png) 
![alt text](合并PDF_纯图版_65.png) 
![alt text](合并PDF_纯图版_66.png) 
![alt text](合并PDF_纯图版_67.png) 
![alt text](合并PDF_纯图版_68.png) 
![alt text](合并PDF_纯图版_69.png) 
![alt text](合并PDF_纯图版_70.png)

https://www.bilibili.com/video/BV1ix4y1f7mX/?spm_id_from=333.337.search-card.all.click&vd_source=f806e1845ce32bd171eeadf5991dc371

