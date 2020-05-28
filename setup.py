from setuptools import setup

setup(
    name            = 'yuvtools',
    version         = '0.0.1',
    description     = 'PSNR/BD-Rate with YUV Files',
    url             = 'https://github.com/brayden-jo/yuvtools',
    author          = 'Brayden Jo',
    author_email    = 'brayden.jo@outlook.com',
    install_requires= ['scipy', 'opencv-python'],
    license         = 'MIT',
    packages        = ['yuvtools'],
    zip_safe        = False
)