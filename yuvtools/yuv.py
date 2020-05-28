import numpy as np


def read_yuv420_frame(file, width, height, frame_index=0, bit_depth=8):
    size = int(width * height * 3 / 2)
    offset = size * frame_index

    frame = np.fromfile(file, dtype='uint8', offset=offset)

    y_start = 0
    y_end = width * height

    u_start = y_end
    u_end = u_start + int(width * height / 4)

    v_start = u_end
    v_end = v_start + int(width * height / 4)

    y = frame[y_start:y_end].reshape(height, width)
    u = frame[u_start:u_end].reshape(int(height/2), int(width/2))
    v = frame[v_start:v_end].reshape(int(height/2), int(width/2))

    return frame, y, u, v



