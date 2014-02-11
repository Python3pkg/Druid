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

__author__ = "OKso <okso.me>"
__version__ = '0.1'

from os.path import join

import tumulus.lib as lib
from tumulus.tags import tags as t
import tumulus.formulas as f

__all__ = ('p',
           'page',
           'bootstrap',
           )

p = t.p


class Image:

    def __init__(self, druid, path, alt):
        self.druid = druid
        self.path = path
        self.alt = alt

    def soup(self):
        return t.img(
            src=join(
                self.druid.public_static,
                self.druid.image_prefix,
                self.path,
                ),
            alt=self.alt,
            ).soup()

    def build(self):
        return self.soup().prettify()

    def file_path(self):
        return join(
            self.druid.local_static,
            self.druid.image_prefix,
            self.path
            )

    def file(self, mode='rb'):
        return open(
            self.file_path(),
            mode=mode,
            )


class Druid:

    def __init__(
            self,
            local_static='static',
            public_static='/static',
            image_prefix='img'):
        self.local_static = local_static
        self.public_static = public_static
        self.image_prefix = image_prefix

    def page(self, *args, **kwargs):
        return t.html(
            t.head(
                f.utf8(),
                ),
            t.body(*args, **kwargs),
            )

    def image(self, path, alt):
        return Image(self, path, alt)


class bootstrap:

    def navbar(items):
        title, items = items[0], items[1:]
        return t.div(
            t.div(
                t.div(
                    t.button(
                        t.span("Toggle navigation", class_="sr-only"),
                        t.span(class_="icon-bar"),
                        t.span(class_="icon-bar"),
                        t.span(class_="icon-bar"),
                        class_="navbar-toggle",
                        **{"data-toggle": "collapse",
                           "data-target": ".navbar-collapse"}
                        ),
                    t.a(
                        title,
                        class_="navbar-brand",
                        ),
                    class_="navbar-header",
                    ),
                t.div(
                    t.ul(
                        [
                            t.li(t.a(item, href=item))
                            for item in items
                            ],
                        class_="nav navbar-nav",
                        ),
                    class_="collapse navbar-collapse",
                    ),
                class_="container",
                ),
            class_="navbar navbar-inverse navbar-fixed-top",
            role="navigation",
            )

    def page_starter(title='', body='', menu=()):
        navbar = bootstrap.navbar(menu) if menu else ()
        print('navbar', navbar)

        return t.html(
            lib.css('bootstrap'),
            lib.css('bootstrap-theme'),
            lib.js('jquery'),
            lib.js('bootstrap'),

            t.head(
                f.utf8(),
                f.IEedge(),
                f.viewport(),

                t.title(title),
                ),
            t.body(
                navbar,

                t.div(
                    t.h1(title),
                    t.div(
                        body
                        ),
                    class_='container',
                    ),
                style="padding-top: 50px;",
                ),
            )
