from utils import add, diff, wiki_summary

def test_add():
    assert 2 == add(1,1)

def test_diff():
    assert 3 == diff(2,5)

def test_wiki_summary():
    assert "Microsoft" in wiki_summary()