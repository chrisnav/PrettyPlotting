from setuptools import find_packages, setup

setup(
    name='PrettyPlotting',
    packages=find_packages(include=['PrettyPlotting']),
    version='0.1.0',
    description='A simple matplotlib wrapper',
    url = 'https://github.com/chrisnav/PrettyPlotting',
    author='Christian Øyn Naversen',
    author_email='christian.oyn.naversen@gmail.com',
    install_requires=['matplotlib>=3.4.1'],
    license='MIT',
)