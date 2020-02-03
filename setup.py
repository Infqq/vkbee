import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vkbee",
    version="0.1",
    author="YamkaFox",
    author_email="cryptoyamafox@gmail.com",
    description="Simple Async VKLibrary faster than vk_api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyncvk/vkbee",
    packages=setuptools.find_packages(),
    license="LGPLv3",
    keywords="vk api framework python",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Mozilla Public License 2.0",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Github": "https://github.com/asyncvk/vkbee",
        "Documentation": "https://github.com/asyncvk/vkbee",
    },
    python_requires=">=2",
    install_requires=[
        "aiohttp",
        "requests"
    ]
)