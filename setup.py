from setuptools import setup, find_packages

setup(
    name='tea-weather-app',  # Yeni adı buraya ekleyin
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.26.0',
    ],
    entry_points={
        'console_scripts': [
            'new-weather-app=weather_app.main:main',
        ],
    },
)