import getopt
import os
import sys

from lib.extract.data_copier import copy_data
from lib.extract.data_extractor import extract_data
from lib.load.data_loader import load_data
from lib.tracking_decorator import TrackingDecorator

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)


@TrackingDecorator.track_time
def main(argv):
    # Set default values
    clean = False
    quiet = False

    # Read command line arguments
    try:
        opts, args = getopt.getopt(argv, "hcq", ["help", "clean", "quiet"])
    except getopt.GetoptError:
        print("main.py --help --clean --quiet")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("main.py")
            print("--help                           show this help")
            print("--clean                          clean intermediate results before start")
            print("--quiet                          do not log outputs")
            sys.exit()
        elif opt in ("-c", "--clean"):
            clean = True
        elif opt in ("-q", "--quiet"):
            quiet = True

    manifest_path = os.path.join(script_path, "data-product.yml")
    raw_path = os.path.join(script_path, "raw")
    workspace_path = os.path.join(script_path, "workspace")
    data_path = os.path.join(script_path, "data")

    #
    # Extract
    #

    extract_data(manifest_path=manifest_path, results_path=raw_path, clean=clean, quiet=quiet)
    copy_data(source_path=raw_path, results_path=workspace_path, clean=clean, quiet=quiet)

    #
    # Transform
    #

    # TODO Add transformation steps in ./lib/transform and call them here

    #
    # Load
    #

    load_data(source_path=workspace_path, results_path=data_path, clean=clean, quiet=quiet)


if __name__ == "__main__":
    main(sys.argv[1:])
