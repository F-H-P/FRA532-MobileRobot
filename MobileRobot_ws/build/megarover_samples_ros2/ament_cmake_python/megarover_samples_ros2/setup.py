from setuptools import find_packages
from setuptools import setup

setup(
    name='megarover_samples_ros2',
    version='0.0.0',
    packages=find_packages(
        include=('megarover_samples_ros2', 'megarover_samples_ros2.*')),
)
