/*
    MACARAIG, Lyka G.
    2014-84047
    RUZ, Julianne Marie
    2014-04280

    Program Description: Program uses tesseract to read text input from license plates.
*/
#include <tesseract/baseapi.h>
#include <sys/time.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <string.h>
#include <opencv/highgui.h>
#include "iostream"
#include <stdlib.h>
#include <stdio.h>                                    

using namespace cv;

Mat binarization(Mat img, int threshold) {                         // image binarization
    Mat src1 = img;
    Mat src = src1;

    for(int i=0; i<src.rows; i++){                                 // then binarize
        for(int j=0; j<src.cols; j++){      
            if(src1.at<uchar>(i,j) < 150){  
                src.at<uchar>(i,j) = 255;
            } else {
                src.at<uchar>(i,j) = 0;
            }
        }
    }
    return src;                                                    // return binarized photo
}

int main() {

    // Initilize tesseract OCR engine
    tesseract::TessBaseAPI *OCR = new tesseract::TessBaseAPI();

    printf("Tesseract-ocr version: %s\n", OCR->Version());

    if(OCR->Init(NULL, "eng")) {
	fprintf(stderr, "Could not initialize tesseract.\n");
    	exit(1);
    }

    // Treat the image as a single text line
    tesseract::PageSegMode pagesegmode = static_cast<tesseract::PageSegMode>(7);
    OCR->SetPageSegMode(pagesegmode);

    Mat p1 = imread("p1.jpg", 0);               // loads images as intensity images
    Mat p2 = imread("p2.jpg", 0);               // connectedComponentsWithStats likes images loaded this way better
    Mat p3 = imread("p3.png", 0);

    Rect isolate(105, 134, 220, 45);            // cropped out the license plates to isolate them
    Mat plate1 = p1(isolate);
    Rect isolate2(341, 165, 115, 40);
    Mat plate2 = p2(isolate2);
    Rect isolate3(340, 245, 150, 70);
    Mat plate3 = p3(isolate3);

    for (int i=0; i<plate3.rows; i++) {
        for(int j=0; j<plate3.cols; j++) {
            if((i<10) && (j<29)) {
                plate3.at<Vec3b>(i,j)[0] = 255;    // blacking out the extra details so it can read the third plate better
                plate3.at<Vec3b>(i,j)[1] = 255;    
                plate3.at<Vec3b>(i,j)[2] = 255;
            }
        }
    }

    imshow("p1_Isolated", plate1);                 // show the cropped license plates
    imshow("p2_Isolated", plate2);
    imshow("p3_Isolated", plate3);

    Mat f1 = p1;
    Mat f2 = p2;
    Mat f3 = p3;

    f1 = binarization(plate1, 100);
    f2 = binarization(plate2, 150);
    f3 = binarization(plate3, 160);

    imshow("p1_Binarized", f1);                    // cropped binarized plates
    imshow("p2_Binarized", f2);
    imshow("p3_Binarized", f3);

    // Get connected components and stats
    const int connectivity_8 = 8;
    Mat labels, stats, centroids;

// for first input image

    int p1Labels = connectedComponentsWithStats(plate1, labels, stats, centroids, connectivity_8, CV_32S);
    // Print number of components
    printf("FOR p1.jpg:\n");
    printf("Number of connected components: %d\n\n", p1Labels);

    // Create images of components
    Mat component[p1Labels];
    char windowLabel[20];
    // traverse through all components
    for(int i=0; i<p1Labels; i++){
        compare(labels, i, component[i], CMP_EQ);
        sprintf(windowLabel,"Component %d", i);
        imshow(windowLabel, component[i]);

        OCR->TesseractRect(component[i].data, 1, component[i].step1(), 0, 0, component[i].cols, component[i].rows);
        const char *text = OCR->GetUTF8Text();

            std::string t(text);
            t.erase(std::remove(t.begin(), t.end(), '\n'), t.end());
        printf("Component %d: %s\n", i, t.c_str());

        delete [] text;
        printf("\n");
    }

// for second input image

    int p2Labels = connectedComponentsWithStats(plate2, labels, stats, centroids, connectivity_8, CV_32S);

    Mat component2[p2Labels];
    char windowLabel2[20];
    printf("FOR p2.jpg:\n");
    printf("Number of connected components: %d\n\n", p2Labels);

    for(int i=0; i<p2Labels; i++){
        compare(labels, i, component2[i], CMP_EQ);
        sprintf(windowLabel2,"Component %d", i);
        imshow(windowLabel2, component2[i]);

        OCR->TesseractRect(component2[i].data, 1, component2[i].step1(), 0, 0, component2[i].cols, component2[i].rows);
        const char *text = OCR->GetUTF8Text();

            std::string t(text);
            t.erase(std::remove(t.begin(), t.end(), '\n'), t.end());
        printf("Component %d: %s\n", i, t.c_str());

        delete [] text;
        printf("\n");
        
    }

// for third input image

    int p3Labels = connectedComponentsWithStats(plate3, labels, stats, centroids, connectivity_8, CV_32S);

    Mat component3[p3Labels];
    char windowLabel3[20];
    printf("FOR p3.png:\n");
    printf("Number of connected components: %d\n\n", p3Labels);

    for(int i=0; i<p3Labels; i++){
        compare(labels, i, component3[i], CMP_EQ);
        sprintf(windowLabel3,"Component %d", i);
        imshow(windowLabel3, component3[i]);

        OCR->TesseractRect(component3[i].data, 1, component3[i].step1(), 0, 0, component3[i].cols, component3[i].rows);
        const char *text = OCR->GetUTF8Text();

            std::string t(text);
            t.erase(std::remove(t.begin(), t.end(), '\n'), t.end());
        printf("Component %d: %s\n", i, t.c_str());

        delete [] text;
        printf("\n");
        
    }

    waitKey(0);

    // destroy tesseract OCR engine
    OCR->Clear();
    OCR->End();

    return 0;
    
}

//Reference for image cropping: http://answers.opencv.org/question/34591/opencv-extract-portion-of-a-mat-image/