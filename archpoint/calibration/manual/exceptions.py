class RoomImageDotsEditorCreatingError(Exception):
    pass


class DotWithTheSameIdAlreadyExists(Exception):
    pass


class DotWithCurrentIdNotFound(Exception):
    pass


class SomeImagesHaveNoDots(Exception):
    pass


class InvalidDotId(Exception):
    pass


class InvalidDotFormat(Exception):
    pass


class InvalidDotCoordinates(Exception):
    pass


class RoomImagesManagerSelfCheckError(Exception):
    pass


class RoomImageDotsEditorSelfCheckError(Exception):
    pass


class NoImagesInDirectoryError(Exception):
    pass


class InvalidHistoryOperationType(Exception):
    pass


class DotsRealCoordinatesLoadingFromFileError(Exception):
    pass


class DotsHistoryIsEmpty(Exception):
    pass
