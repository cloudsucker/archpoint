import os
import numpy as np
from pathlib import Path

from hloc import (
    extract_features,
    match_features,
    reconstruction,
    visualization,
    pairs_from_exhaustive,
)
from hloc.visualization import read_image
from hloc.utils import viz_3d


class HLOC_Handler:
    def __init__(self):
        self.images = Path()
        self.outputs_path = Path()

        self.__sfm_pairs_filepath = ""
        self.__loc_pairs_filepath = ""
        self.__sfm_directory = ""
        self.__features = ""
        self.__matches = ""

        self.is_hloc_handler_initialized = False

    def process_images(self, images_path: str, outputs_path: str):
        if not os.path.exists(images_path):
            raise FileNotFoundError("Директория с изображениями не найдена.")

        if not os.path.exists(outputs_path):
            raise FileNotFoundError("Директория для сохранения результатов не найдена.")

        self.images = Path(images_path)
        self.outputs_path = Path(outputs_path)
        self.__init_handler(self.outputs_path)
        self.__get_images_references()
        self.__extract_image_features()
        self.__reconstruct()
        self.__visualize()

    def __init_handler(self, outputs_path: str):
        self.__sfm_pairs_filepath = outputs_path / "pairs-sfm.txt"
        self.__loc_pairs_filepath = outputs_path / "pairs-loc.txt"
        self.__sfm_directory = outputs_path / "sfm"
        self.__features = outputs_path / "features.h5"
        self.__matches = outputs_path / "matches.h5"
        self.__feature_conf = extract_features.confs["disk"]
        self.__matcher_conf = match_features.confs["disk+lightglue"]
        self.is_hloc_handler_initialized = True

    def __get_images_references(self):
        self.__references = [
            p.relative_to(self.images).as_posix() for p in (self.images).iterdir()
        ]

    def __extract_image_features(self):
        extract_features.main(
            self.__feature_conf,
            self.images,
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

    def __reconstruct(self):
        self.model = reconstruction.main(
            self.__sfm_directory,
            self.images,
            self.__sfm_pairs_filepath,
            self.__features,
            self.__matches,
            image_list=self.__references,
        )

    def __visualize(self):
        fig = viz_3d.init_figure()
        viz_3d.plot_reconstruction(
            fig, self.model, color="rgba(255,0,0,0.5)", name="mapping", points_rgb=True
        )
        fig.show()


class HLOC_handlerIsNotInitialized(Exception):
    pass
