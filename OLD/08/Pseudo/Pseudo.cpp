#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgproc/imgproc_c.h"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/opencv.hpp"
#include "stdlib.h"
#include "stdio.h"

#define N 8

using namespace cv;
using namespace std;

int main( int argc, char** argv ){

    Mat src = imread(argv[1], 1);
    Mat scale = imread("./scales/colorscale_rainbow.jpg", 1);
    Mat output = src;
    Mat src_hsv;
    double min = 0.6, max = 1.0;

    if( !src.data ){
	return -1;
    }

    cvtColor(src, src_hsv, CV_BGR2HSV);

    printf("%d %d\n", scale.rows, scale.cols);
    printf("%d %d %d\n", scale.at<Vec3b>(0,150)[0], scale.at<Vec3b>(0,150)[1], scale.at<Vec3b>(0,150)[2]);

    for (int i = 0; i < src.rows; i++){
   	for (int j = 0; j < src.cols;  j++) {

	    double hue = src_hsv.at<Vec3b>(i,j)[1];
	    hue = hue / 360.0;

	    if(hue > min){
	    	// blue
	    	output.at<Vec3b>(i,j)[0] = scale.at<Vec3b>(0,(int)((255*(hue-min))/(max-min)))[0];
 
	    	// green
	    	output.at<Vec3b>(i,j)[1] = scale.at<Vec3b>(0,(int)((255*(hue-min))/(max-min)))[1];

	    	// red
	    	output.at<Vec3b>(i,j)[2] = scale.at<Vec3b>(0,(int)((255*(hue-min))/(max-min)))[2];
	    }
   	}
    }

    imshow("sample", output);

    waitKey(0);
}
