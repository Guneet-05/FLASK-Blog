from enum import Enum

class SecretsManager(Enum):
    PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    SECRET_KEY = "37e249cff0162245eeda58821c6c9649"
