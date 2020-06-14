from setuptools import setup

setup(
    name = 'alexflipnote-api',
    version = '0.2',
    packages = ['alexflipnote-api'],
    url = 'https://github.com/Soheab/Alexflipnote_api',
    download_url = 'https://github.com/Soheab/alexflipnote_api/archive/1.1.tar.gz',
    license = 'MIT',
    author = 'Soheab',
    author_email = '',
    install_requires=['aiohttp', 'url_regex'],
    description = 'A easy to use Wrapper for the AlexFlipnote API'
)
