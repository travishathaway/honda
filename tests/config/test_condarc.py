import pytest

from honda.config.condarc import CondaRC, merge_condarc

MERGE_TEST_PARAMS = [
    (CondaRC(channels=['bloop']), CondaRC(channels=['bleep']), {'channels': ['bleep']}),
]


@pytest.mark.parametrize("con,con1,expected", MERGE_TEST_PARAMS)
def test_merge_condarc(con, con1, expected):
    con2 = merge_condarc(con, con1)

    for fld, val in expected.items():
        assert getattr(con2, fld) == val
