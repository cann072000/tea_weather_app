from setuptools import setup, find_packages

setup(
    name='tea-weather-app',  # Yeni adı buraya ekleyin
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'eaddaa-game==0.1.0',
    ],
    entry_points={
        'console_scripts': [
            'new-weather-app=weather_app.main:main',
        ],
    },
    url='https://github.com/cann072000/tea-weather-app',  # GitHub deposunun URL'sini ekleyin
)
