import os
import sys

# Append top dir to system path
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)


from filter_plugins.surround_by import surround_by


L = [1, 2, 3]


def test_surround_by():
    assert surround_by(L, '"') == ['"1"', '"2"', '"3"']
    assert surround_by(L, '|') == ['|1|', '|2|', '|3|']

    assert surround_by(1, '"') == 1


test_surround_by()
