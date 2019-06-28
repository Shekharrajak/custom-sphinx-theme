from setuptools import setup
from io import open
from spr_theme import __version__

setup(
    name = 'custom_sphinx_theme',
    version =__version__,
    author = 'Shekhar',
    author_email= 'shekharrajak@live.com',
    url="https://github.com/shekharrajak/custom-sphinx-theme",
    docs_url="https://github.com/shekharrajak/custom-sphinx-theme",
    description='Custom Sphinx Theme',
    py_modules = ['custom_sphinx_theme'],
    packages = ['spr_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'custom_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/images/*.*'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'custom_sphinx_theme = spr_theme',
        ]
    },
    license= 'MIT License',
    install_requires=[
       'sphinx'
    ]
)
