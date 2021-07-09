from setuptools import setup, find_packages

setup(
    name='the-littlest-jupyterhub',
    version='0.1',
    description='A small JupyterHub distribution',
    url='https://github.com/wpinvestigative/the-littlest-jupyterhub',
    author='Aaron Williams',
    author_email='aaron.williams@washpost.com',
    license='3 Clause BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'ruamel.yaml==0.15.*',
        'jinja2',
        'pluggy>0.7<1.0',
        'passlib',
        'backoff',
        'requests',
        'jupyterhub-traefik-proxy==0.1.*'
    ],
    entry_points={
        'console_scripts': [
            'tljh-config = tljh.config:main',
        ],
    },
)
