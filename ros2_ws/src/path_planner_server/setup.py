from setuptools import setup
import os
from glob import glob

package_name = 'path_planner_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'nav_to_pose = path_planner_server.nav_to_pose_action_client:main',
        'nav_to_pose2 = path_planner_server.nav_to_pose2:main',
        'spot_recorder = path_planner_server.spot_recorder:main',

        ],
    },
)