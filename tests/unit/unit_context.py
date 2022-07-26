import os
import sys
package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
    '../../src'))
if package_path not in sys.path:
    sys.path.insert(0, package_path)

import pinyin_tools

RESOURCES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),"res/")
OUTPUT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),"out/")