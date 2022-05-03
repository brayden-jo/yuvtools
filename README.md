# yuvtools
YUV Tools using Python3

# Install

```
$ pip install yuvtools
```

# Usage
## y4m to yuv
```
$ python -m yuvtools.y4m2yuv examples/foreman.y4m output.yuv     // 64x64 foreman yuv
```



```
$ python -m yuvtools.psnr src1.yuv src2.yuv -s 176x144 -f 2 -c Y         // 2 frames Y channel
$ python -m yuvtools.psnr src1.yuv src2.yuv -s 176x144 -f 2 -c YUV       // 2 frames YUV channel
$ python -m yuvtools.psnr src1.yuv src2.yuv -s 176x144 -f 2 -c U         // 2 frames U channel
$ python -m yuvtools.psnr src1.yuv src2.yuv -s 176x144 -f 2 -c V         // 2 frames V channel
```
