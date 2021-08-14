# Built-int imports
import os
import sys

# External imports 
import cv2 as cv
import numpy as np

# My Own imports
import get_path_assests_folder as gpaf

# Get assets folder in repo for the samples
ASSETS_FOLDER = gpaf.get_assets_folder_path()


def load_image():
    image_relative_path = os.path.join(
        ASSETS_FOLDER, "imgs", "Tony_Stark.jpeg")

    bgr_image = cv.imread(image_relative_path,1)
    gray_image = cv.imread(image_relative_path,0)
    return bgr_image, gray_image


def plot_histogram(window, gray_image):
    # Define the dimensions of the plot
    wbins = 256
    hbins = 256

    #cv.calcHist(images, channels, mask, histSize, ranges)
    histr = cv.calcHist([gray_image],[0],None,[hbins],[0,wbins])
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(histr)
    hist_image = np.zeros([hbins, wbins], np.uint8)

    # Plot the lines to make the histogram
    for w in iter(range(wbins)):
        binVal = histr[w]
        intensity = int(binVal*(hbins-1)/max_val)
        cv.line(hist_image, (w,hbins), (w,hbins-intensity),255)
        cv.imshow(window,hist_image)


def ajuste_gamma(image, gamma):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
    for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv.LUT(image, table)


def main():
    bgr_image, gray_image = load_image()
    bgr_image = cv.resize(bgr_image,(320,240))
    gray_image = cv.resize(gray_image,(320,240))

    cv.imshow("BGR IMAGE", bgr_image)
    cv.imshow("GRAY IMAGE", gray_image)
    plot_histogram("ORIGINAL HISTOGRAM",gray_image)
    cv.waitKey()
    cv.destroyAllWindows()
    
    return 0
    ret, img_bin = cv.threshold(gray_image, 210,255, cv.THRESH_BINARY)
    img_gama = ajuste_gamma(bgr_image,1.5)
    cv.imshow("Gamma",img_gama)
    h,w = gray_image.shape[:2]
    total = h*w
    count = 0
    #print (gray_image[0])
    ## for y in range(h):
    ## for x in range(w):
    ##
    ## #gray_image[y,x] = gray_image[y,x]*2
    ## gray_image[y,x] = int(pow(gray_image[y,x],2)/np.max(gray_image))
    ## if(gray_image[y,x] >255):
    ## gray_image[y,x]=255
    ## if (gray_image[y,x]<100 and gray_image[y,x]>60):
    ## gray_image[y,x] = gray_image[y,x] + 30
    ## #count = count + 1
    ## if (gray_image[y,x]<=60 and gray_image[y,x]>20):
    ## gray_image[y,x] = gray_image[y,x] + 10

    mostrar_imagen("img_bin",img_bin)
    #mostrar_imagen("Gris_New",gray_image)
    #ret, img_bin2 = cv.threshold(gray_image, 210,255, cv.THRESH_BINARY)
    #mostrar_imagen("img_bin2",img_bin2)
    #print((count*100.0)/(1.0*total))
    cv2.waitKey(0)
    cerrar_ventana()

if __name__=="__main__":
    sys.exit(main())