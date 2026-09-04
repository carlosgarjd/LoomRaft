# test_loomraft.py
"""
Tests for LoomRaft module.
"""

import unittest
from loomraft import LoomRaft

class TestLoomRaft(unittest.TestCase):
    """Test cases for LoomRaft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoomRaft()
        self.assertIsInstance(instance, LoomRaft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoomRaft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
