# This file is part of Gentooza's web page
#
# Copyright 2021-2022, Joaquín Cuéllar <joa.cuellar (at) riseup (dot) net>
#
# Gentooza's web page is free software:
# you can redistribute it and/or modify it under the terms of
# the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gentooza's web page is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Gentooza's web page.
# If not, see <https://www.gnu.org/licenses/>.
import datetime
import os
import sys
sys.path.append(os.curdir)

import projects

AUTHOR = 'Joaquín Cuéllar'
SITENAME = "Gentooza's web page"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./theme"
PROFILE_IMAGE_URL = "https://gentooza.pixelada.org/wp-content/uploads/2018/10/gentooza_title.gif"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/index.html'),
    ('Sobre mí', '/pages/sobre-mi.html'),
    ('Proyectos', '/pages/proyectos.html'),
    ('Contacto', '/pages/contacto.html'),
)
LICENSE_URL="https://www.gnu.org/licenses/agpl-3.0.html"
LICENSE_NAME="AGPLv3+"

CURRENT_YEAR = datetime.datetime.now().year

PROY_CATEGORIES = projects.CATEGORIES

PROJECTS = projects.projects
