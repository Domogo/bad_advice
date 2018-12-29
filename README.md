# AnyAdvice

Simple Django + Python3 app that works with Advice Slip API <https://api.adviceslip.com/>

# Setup:

  - create a virtualenv and activate it
  - install Django==2.1.4 and requests
  - clone this repo

### Usage:
  - catch new advice using management command: python manage.py getNewAdvice
  - go to http://127.0.0.1:8000/ to see latest advice
  - use links on the homepage to see all advice or receive a random one
