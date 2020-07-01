from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'alexflipnote.py',
    description = 'An easy to use Python Wrapper for the AlexFlipnote API',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    version = '1.2.6',
    packages = ['alexflipnote'],
    url = 'https://github.com/Soheab/Alexflipnote.py',
    download_url = 'https://github.com/Soheab/alexflipnote.py/archive/1.2.6.tar.gz',
    license = 'MIT',
    author = 'Soheab_',
    install_requires = ['aiohttp', 'url_regex'],
    keywords = ['alexflipnote', 'discord'],
    project_urls = {
        "Discord": "https://discord.gg/alexflipnote",
        "Source": "https://github.com/Soheab/alexflipnote.py",
        "Documentation": "https://github.com/Soheab/alexflipnote.py/blob/master/docs.md",
        "Issue tracker": "https://github.com/Soheab/alexflipnote.py/issues",
    },

    python_requires = '>=3.6',
)
