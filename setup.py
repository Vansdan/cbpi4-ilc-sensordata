from setuptools import setup

setup(name='cbpi4-ilc-sensordata',
      version='0.0.1',
      description='Generic CraftBeerPi ILC Sensor Plugin',
      author='Daniel Lauterbach',
      author_email='vansdan@web.de'
      url='https://github.com/vansdan/cbpi4-ilc-sensordata',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-http-actor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-ilc-sensordata'],
      install_requires=[
            'cbpi>=4.0.0.34',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
