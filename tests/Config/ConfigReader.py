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
            with open(cls.configPath, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            props[key.strip()] = value.strip()
            cls._cachedProps = props
        except OSError as e:
            print("Error reading config.properties: {}".format(e))

            cls._cachedProps = {}
        return cls._cachedProps
