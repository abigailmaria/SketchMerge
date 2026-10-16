# test_sketchmerge.py
"""
Tests for SketchMerge module.
"""

import unittest
from sketchmerge import SketchMerge

class TestSketchMerge(unittest.TestCase):
    """Test cases for SketchMerge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchMerge()
        self.assertIsInstance(instance, SketchMerge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchMerge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
