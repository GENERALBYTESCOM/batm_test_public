import codecs
import logging
import os


class ConfigReader:
    configPath = os.path.join(os.path.dirname(__file__), "config.properties")
    _cachedProps = None

    @classmethod
    def loadProperties(cls):
        if cls._cachedProps is not None:
            return cls._cachedProps
        props = {}
        try:
            with codecs.open(cls.configPath, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            props[key.strip()] = value.strip()
            cls._cachedProps = props
        except OSError as e:
            logging.info("Error reading config.properties: %s", e)
            cls._cachedProps = {}
        return cls._cachedProps
