from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='click-conf',
    author='Moshe Zada',
    version='0.0.1',
    keywords=['click', 'conf', 'cli', 'yaml', 'python', 'json', 'config'],
    url='https://github.com/Moshe/click-conf',
    py_modules=['click_conf'],
    license='',
    long_description=long_description,
    description='Load default click configurations from file',
    install_requires=[
        'click',
        'pyaml'
    ],
    tests_require=[
        'pytest'
    ]
)
