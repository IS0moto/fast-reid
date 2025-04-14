from setuptools import find_packages, setup

setup(
    name="fastreid",
    version="1.0.0",
    author="Xingyu Liao",
    author_email="sherlockliao01@gmail.com",
    description="FastReID: A research framework for person re-identification based on PyTorch.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JDAI-CV/fast-reid",
    packages=find_packages(exclude=("configs", "tests", "docs")),
    include_package_data=True,
    install_requires=[
        "torch>=1.4",
        "torchvision>=0.5.0",
        "yacs>=0.1.6",
        "termcolor",
        "tqdm",
        "opencv-python",
        "tensorboardX",
        "scipy",
        "scikit-learn",
        "matplotlib",
        "Pillow",
        "numpy<2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)