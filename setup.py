import setuptools

install_requires = [
    'scipy',
    'opencv-python'
]

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='yuvtools',
    version='0.0.2',
    author='Brayden Jo',
    author_email='brayden.jo@pyquant.co.kr',
    description="utils for YUV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/brayden-jo/yuvtools',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)