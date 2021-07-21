#include <opencv2/opencv.hpp>
 
int main(void)
{
	// 画像を格納するオブジェクトを宣言する
	cv::Mat	image;
 
	// 画像ファイルから画像データを読み込む
	image = cv::imread("C:/opencv/sources/samples/data/lena.jpg");
 
	if (image.empty() == true) {
		// 画像データが読み込めなかったときは終了する
		return 0;
	}
 
	// ウィンドウに画像を表示する
	// # ここではウィンドウに「画像」という識別名を付けている
	cv::imshow("画像", image);
 
	// 何かキーが押されるまで待つ
	cv::waitKey();
 
	r