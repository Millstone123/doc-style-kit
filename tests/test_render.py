import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from doc_style.reporter import run

def test_render():
    assert isinstance(run(), str)
