from abc import ABC, abstractmethod


class CalibrationMethodAbstract(ABC):
    @abstractmethod
    def calibrate(self, image_paths: list) -> dict:
        pass

    @abstractmethod
    def calibrate_stereo(self, left_image_paths: list, right_image_paths: list) -> dict:
        pass
