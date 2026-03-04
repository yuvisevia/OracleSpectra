# test_oraclespectra.py
"""
Tests for OracleSpectra module.
"""

import unittest
from oraclespectra import OracleSpectra

class TestOracleSpectra(unittest.TestCase):
    """Test cases for OracleSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleSpectra()
        self.assertIsInstance(instance, OracleSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
