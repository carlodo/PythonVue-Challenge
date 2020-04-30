from setuptools import find_packages, setup


install_requires = ['aiohttp==3.6.2',
                    'pyjwt==1.7.1',
                    'pymongo==3.9.0',
                    'bcrypt==3.1.7']
tests_require = ['pylama==7.7.1']
dev_require = ['aiohttp-devtools==0.13.1']


setup(
    name='moti',
    version='0.0.0',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={'tests': tests_require,
                    'dev': tests_require + dev_require}
)
