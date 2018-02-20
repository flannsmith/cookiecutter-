'''
Created on 13 Feb 2018

@author: lindasmith
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Linda Smith",
      author_email="linda.smithjameson@ucdconnect.ie",
      license="MIT",
      package_dir={'':'systeminfo'},
      packages=[''],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.sysinfo:getplatforminfo']
          }
      )

