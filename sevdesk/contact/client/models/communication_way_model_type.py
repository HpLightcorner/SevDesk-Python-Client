from enum import Enum


class CommunicationWayModelType(str, Enum):
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    WEB = "WEB"
    MOBILE = "MOBILE"

    # The SevDesk API might use "0" for null-enums
    NULL = "0"

    def __str__(self) -> str:
        return str(self.value)
