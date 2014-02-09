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


from druid import page, bootstrap, p


LOREM = p('''
According to Pastafarian "beliefs", pirates are "absolute divine beings" and
the original Pastafarians. Furthermore, Pastafarians believe that the
concept of pirates as "thieves and outcasts" is misinformation spread by
Christian theologians in the Middle Ages and by Hare Krishnas. Instead,
Pastafarians believe that they were "peace-loving explorers and spreaders of
good will" who distributed candy to small children, adding that modern
pirates are in no way similar to "the fun-loving buccaneers from history".
In addition, Pastafarians believe that ghost pirates are responsible for all
of the mysteriously lost ships and planes of the Bermuda Triangle.
Pastafarians celebrate International Talk Like a Pirate Day on September 19.
''')

IPSUM = p('''
The inclusion of pirates in Pastafarianism was part of Henderson's original
letter to the Kansas State Board of Education, in an effort to illustrate
that correlation does not imply causation.[39] Henderson presented the
argument that "global warming, earthquakes, hurricanes, and other natural
disasters are a direct effect of the shrinking numbers of pirates since the
1800s". A chart accompanying the letter (with numbers humorously disordered on
the x-axis) shows that as the number of pirates decreased, global
temperatures increased. This parodies the suggestion from some religious
groups that the high numbers of disasters, famines, and wars in the world is
due to the lack of respect and worship toward their deity. In 2008, Henderson
interpreted the growing pirate activities at the Gulf of Aden as additional
support, pointing out that Somalia has "the highest number of pirates and the
lowest carbon emissions of any country".
''')


def test_page():
    pg = page()
    assert pg


def test_bootstrap_starter():
    pg = bootstrap.starter(
        menu=('My website', 'home', 'about', 'contact'),
        title='Hello World',
        body=(LOREM, IPSUM),
        )
    assert pg
    print(pg.build())
