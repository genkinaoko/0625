#必要なライブラリの宣言
from skimage import data, io
from sklearn.cluster import MeanShift, estimate_bandwidth

#組み込みデータ
image = data.camera()
print(image.shape)

#MeanShift前の画像保存先指定 ※要入力
image_path = r""
io.imsave(image_path, image)

#MeanShiftクラスタリング実行
x = image.reshape((-1, 1))
bandwidth = estimate_bandwidth(x, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(x)

#結果画像の保存　
segmented_image = ms.labels_
segmented_image.shape = image.shape
io.imsave("result.png", segmented_image)
