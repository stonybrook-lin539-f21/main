# Build instructions

## How to build

Currently, the Python program "Doit" is used to convert the source files into PDF and HTML form. To build everything, simply run "doit" from the project root. All output will be in the directory "build".

To selectively build one or more formats, run "doit TASK" where TASK is one of {pdf_chaps, latex_chaps, html_chaps}.

## Requirements

- Python >= 3.9
- Doit >= 0.31
- Pandoc >= 2.9
- bash, sed

Everything is tested only on Ubuntu 21.04, and the above requirements are installed from the Ubuntu repositories. The current build script may work with older software, but has not been tested yet.

## Makefile

A makefile for GNU Make is also available, but is not up to date. For now, use Doit.
