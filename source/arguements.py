#!/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed. 30/10/2024 14:20:00 - JRH

Description: Script defining the arguements for the PEtab to SEDML conversion
"""

# -----------------------Package Import & Defined Arguements-------------------#
import argparse


def parse_args():
    """Retrieve and parse arguments necessary for PEtab to SEDML conversion
    Inputs:
        None

    Returns:
        A namespace populated with all the attributes.
    """

    parser = argparse.ArgumentParser(
        description="Provide arguments to build the SPARCED model"
    )

    parser.add_argument(
        "--yaml_path",
        "-y",
        required=False,
        type=str,
        help="path to the yaml file for conversion",
    )

    return parser.parse_args()
