from yuvtools.psnr import *

file1 = "foreman_64x64.yuv"
file2 = "foreman_64x64_rec.yuv"
width = 64
height = 64

psnr_list = psnr(file1, file2, width, height, 2, channel='Y')
print(psnr_list)
print(sum(psnr_list) / len(psnr_list))