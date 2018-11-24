from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

extras_require = {
    
}

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='WarframeAlertBot',
      version='0.0.1-dev',
      description='Discord bot that will post Warframe Alerts',
      url='https://github.com/systemkaos/WarframeAlertBot',
      author='Mark Pierce',
      author_email='mark.pierce.d@gmail.com',
      license='MIT',
      long_description=readme,
      install_requires=requirements,
      extras_require=extras_require,
      zip_safe=False)