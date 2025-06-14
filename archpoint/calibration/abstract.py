from abc import ABC, abstractmethod


class CalibrationMethodAbstract(ABC):
    @abstractmethod
    def calibrate(self, image_paths: list[str]) -> dict:
        pass

    @abstractmethod
    def calibrate_stereo(
        self, left_image_paths: list[str], right_image_paths: list[str]
    ) -> dict:
        pass
