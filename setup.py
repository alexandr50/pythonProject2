from setuptools import setup

setup(
   name='wsgi_framework',
   version='1.0',
   description='Is a pretty simple wsgi framework',
   author='Maslov Alexandr',
   author_email='dmitrymaslov2016@mail.ru',
   packages=['wsgi_framework'],
   install_requires=['jinja2', 'gunicorn']
)