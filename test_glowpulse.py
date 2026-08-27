# test_glowpulse.py
"""
Tests for GlowPulse module.
"""

import unittest
from glowpulse import GlowPulse

class TestGlowPulse(unittest.TestCase):
    """Test cases for GlowPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlowPulse()
        self.assertIsInstance(instance, GlowPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlowPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
