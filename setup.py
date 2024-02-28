from setuptools import setup, find_packages

setup(
    name='tea-weather-app',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'eaddaa-game==0.1.3',
    ],
    entry_points={
        'console_scripts': [
            'new-weather-app=weather_app.main:main',
        ],
    },
    author='cann',
    author_email='savemefromthedark777@gmail.com',
    bugtrack_url='https://github.com/cann072000/tea_weather_app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Source': 'https://github.com/cann072000/tea_weather_app',
    },
)
