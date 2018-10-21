#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgproc/imgproc_c.h"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/opencv.hpp"
#include "stdlib.h"
#include "stdio.h"

using namespace cv;
using namespace std;

string colormap(int id)
{
    switch(id){
        case COLORMAP_AUTUMN :
            return "COLORMAP_AUTUMN";
        case COLORMAP_BONE :
            return "COLORMAP_BONE";
        case COLORMAP_JET :
            return "COLORMAP_JET";
        case COLORMAP_WINTER :
            return "COLORMAP_WINTER";
        case COLORMAP_RAINBOW :
            return "COLORMAP_RAINBOW";
        case COLORMAP_OCEAN :
            return "COLORMAP_OCEAN";
        case COLORMAP_SUMMER:
            return "COLORMAP_SUMMER";
        case COLORMAP_SPRING :
            return "COLORMAP_SPRING";
        case COLORMAP_COOL :
            return "COLORMAP_COOL";
        case COLORMAP_HSV :
            return "COLORMAP_HSV";
        case COLORMAP_PINK :
            return "COLORMAP_PINK";
        case COLORMAP_HOT :
            return "COLORMAP_HOT";
        
    }
    
    return "NONE";
}

int main( int argc, char** argv ){

    Mat src = imread(argv[1], IMREAD_GRAYSCALE);
    Mat output = Mat::zeros(src.rows, src.cols, CV_8UC3);

    if( !src.data ){
	return -1;
    }

    for (int i=0; i<12; i++){
	applyColorMap(src, output, i);
	imshow(colormap(i), output);
    }

    waitKey(0);
}
