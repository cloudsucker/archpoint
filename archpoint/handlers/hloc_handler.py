import os
from pathlib import Path

from hloc import (
    extract_features,
    match_features,
    reconstruction,
    pairs_from_exhaustive,
)
from hloc.utils import viz_3d

# TODO: Remove unused function or use it instead
# from hloc import visualization
# from hloc.visualization import read_image


class HLOC_Handler:
    def __init__(self):
        self.images_path = Path()
        self.outputs_path = Path()

        self.pairs_dir = "pairs"
        self.features_dir = "features"

        self.__sfm_pairs_filepath = ""
        # self.__loc_pairs_filepath = ""
        self.__sfm_directory = ""
        self.__features = ""
        self.__matches = ""

        self.is_hloc_handler_initialized = False

    def process_images(self, images_path: str, outputs_path: str) -> None:
        if not os.path.exists(images_path):
            raise FileNotFoundError("Директория с изображениями не найдена.")

        if not os.path.isdir(outputs_path):
            raise FileNotFoundError(
                "Некорректная директория для сохранения результатов."
            )

        os.makedirs(outputs_path, exist_ok=True)

        self.images_path = Path(images_path)
        self.outputs_path = Path(outputs_path)
        self.__init_handler(self.outputs_path)
        self.__get_images_references()
        self.__extract_image_features()
        self.__reconstruct()
        self.__visualize()

    def __init_handler(self, outputs_path: str) -> None:
        self.__sfm_pairs_filepath = outputs_path / self.pairs_dir / "pairs-sfm.txt"
        # self.__loc_pairs_filepath = outputs_path / self.pairs_dir / "pairs-loc.txt"
        os.makedirs(outputs_path / self.pairs_dir, exist_ok=True)

        self.__sfm_directory = outputs_path / "sfm"
        os.makedirs(self.__sfm_directory, exist_ok=True)

        self.__features = outputs_path / self.features_dir / "features.h5"
        self.__matches = outputs_path / self.features_dir / "matches.h5"
        os.makedirs(outputs_path / self.features_dir, exist_ok=True)

        self.__feature_conf = extract_features.confs["disk"]
        self.__matcher_conf = match_features.confs["disk+lightglue"]

        self.is_hloc_handler_initialized = True

    def __get_images_references(self) -> None:
        self.__references = [
            p.relative_to(self.images_path).as_posix()
            for p in (self.images_path).iterdir()
        ]

    def __extract_image_features(self) -> None:
        extract_features.main(
            self.__feature_conf,
            self.images_path,
            image_list=self.__references,
            feature_path=self.__features,
        )
        pairs_from_exhaustive.main(
            self.__sfm_pairs_filepath, image_list=self.__references
        )
        match_features.main(
            self.__matcher_conf,
            self.__sfm_pairs_filepath,
            features=self.__features,
            matches=self.__matches,
        )

    def __reconstruct(self) -> None:
        self.model = reconstruction.main(
            self.__sfm_directory,
            self.images_path,
            self.__sfm_pairs_filepath,
            self.__features,
            self.__matches,
            image_list=self.__references,
        )

    # TODO: Remove this function or refactor it to visualize
    #       the results in app or web views.
    def __visualize(self) -> None:
        fig = viz_3d.init_figure()
        viz_3d.plot_reconstruction(
            fig, self.model, color="rgba(255,0,0,0.5)", name="mapping", points_rgb=True
        )
        fig.show()


class HLOC_handlerIsNotInitialized(Exception):
    pass
