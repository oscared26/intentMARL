"""
Created on Aug 19, 2017

@author: Siyuan Qi

Description of the file.

"""

import errno
import logging
import os


class Paths(object):
    def __init__(self):
        """
        Configuration of data paths
        member variables:
            data_root: The root folder of all the recorded data of events
            metadata_root: The root folder where the processed information (Skeleton and object features) is stored.
        """
        self.project_root = '/home/siyuan/projects/papers/icra2018/'
        self.tmp_root = '/home/siyuan/projects/papers/icra2018/tmp/'

        if not os.path.exists(self.tmp_root):
            os.makedirs(self.tmp_root)


def set_logger(name='../../tmp/learner.log'):
    if not os.path.exists(os.path.dirname(name)):
        try:
            os.makedirs(os.path.dirname(name))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(name, mode='w')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                                                "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def main():
    pass


if __name__ == '__main__':
    main()
