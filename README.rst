kairo.eti.br
############

These are notes to recall myself how deploy my own site, yes it is funny truth.

I use two branches (master and pelican)

master is the website kairo.eti.br itself.
pelican is the branch with sources used to generate the website

Structure
=========

.. code-block::

  /
  /themes/pelican-clean-blog -> submodule [in pelican branch]
  /output                    -> master branch


Preparing local data
====================

1. Clone the pelican branch in kairo.eti.br folder

``git clone -b pelican --recursive http://github.com/kairoaraujo/kairoaraujo.github.io kairo.eti.br``

2. Clone the master branch to output folder

.. code-block::

  cd kairo.eti.br
  git clone http://github.com/kairoaraujo/kairoaraujo.github.io output

Writing posts/contents
======================

Just rst files in content :D

``pelican -s publishconf.py``

Preview

.. code-block::

  cd output
  python3 -m http.server


Publishing
==========

Just commit and push the branches :D
