import unittest
import dotconfig
import tempfile
import os.path
import ConfigParser


class TestDotConfig(unittest.TestCase):
    # Reading files and dicts
    # reading sections
    # reading values

    def test_initializaton(self):
        dotconfig.Config(tempfile.TemporaryFile())

    def test_no_file(self):
        with self.assertRaises(TypeError):
            dotconfig.Config(None)

    def test_sections(self):
        c = dotconfig.Config(self._test_data())
        c.MySection
        c.MyData
        c.Foobar

    def test_values(self):
        c = dotconfig.Config(self._test_data())

        # optionxform in ConfigParser converts
        # options to lower case by default.
        c.MySection.abool
        c.MySection.astring
        c.MySection.afloat
        c.MySection.anint

    def test_missing_section(self):
        c = dotconfig.Config(self._test_data())
        with self.assertRaises(ConfigParser.NoSectionError):
            c.MissingSection

    def test_missing_value(self):
        c = dotconfig.Config(self._test_data())
        with self.assertRaises(ConfigParser.NoOptionError):
            c.MySection.MissingOption

    def _test_data(self):
        cwd = os.path.dirname(__file__)
        return os.path.join(cwd, "test_data.cfg")
