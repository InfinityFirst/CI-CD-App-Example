from src.app import index

def test_index():
    assert index() == "First CI-CD Flask app"