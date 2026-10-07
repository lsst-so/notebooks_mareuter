import logging
import unittest

import lsst.sitcom.mareuter.helpers as hp

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.level = logging.DEBUG


class TestHelpers(unittest.TestCase):
    def test_get_dir_from_fs_file(self) -> None:
        fs_file = "FiberSpectrograph:Blue_fiberSpecBlue_2026-07-14T15:05:40.032.fits"
        fdir = hp.get_dir_from_fs_file(fs_file)
        self.assertEqual(str(fdir), "FiberSpectrograph:Blue/fiberSpecBlue/2026/07/14")
