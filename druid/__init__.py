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


import tumulus.lib as lib
from tumulus.tags import tags as t
import tumulus.formulas as f

__all__ = ('p',
           'page',
           'bootstrap',
           )

p = t.p


def page(title=None):
    return True


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

    def starter(title='', body='', menu=()):
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
