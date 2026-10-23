import setuptools

setuptools.setup(
    name="beets-mood",
    version="0.0.1",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/MaartenBehn/beets-mood",
    license="MIT",
    platforms="ALL",
    packages=["beetsplug"],
    namespace_packages=["beetsplug"],
    install_requires=["beets"],
    classifiers=[
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
