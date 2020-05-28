import cv2
from . import yuv
import argparse


def psnr(file1, file2, width, height, frames, start=0, channel='Y'):
    """
    Calculate PSNR for each frame
    :param file1: YUV file1 path
    :param file2: YUV file2 path
    :param width: width of the YUV
    :param height: height of the YUV
    :param frames: total number of frames for PSNR calculation
    :param start: start frame index (default=0)
    :param channel: 'Y','U','V', or 'YUV'
    :return: list of the PSNR for each frame
    """
    psnr_list = []

    for frame in range(start, frames):
        yuv1, y1, u1, v1 = yuv.read_yuv420_frame(file1, width, height, frame)
        yuv2, y2, u2, v2 = yuv.read_yuv420_frame(file2, width, height, frame)

        if channel == 'Y':
            psnr = cv2.PSNR(y1, y2)
        elif channel == 'U':
            psnr = cv2.PSNR(u1, u2)
        elif channel == 'V':
            psnr = cv2.PSNR(v1, v2)
        else:
            psnr = cv2.PSNR(yuv1, yuv2)

        psnr_list.append(psnr)

    return psnr_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # positional arguments
    parser.add_argument("file1")
    parser.add_argument("file2")

    # optional arguments
    parser.add_argument("-s", "--size", dest="size", action="store", required=True)
    parser.add_argument("-f", "--frames", dest="frames", action="store", default=1)
    parser.add_argument("-c", "--channel", dest="channel", action="store", default='Y')
    args = parser.parse_args()

    width, height = args.size.split('x')

    file1 = args.file1
    file2 = args.file2
    width = int(width)
    height = int(height)
    end = args.frames

    psnr_list = psnr(file1, file2, width, height, 2, channel='Y')
    print(psnr_list)
    print(sum(psnr_list) / len(psnr_list))


