<p align="center">
  <img src="static/logo_v2_white.png" width="30%" alt="Archpoint logo">
</p>

<h1 align="center">Archpoint</h1>

<p align="center">
  Desktop-приложение для получения плотного облака точек архитектурных объектов по набору изображений с поддержкой автоматической и ручной калибровки камер в моно и стерео режимах.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/🖥️%20Windows-blue?style=for-the-badge" alt="Windows">
  <img src="https://img.shields.io/badge/🐧%20Linux-blue?style=for-the-badge" alt="Linux">
  <img src="https://img.shields.io/badge/🍎%20macOS-blue?style=for-the-badge" alt="macOS">
</p>

<p align="center">
  <a href="https://github.com/cloudsucker/archpoint/commits/main/">
    <img src="https://img.shields.io/badge/status-active-darkgreen?style=for-the-badge" alt="Status">
  </a>
  <a href="https://github.com/cloudsucker/archpoint/issues">
    <img src="https://img.shields.io/github/issues/cloudsucker/archpoint?label=Issues&logo=github&style=for-the-badge" alt="Issues">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-white?style=for-the-badge" alt="License">
  </a>
  </br>
    <a href="https://github.com/users/cloudsucker/projects/3">
    <img src="https://img.shields.io/badge/Project_Board-blueviolet?logo=github&style=for-the-badge" alt="Project Board">
  </a>
</p>

<p align="center">
  <img src="static/preview/result.gif" width="80%">
</p>

> [!WARNING]
> Данный репозиторий на данный момент находится в активной разработке. Некоторые детали могут быть описаны или реализованы неполностью или неккоректно. Буду рад вашей помощи в их обнаружении!

## 🚀 Установка

### 📦 Обычная установка

> [!NOTE]
> Скоро всё напишем! 😊

### 🛠 Установка в режиме разработки

#### **1. Создайте виртуальное окружение:**

```bash
python -m venv .venv
```

#### **2. Активируйте виртуальное окружение:**

```bash
.venv/Scripts/activate
```

#### 3. **Клонируйте репозиторий:**

```bash
git clone https://github.com/cloudsucker/archpoint.git
```

#### 4. **Установите зависимости:**

**Перейдите в директорию проекта:**

Для перехода в созданную при клонировании репозитория директорию используйте:

```bash
cd archpoint/
```

**Запустите установку зависимостей:**

```bash
pip install -r requirements.txt
```

> [!IMPORTANT]  
> Установка требует подключения к интернету для загрузки библиотеки [HLOC](https://github.com/cvg/Hierarchical-Localization) из GitHub-репозитория для последующей её установки в качестве зависимости. Этот процесс может занять некоторое время.

### 🚀 Запуск

Запустите файл `main.py` из корня проекта.

## 🔗 **Зависимости**

-   numpy<2.0.0
-   opencv-python==4.11.0.86
-   PySide6==6.8.2.1
-   git+https://github.com/cvg/Hierarchical-Localization.git#egg=hloc

> [!WARNING]  
> Проект требует версии `numpy<2.0.0` для корректной работы.

> [!NOTE]
> В проекте используется библиотека **[hloc](https://github.com/cvg/Hierarchical-Localization)**, распространяемая под лицензией **Apache License 2.0**. Поскольку **hloc** включается как внешняя зависимость через `requirements`, её код не распространяется вместе с проектом. Тем не менее, обращаем внимание, что использование **hloc** подпадает под условия **Apache 2.0**. Подробнее о лицензии: https://www.apache.org/licenses/LICENSE-2.0

## ⚙️ **Калибровка**

Демонстрация ручного метода калибровки с расстановкой точек:  
![calibration_preview](static/preview/room.gif)

## 📬 **Обратная связь**

**Репозиторий активно развивается, буду рад обратной связи.**

**По всем вопросам:** ferjenkill@gmail.com
