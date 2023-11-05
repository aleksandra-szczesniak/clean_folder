from setuptools import setup

setup(
    name="clean-folder",
    version="1.0",
    packages=["clean_folder"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:clean_folder"
        ]
    }
)