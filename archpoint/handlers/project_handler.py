import os
import json
import datetime


class ProjectHandler:
    def __init__(self):
        self.name = ""
        self.path = ""
        self.is_project_initialized = False

        self.__config_filename = "config.json"
        self.__config_path = ""

    def create_project(self, name: str, path: str) -> None:
        if not name:
            raise ValueError("Название проекта не может быть пустым.")

        if not os.path.isdir(path):
            raise FileNotFoundError("Указанный путь не существует.")

        os.makedirs(path, exist_ok=True)

        self.name = name
        self.path = path
        self.__config_path = self.__get_config_path(path)

        if os.path.exists(self.__config_path):
            raise ProjectAlreadyExists("Проект уже существует.")

        self.__create_config()
        self.is_project_initialized = True

    def open_project(self, path: str) -> None:
        if not os.path.exists(path):
            raise ProjectNotFound("Директория не найдена.")

        config_path = self.__get_config_path(path)
        config_data = self.__load_config(config_path)

        self.name = config_data["name"]
        self.path = config_data["path"]
        self.__config_path = config_path
        self.is_project_initialized = True

    def __get_config_path(self, project_path: str) -> str:
        return os.path.join(project_path, self.__config_filename)

    def __create_config(self) -> None:
        config = {
            "name": self.name,
            "path": self.path,
            "created_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        }

        with open(self.__config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

    def __load_config(self, config_path: str) -> dict:
        if not os.path.exists(config_path):
            raise ProjectConfigurationError("Файл конфигурации проекта не найден.")

        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)
        self.__validate_config(config_data)

        return config_data

    def __validate_config(self, config: dict) -> None:
        required_keys = {"name", "path", "created_at"}
        if not required_keys.issubset(config):
            raise ProjectConfigurationError(
                "Ошибка загрузки файла конфигурации проекта: Файл конфигурации повреждён или неполный."
            )


class ProjectNotFound(Exception):
    pass


class ProjectAlreadyExists(Exception):
    pass


class ProjectWasNotCreated(Exception):
    pass


class ProjectAlreadyCreated(Exception):
    pass


class ProjectConfigurationError(Exception):
    pass
