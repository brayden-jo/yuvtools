#/usr/bin/env python3
import subprocess

def y4m2yuv(src, dst):
    cmd = f"ffmpeg -i {src} {dst}"
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv2y4m(src, dst, width, height, format="yuv420p"):
    cmd = f"ffmpeg -video_size {width}x{height} -pix_fmt {format} -i {src} {dst}"
    subprocess.run(cmd, shell=True, encoding='utf-8')

def video2yuv(src, dst, format="yuv420p"):
    cmd = f'ffmpeg -i {src} -c:v rawvideo -pixel_format {format} {dst}'
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_trim(src, dst, width, height, start_frame=0, frame_num=60, format="yuv420p"):
    end_frame = start_frame + frame_num
    cmd = f"ffmpeg -video_size {width}x{height} -pixel_format {format} -i {src} -f rawvideo -vf trim=start_frame={start_frame}:end_frame={end_frame} {dst}"
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_crop(src, dst, width, height, h, w, x, y, format="yuv420p"):
    cmd = f'ffmpeg -video_size {width}x{height} -pixel_format {format} -i {src} -filter:v "crop={h}:{w}:{x}:y" {dst}'
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_add_number(src, dst, width, height, format="yuv420p"):
    cmd = f'''ffmpeg -video_size {width}x{height} -i {src} -c:v rawvideo -vf "drawtext=fontfile=Arial.ttf: text='%{frame_num}': start_number=0: x=(w-tw)/2: y=h-(2*lh): fontcolor=black: fontsize=20: box=1: boxcolor=white: boxborderw=5" -pix_fmt {format} {dst}'''
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_play(src, dst, width, height, format="yuv420p"):
    cmd = f"ffplay -video_size {width}x{height} -pixel_format {format} {dst} -loop 0"
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_scale(src, dst, width, height, w, h, format="yuv420p"):
    cmd = "ffmpeg -video_size {width}x{height} -pixel_format {format} -i {src} -vf scale={w}:{h} -c:v rawvideo -pixel_format {format} {dst}"
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_add_bottom(src, dst, width, height, offset, color="black", format="yuv420p"):
    cmd = f'fmpeg -video_size {width}x{height} -pixel_format {format} -i {src} -filter_complex "[0]pad=w=iw:h=ih+{offset}:x=0:y=0:color={color}" -pixel_format {format} {dst}'
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_add_right(src, dst, width, height, offset, color="black", format="yuv420p"):
    cmd = f'fmpeg -video_size {width}x{height} -pixel_format {format} -i {src} -filter_complex "[0]pad=w=iw+{offset}:h=ih:x=0:y=0:color={color}" -pixel_format {format} {dst}'
    subprocess.run(cmd, shell=True, encoding='utf-8')

def yuv_color(dst, width, height, rate=60, duration=1, color="black", format="yuvj420p"):
    cmd = f"ffmpeg -f lavfi -i color=c=black:size={width}x{height}:rate={rate}:duration={duration} -pix_fmt {format} {dst}"
    subprocess.run(cmd, shell=True, encoding='utf-8')

if __name__ == "__main__":
    y4m2yuv(src="../examples/foreman.y4m", dst="../examples/output.yuv")