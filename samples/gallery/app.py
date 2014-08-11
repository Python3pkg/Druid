 # -*- coding: utf-8 -*-

# This file is part of Druid.
#
# Copyright (C) 2014 OKso (http://okso.me)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import listdir
from os.path import dirname, realpath, join

from bottle import Bottle, static_file
from druid import Druid, bootstrap

from tumulus.tags import tags as t

HERE = dirname(realpath(__file__))

app = Bottle()
druid = Druid(local_static=join(HERE, 'static'))


def list_images():
    return (i for i in listdir(druid.image_dir) if i.endswith('.png'))


def image_with_legend(name, legend):
    return t.div(
        druid.image(name, alt=legend).thumb((200, 200)),
        t.div(legend),
        style='width: 220px; border: 2px solid; margin: 10px',
        )


@app.get('/')
def index():
    print(listdir(druid.image_dir))
    page = druid.page(
        'hello',
        [image_with_legend(i, i)
         for i in list_images()]
        )
    return page.build()


@app.get('/boot')
def boot():
    content = {
        'menu': ('My website', 'home', 'about', 'contact'),
        'title': 'Hello World',
        'body': [image_with_legend(i, i)
                 for i in list_images()],
    }

    return bootstrap.page_starter(**content).build()


@app.get('/static/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(
        filename,
        root=druid.local_static,
        )


app.run(debug=True, reloader=True)
