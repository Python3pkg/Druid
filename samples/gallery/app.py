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

from os.path import dirname, realpath, join

from bottle import Bottle, static_file
from druid import Druid

HERE = dirname(realpath(__file__))

app = Bottle()
druid = Druid(local_static=join(HERE, 'static'))


@app.get('/')
def index():
    page = druid.page(
        'hello',
        druid.image('basic.png').thumb((200, 200)),
        )
    return page.build()


@app.get('/static/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(
        filename,
        root=druid.local_static,
        )


app.run(debug=True, reloader=True)
