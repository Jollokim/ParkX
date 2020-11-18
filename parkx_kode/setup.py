from setuptools import setup

setup(
    name='prosjektnavn',
    version='0.0.1',
    packages=['prosjektnavn'],
    include_package_data=True,
    install_requires=[
        "Kivy",
        "kivy-deps.angle",
        "kivy-deps.glew",
        "kivy-deps.sdl2",
        "pytest",
        "pytest-mock",
        "mock",
        "freezegun"
    ],
    python_requires='>=3.5, <=3.7'
)
