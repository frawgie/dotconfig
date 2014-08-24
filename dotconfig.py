"""A simpler way to read configuration files.

dotconfig provides a very simple way to read options
from a config file. It is currently read-only.

Example:

    --- data.config ---

    [network]
    port: 8080

    --- eof ---

    --- example.py ---

    config = dotconfig.Config("data.config")
    config.network.port # returns the port number as string

    --- eof ---
"""
import ConfigParser


class Config(object):
    """Contains the configuration data.

    The configuration is read at initialization
    and you read sections and options as attributes
    of the class, e.g. config.my_section.my_value
    where my_sectiona and my_value are data in
    your config file.

    Attributes:
        You access your config file sections as
        attributes.

    """

    def __init__(self, config_file):
        """Create the parser and read config file.

        Args:
            config_file: path to your config file.

        Returns:
            None

        Raises:
            TypeError: if config_file is not a string.

        """
        self._parser = ConfigParser.ConfigParser()
        self._parser.read(config_file)

    def __getattr__(self, name):
        """Read and return a section object.

        Args:
            name: section name to fetch.

        Returns:
            a section object with the options.

        Raises:
            ConfigParser.NoSectionError: if the
                section can't be found.

        """
        if self._parser.has_section(name):
            items = self._parser.items(name)
            return Section(name, items)
        else:
            raise ConfigParser.NoSectionError(name)
        # TODO: Could we use __type here to a avoid casting later?


class Section(object):
    """A data object with the options in a section.

    Section works much like Config. In a section
    you have zero or more options which is reached
    as attributes in your object, e.g:
    config.my_section.my_option where my_section
    is the name of your section and my_option
    the option you want to read.

    Attributes:
        You access your config file sections as
        attributes.

    """

    def __init__(self, section_name, items):
        """Save the section name and make a dict
        of the options.

        Args:
            section_name: the name of your section
            items: [(name: string, value: string)]

        Returns:
            None

        """
        self._section_name = section_name
        self._items = dict(items)

    def __getattr__(self, name):
        """Read and return a value as string.

        Args:
            name: option name to fetch.

        Returns:
            An option.

        Raises:
            ConfigParser.NoOptionError: if the
                option can't be found.

        """
        if name in self._items:
            return self._items[name]
        else:
            raise ConfigParser.NoOptionError(name, self._section_name)
