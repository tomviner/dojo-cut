import pytest
from cut import _cut


@pytest.mark.parametrize('f, expected',
    [
        ['1', '1']
        ['2,3', '2, 3']
    ],
)
def test(f, expected):
    result = _cut(input='1|2|3|4|5|6|7|8|9', d='|', f=f)
    line = ''.join(result)
    assert line == expected
