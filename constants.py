from enum import Enum

class SecretsManager(Enum):
    PASSWORD_REGEX = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    SECRET_KEY = "37e249cff0162245eeda58821c6c9649"
