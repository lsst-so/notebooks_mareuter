import pathlib

__all__ = ["get_data_dir", "get_mplstyle_file", "get_dir_from_fs_file"]


def get_data_dir() -> pathlib.Path:
    """Return the data directory of this package."""
    return pathlib.Path(__file__).resolve().parent / "data"


def get_mplstyle_file() -> pathlib.Path:
    """Return the matplotlib style file."""
    return get_data_dir() / "plot_style.mplstyle"


def get_dir_from_fs_file(fs_file: str) -> str:
    """Get directory from a FiberSpectrograph FITS file."""
    head = fs_file.split("T")[0]
    temp1 = head.replace("_", "/")
    temp2 = temp1.replace("-", "/")
    return temp2
    