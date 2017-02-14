from setuptools import setup

setup(name='bewire-todo',
      version='1.0',
      description='Bewire Python Intro TODO app.',
      long_description='Todo app created as introduction to Python on the Bewire Python Introduction session',
      classifiers=[
        'Intended Audience :: Developers',
        'License :: © 2015 VIAA',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='todo bewire introduction',
      author='Jonas Liekens',
      author_email='jonas.liekens@c4j.be',
      license='GNUv3',
      packages=['todo'],
      install_requires=[
          'tabulate',
      ],
      entry_points={
          'console_scripts': ['todo=todo.main:execute'],
      },
      include_package_data=True,
      zip_safe=False)
