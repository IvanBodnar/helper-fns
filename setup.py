from setuptools import setup, find_packages

setup(
    name="helper_fns",
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points='''
        [console_scripts]
    ''',
)
