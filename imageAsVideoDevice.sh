#!/bin/bash
# $1 image file
ffmpeg -loop 1 -re -i $1 -f v4l2 -vcodec rawvideo -pix_fmt yuv420p /dev/video1
