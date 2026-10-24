class LibraryError(Exception):
    """Base class for all library related errors."""


class DuplicateIDError(LibraryError):
    pass


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass


class BookNotBorrowedError(LibraryError):
    pass
