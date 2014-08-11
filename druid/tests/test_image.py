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

from os import remove
from os.path import dirname, realpath, join, isfile

from druid import Druid


HERE = dirname(realpath(__file__))

def local_druid():
    return Druid(local_static=join(HERE, 'static'))


def test_image():
    druid = local_druid()
    i = druid.image('druid_circle.jpg', alt='Druid Circle')
    assert i

    result = i.build()
    assert result == \
        '<img alt="Druid Circle" src="/static/img/druid_circle.jpg"/>\n'

    assert i.file_path() == join(HERE, 'static', 'img', 'druid_circle.jpg')

    f = i.file()
    assert f
    data = f.read()
    assert data
    assert len(data) == 226450


def test_thumbnail():
    thumb_path = join(HERE, 'static', 'thumb', 'druid_circle-100x100.jpg')
    if isfile(thumb_path):
        remove(thumb_path)

    druid = local_druid()
    i = druid.image('druid_circle.jpg', alt='Druid Circle')
    t = i.thumb((100, 100))
    assert i
    assert t

    result = t.build()
    assert result == (
        '<img alt="Druid Circle"'
        ' src="/static/thumb/druid_circle-100x100.jpg"/>\n')

    assert t.file_path() == thumb_path
    assert isfile(t.file_path())

    # Thumbnail filesize should be smaller than original
    assert len(i.file().read()) > len(t.file().read())