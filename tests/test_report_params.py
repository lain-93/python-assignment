import pytest
from ..src.reportinput import gen_params, extract_items, extract_common_items


def test_():
    """
    This is just a stub to get you started. Please change anything to improve.
    """

testdata = [
    ('Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox', 'Frog  apple    fox cat fish fish', {'fish', 'frog', 'fox', 'apple'}),
    ('TrEe:NEAT:  Company, SucCess    : QA', 'qa; test/     Sample, succeSS', {'qa', 'success'})
    ]


@pytest.mark.parametrize("a, b, expected", testdata)
def test_gen_params_success(a, b, expected):
    returned = set(gen_params(a, b))
    assert expected == returned


def test_gen_params_failure():
    expected = {'fush', 'frog', 'fox', 'apple'}
    returned = set(gen_params('Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox', 'Frog  apple    fox cat fish fish'))
    assert expected != returned


def test_gen_params_failure_exit_one():
    with pytest.raises(SystemExit) as exitinfo:
        gen_params('Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox', ' ')

    assert exitinfo.value.code == 1


def test_extract_items():
    expected = ['dog', 'catfish', 'frog', 'fish', 'apple', 'monkey', 'apple', 'fox']
    returned = extract_items('Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox')

    assert expected == returned 


def test_extract_common_items():
    expected = {'fish', 'frog', 'fox', 'apple'}
    returned = set(extract_common_items(
        ['dog', 'catfish', 'frog', 'fish', 'apple', 'monkey', 'apple', 'fox'],
        ['frog', 'apple', 'fox', 'cat', 'fish', 'fish'])
        )
    
    assert expected == returned 