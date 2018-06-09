Pelican blog with Github Pages (Github.io)
##########################################

:date: 2018-06-09 22:15
:modified: 2018-06-09 22:15
:tags: Blog Pelican Python Github Pages Github.io
:category: Pelican GitHub Structure Github.io Pages
:authors: Kairo Araujo

This post is how I use Pelican. I guess I found a good way to have it. Keep in
mind, I didn't create this way fully by my self, I went to different blog posts
and I decided that way was easy to me.

I am trying to use Pelican for a while and finally I created a good/easy way.

Resources
=========

First I use GitHub.io (Github Pages) to publish my blog

I will not cover this part, it can be find well described here
https://pages.github.com

My repository is ``kairoaraujo.github.io`` as standard for GitHub Pages.
https://github.com/kairoaraujo/kairoaraujo.github.io


Pelican installation
====================

Pelican has a very good documentation. I suggest you to read it
http://docs.getpelican.com/en/stable/

There are dozen of blog posts how to do it.


Structure on Github
===================

After you have your blog working locally is time to publish it and here is may
way to do it. It is quite simple and works well.


Source branch (pelican)
-----------------------

First I created a branch named ``pelican``. It has my folder that I used to
create my blog, using the ``pelican-quickstart``

This is my example:

.. code-block:: txt

  kairo.eti.br
  ├── Makefile
  ├── README.rst
  ├── content
  ├── develop_server.sh
  ├── extras
  ├── fabfile.py
  ├── output
  ├── pelicanconf.py
  ├── publishconf.py
  └── themes
      └── pelican-clean-blog

In ``pelican`` branch I created my ``.gitignore`` excluding some files

The most important here is exclude the *output* folder. Because it is my
blog/site content itself and I want it on different branch.

.. code-block:: txt

    .idea
    *.pyc
    *.log
    output   <---------- Important!
    cache
    *.pid
    venv
    .venv
    .ropeproject

I use a theme and I store it in ``themes/pelican-clean-blog``. As this theme is
available in Github (as most of them) I store it using ``git submodule add``. It
makes easy to keep it updated and linked to my repository

I did like that:

``git submodule add https://github.com/gilsondev/pelican-clean-blog.git themes/pelican-clean-blog``

TIP: About ``CNAME`` used by Github pages, I store it in extras folder and
setup in ``pelicanconf.py``

Blog branch (master)
--------------------

It is the blog itself.

As the folder ``output`` is excluded in my pelican branch what I did was create
in output as a new git repository as my master branch. ;)

TIP: Do not use the overwrite option from Pelican and I recommend include this
option on your ``pelicanconf.py`` and ``publishconf.py``.

``DELETE_OUTPUT_DIRECTORY = False``

Using
=====

Now is easy to me to use my blog. I just follow the instructions that I wrote
to myself in my ``README.rst`` on pelican branch :D

Basically 4 steps:

1. Just rst files in content :D

2. ``pelican -s publishconf.py``

3. Preview: ``cd output && python3 -m http.server``

4. Commit branches pelican and master
