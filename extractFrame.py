try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import argparse


def video_string_match(input_file_path, output_path, string_match, x, y, h, w, count, success):
    vidcap = cv2.VideoCapture(input_file_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print("The input video has %s fps" % fps)
    while success:
        # Capture frame-by-frame
        success, image = vidcap.read()
        count += 1
        if count%5 == 0 and success == True:
            file_name = "frame{}.png".format(count)
            crop_img = image[y:y+h, x:x+w]
            img_rgb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
            text_output = pytesseract.image_to_string(img_rgb)
            print("Analyzing frame:{}".format(count))
            if (text_output.find(string_match) != -1): 
                print('Identified the frame{} with string match - "{}"'.format(count, string_match))
                cv2.imwrite(output_path + "/" + file_name, image)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--coordinates', dest='coordinates', type=int, nargs='+',
                    help='Please enter coordinates from where the text needs to be extracted on a video frame in the following format -> x y h w \n (x,y) will be starting point.\n (h,w) is the height and  width from the starting point')
    parser.add_argument('--input-file-path', dest='input_file_path',  help='Provide the input file path for the video file')
    parser.add_argument('--output-file-path', dest='output_path',  help='Provide the output path where the images will be stored')
    parser.add_argument('--string-match', dest='string_match',  help='Provide the string that needs to be matched with the cropped frame')
    args = parser.parse_args()                   
    count = 0
    success = True
    video_string_match(args.input_file_path, args.output_path, args.string_match, args.coordinates[0], args.coordinates[1], args.coordinates[2], args.coordinates[3], count, success)
