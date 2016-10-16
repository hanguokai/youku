from setuptools import setup


setup(
    name='youku',
    version='0.0.9',
    description='Youku open api python client and video uploader',
    long_description='Youku open api python client,'
    '  support video upload and other api, do not support video download.',
    url='https://github.com/hanguokai/youku',
    author='Guokai Han',
    author_email='han.guokai@gmail.com',
    packages=['youku'],
    keywords='youku api upload video',
    install_requires=['requests'],

    classifiers=[
        "Topic :: Multimedia :: Video",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python"
    ],
)
