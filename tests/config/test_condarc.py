import pytest

from honda.config.condarc import CondarcConfig, merge_condarc

MERGE_TEST_PARAMS = [
    (
        CondarcConfig(channels=["bloop"]),
        CondarcConfig(channels=["bleep"]),
        {"channels": ["bleep"]},
    ),
]


@pytest.mark.parametrize("con,con1,expected", MERGE_TEST_PARAMS)
def test_merge_condarc(con, con1, expected):
    con2 = merge_condarc(con, con1)

    for fld, val in expected.items():
        assert getattr(con2, fld) == val
