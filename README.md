# Identifying text from Video Frame

## Description

This repo has the code to analyze video and extract a frame using a string match.

## Python script

The python script reads the image frame-by-frame from the video provided and then crops the image using the coordinates provided. The script will then look for the string match of the string provided with the cropped video.

```bash
optional arguments:
  -h, --help            show this help message and exit
  --coordinates COORDINATES [COORDINATES ...]
                        Please enter coordinates from where the text needs to be extracted on a video frame in the following format -> x y h w (x,y) will be
                        starting point. (h,w) is the height and width from the starting point
  --input-file-path INPUT_FILE_PATH
                        Provide the input file path for the video file
  --output-file-path OUTPUT_PATH
                        Provide the output path where the images will be stored
  --string-match STRING_MATCH
                        Provide the string that needs to be matched with the cropped frame

```

## Docker Execution Steps

1. Build the container by running the following command

```bash
    docker build -t {image_name}:v{image_version}
```

2. Run the Docker container by executing the command

```bash
    docker run -v local_dir:cont_dir opencv-tesseract:v1.0.0  --input-file-path {cont_dir)/{video_name)--output-file-path {cont_dir) --string-match "{string_to_be_matched}" --coordinates {x y h w}
```