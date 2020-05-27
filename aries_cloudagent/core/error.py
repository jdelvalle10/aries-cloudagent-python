"""Common exception classes."""

import re


class BaseError(Exception):
    """Generic exception class which other exceptions should inherit from."""

    def __init__(self, *args, error_code: str = None, **kwargs):
        """Initialize a BaseError instance."""
        super().__init__(*args, **kwargs)
        self.error_code = error_code if error_code else None

    @property
    def message(self) -> str:
        """Accessor for the error message."""
        return self.args[0].strip() if self.args else ""

    @property
    def roll_up(self) -> str:
        """
        Accessor for nested error messages rolled into one line.

        For display: aiohttp.web errors truncate after newline.
        """
        line = "{}{}".format(
            "({}) ".format(self.error_code) if self.error_code else "",
            re.sub(r"\n\s*", ". ", self.args[0]) if self.args else "",
        )
        return line.strip()


class StartupError(BaseError):
    """Error raised when there is a problem starting the conductor."""


class ProtocolDefinitionValidationError(BaseError):
    """Error raised when there is a problem validating a protocol definition."""


class ProtocolMinorVersionNotSupported(BaseError):
    """
    Minimum minor version protocol error.

    Error raised when protocol support exists
    but minimum minor version is higher than in @type parameter.
    """
