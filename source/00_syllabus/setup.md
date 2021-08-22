# Installation and Setup for Jupyter Notebook

The lecture notes are made available as [Jupyter notebooks](http://jupyter.org/) in the [main github repository](https://github.com/StonyBrook-Lin539-F17/main).
A Jupyter notebook is a mixture of text and Python code, which allows for a more interactive learning environment.
There are multiple ways you can view the notebooks:

1.  Use Stony Brook's [Virtual SINC site](https://it.stonybrook.edu/services/virtual-sinc-site), which already has Jupyter installed. 
1.  Use our virtual machine image for VirtualBox, available at Stony Brook's [Softweb](https://softweb.cc.stonybrook.edu/).
1.  Install [Anaconda](https://www.continuum.io/downloads), a Python distro that also installs Jupyter.
1.  If you already have a working Python setup, install Jupyter separately.
1.  If you can live without the interactive Python demonstrations, you can just read the notebooks directly on github.

For all options except the last one, you should use the supplied `start_jupyter.py` script to start the Jupyter server.
This will load additional macros and styles that are needed to display the notebooks correctly.

## Using Jupyter Notebooks with Virtual SINC

1. Go to the [Virtual SINC](https://it.stonybrook.edu/services/virtual-sinc-site) site in your browser, and log in with your Net ID.
   In order to start the virtual desktop, you need the Citrix receiver installed.
   Stony Brook has guides for how to do this on
   - [Windows and Mac](https://it.stonybrook.edu/help/kb/connecting-to-the-virtual-sinc-site-on-windows-or-mac),
   - [Android](https://it.stonybrook.edu/help/kb/connecting-to-the-virtual-sinc-site-on-an-android-tablet),
   - [iOS](https://it.stonybrook.edu/help/kb/connecting-to-the-virtual-sinc-site-on-an-apple-ipad).

1. Once the virtual desktop has loaded, open the web browser and download the entire course repository as a zip folder.
   To do this, go to the [main repository](http://lin539.thomasgraf.net), click on the green button *Clone or download* in the top right corner, and pick *Download ZIP*.

1. Extract the zip file into the *My SBfiles* folder.
   This is your university wide network storage, and is the only location on Virtual SINC where you can safely store file without them being deleted.
   For more information about My SBfiles, [follow this link](https://it.stonybrook.edu/services/mysbfiles).

1. Click on the folder you extracted the archive to.
   If there is just another folder inside of it, click on that one too.

1. Click on the file `start_jupyter.py`.
   The notebook server will launch and open the Home tab in the browser.
   In the Home tab, you should be able to see all files and folders of the repository.

1. All notebooks are in the folder called `notebooks`.
   Use the Home tab in your browser to navigate to whatever notebook you want to read, and left click to open it.

## Using Jupyter with Anaconda

1. If you are using Windows, first verify whether your version is 32-bit or 64-bit.
   Here is [a tutorial](https://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/) for how to do this in various Windows versions.

1. Go to the [Anaconda website](https://www.anaconda.com/download/) and download Anaconda for Python 3.
   Make sure you pick the correct downloader for your OS, and if you're on the Windows, also the correct 32-bit or 64-bit installer.

1. Install Anaconda.
   You can keep all the settings at their default values.

1. Once Anaconda is installed, open the web browser and download the entire course repository as a zip folder.
   To do this, go to the [main repository](http://lin539.thomasgraf.net), click on the green button *Clone or download* in the top right corner, and pick *Download ZIP*.

1. Extract the zip file into a folder of your choice.
   I suggest you put the folder directly in your default user directory (the same folder that also contains subfolder for downloads, music, pictures, and so on).

1. Once Anaconda is installed, open the Anaconda prompt.
   Navigate to the folder that you extracted the repository to.
   For example, if you put all the files in a folder `lin539` in your user directory, type `cd lin539` to change to the folder.
   If you instead put a folder `lin539` in a subfolder `school`, you would type `cd school`, hit Enter, then type `cd lin539`.

1. Type `dir` to see the files in the folder you are currently at in the prompt.
   You should see a file called `start_jupyter.py`.

1. Type `python start_jupyter.py` to start the Jupyter server.
   The notebook server will launch and open the Home tab in the browser.
   In the Home tab, you should be able to see all files and folders of the repository.

1. All notebooks are in the folder called `notebooks`.
   Use the Home tab in your browser to navigate to whatever notebook you want to read, and left click to open it.
