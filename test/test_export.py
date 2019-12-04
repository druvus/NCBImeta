"""
NCBImeta Test - Export

@author: Katherine Eaton
"""

#-----------------------------------------------------------------------#
#                         Modules and Packages                          #
#-----------------------------------------------------------------------#

import pytest                             # Testing suite
from ncbimeta import *                    # Main Program
import os                                 # Filepath operations
import test.test_ncbimeta                 # Run the program to create test db
import subprocess                         # Execute CLI/Shell

#-----------------------------------------------------------------------#
#                           Test Function                               #
#-----------------------------------------------------------------------#

def test_export_run():
    '''Test the NCBImetaExport application for run completion'''
    # Use the test database
    test_db = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test.sqlite")
    test_output_dir = os.path.dirname(os.path.abspath(__file__))
    # If the test_db doesn't alread exist, run the test cmd from test_ncbimeta
    if not os.path.exists(test_db): test_ncbimeta.test_ncbimeta_run()
    test_cmd = ("ncbimeta/NCBImetaExport.py --database " + test_db +
                " --outputdir " + test_output_dir)

    # test NCBImetaExport through a subprocess
    returned_value = subprocess.call(test_cmd, shell=True)
    # If it returns a non-zero value, it failed
    assert returned_value == 0

def test_export_assemblyvalues(assembly_table_data):
    '''
    Test the integrity of the Assembly table values based on expected values.

    Parameters:
    assembly_table_data (fixture): Dict fixture of Assembly table data from conftest.py
    '''
    # Setup the assembly table file
    test_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_Assembly.txt")
    test_file = open(test_filename,'r')
    # Retrieve the headers and fields
    test_column_list = test_file.readline().strip('\n').split("\t")
    test_metadata_list = test_file.readline().strip('\n').split("\t")
    # Populate the dict with data
    test_dict = {}
    for i in range(0,len(test_column_list)):
        key = test_column_list[i]
        value = test_metadata_list[i]
        test_dict[key] = value
    # Test whether the values are as expected
    assert test_dict == assembly_table_data
    #Cleanup
    test_file.close()

def test_export_bioprojectvalues(bioproject_table_data):
    '''
    Test the integrity of the BioProject table values based on expected values.

    Parameters:
    bioproject_table_data (fixture): Dict fixture of BioProject table data from conftest.py
    '''
    # Setup the assembly table file
    test_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_BioProject.txt")
    test_file = open(test_filename,'r')
    # Retrieve the headers and fields
    test_column_list = test_file.readline().strip('\n').split("\t")
    test_metadata_list = test_file.readline().strip('\n').split("\t")
    # Populate the dict with data
    test_dict = {}
    for i in range(0,len(test_column_list)):
        key = test_column_list[i]
        value = test_metadata_list[i]
        test_dict[key] = value
    # Test whether the values are as expected
    assert test_dict == bioproject_table_data
    #Cleanup
    test_file.close()