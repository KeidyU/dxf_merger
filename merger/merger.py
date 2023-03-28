import sys
import ezdxf
from ezdxf.addons import Importer
# import json
# from os import listdir
# from os.path import isfile, join

"""
The idea of this script is to merge n dxf files (from pathin) into a target dxf file (into pathout)
"""


def merge(source, target):
    """
    input: source file (with dxf data), target data (empty shell where you add dxf data from source)
    output: accumulative dxf data on target file
    """
    try:
        # https://ezdxf.readthedocs.io/en/stable/drawing/management.html?highlight=readfile#ezdxf.readfile
        source = ezdxf.readfile(source)

    except ezdxf.DXFError as e:
        print("\n" + "*" * 40)
        print("FOUND DXF ERROR: {}".format(str(e)))
        print("*" * 40 + "\n")
        return False

    try:
        importer = Importer(source, target)
        # import all entities from source modelspace into target modelspace
        importer.import_modelspace()
        # import all required resources and dependencies
        importer.finalize()

    except Exception as e:
        print("Error -> ", e.__class__)


"""
Main Function
"""
if __name__ == "__main__":
    # opening JSON file
    #jsondata = json.load(open("data.json"))
    files = []

    dxf_1 = sys.argv[1]
    dxf_2 = sys.argv[2]
    output = sys.argv[3]
    # dxf_1 = "C:/Users/Keidy/Desktop/merge-dxf/dxf_merger/in/instrumentos.dxf"
    # dxf_2 = "C:/Users/Keidy/Desktop/merge-dxf/dxf_merger/in/topo.dxf"
    # output = "C:/Users/Keidy/Desktop/merge-dxf/dxf_merger/out/merge_5.dxf"

    files.append(dxf_1)
    files.append(dxf_2)

    # empty target dxf
    target = ezdxf.new()

    # merger with filelist
    for file in files:
        print("filein ->", file)
        merge(file, target)

    # save merged dfx target
    try:
        print("target ->", output)
        target.saveas(output)
    except Exception as e:
        print("Error -> ", e.__class__)
