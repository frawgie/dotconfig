DotConfig
=========

A simpler way to read configuration files.

dotconfig provides a very simple way to read options from a config file.
It is currently read-only.

How to use
----------

Example:

data.config
~~~~~~~~~~~

::

    [network]
    port: 8080

example.py
~~~~~~~~~~

::

    import dotconfig
    config = dotconfig.Config("data.config")
    config.network.port # returns the port number as string

Contribute
----------

Feel free to fork and add anything you find is missing. :)
