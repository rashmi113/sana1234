# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os
import torch
import sys

print("Python Version:", sys.version)
print("PyTorch Version:", torch.__version__)
print("Model File Path:", os.path.abspath('model/vitDefAugResnet50.pkl'))
print("Model File Exists:", os.path.exists('model/vitDefAugResnet50.pkl'))
print("Model File Size:", os.path.getsize('model/vitDefAugResnet50.pkl'), "bytes")