python-cli-comparison
=====================

.. image:: https://travis-ci.org/tylerdave/python-cli-comparison.svg?branch=master
  :target: https://travis-ci.org/tylerdave/python-cli-comparison

A comparison of Python CLI frameworks / packages / modules.

What is this?
-------------

There are a number of tools available to help with writing command line
applications in Python. In order to make a decision on which one(s) to use, I
thought it would be helpful to implement the same interface using each tool.

The same tests are run against each implementation to ensure they exhibit the
same behavior.

Status
------

This currently tests very basic argument parsing for the following tools:

* Argparse
* Click
* Docopt

TODOs
-----

* Support more tools
* More complex argument combinations
* Test and implement

  * Version output
  * Help output
  * User prompting
  * Input validation
  * Multi-command applications
  * File IO
  * Color output
  * Auto-completion

