"""TMU base exception handling."""


class TmuException(Exception):
    """Base Tmu exception
    To correctly use this class, inherit from it and define
    a `template` property.
    That `template` will be formated using the keyword arguments
    provided to the constructor.
    """

    template = "An unknown exception occurred."

    def __init__(self, message=None, **kwargs):
        message = message or self.template

        try:
            message = message % kwargs
        except (TypeError, KeyError):
            # Something went wrong during message formatting.
            # Probably kwargs doesn't match a variable in the message.
            message = ("Message: %(template)s. Extra or "
                       "missing info: %(kwargs)s" %
                       {"template": message, "kwargs": kwargs})

        super(TmuException, self).__init__(message)


class Invalid(TmuException):

    """The received object is not valid."""

    template = "Unacceptable parameters."
