Week 1
======


Week 1 will be a general introduction to the course and a refresher
on basic python programming.


Preparation
-----------

I would encourage everyone to bring a laptop to the classes to follow along. 
If you do not already have python installed the simplest way to set up your
computer is probably with the 
`Anaconda installer <https://www.continuum.io/downloads>`_. Use the installer 
for python 3.6 appropriate for your operating system. 

We will be using python 3.6 throughout the course. If you already have a 
version of python 3 installed all the examples we go through will probably 
work without any errors. If you currently have a version of python 2 installed 
you may still be fine but errors are more likely and I would encourage you to 
either upgrade or create a python 3.6 environment specifically for this 
course. If you have previously used the anaconda installer a new environment 
can be created with::

    conda create -n py36 python=3.6 anaconda

The necessary command to activate this new environment will depend on your
`operating system <http://conda.pydata.org/docs/test-drive.html#managing-envs>`_. 


Useful Packages
---------------

Depending on your background the following packages may be new to you. As we will be making extensive use of each developing familiarity with each will be useful to you.

Jupyter
^^^^^^^

Jupyter notebook is a web application that enables sharing of live code together with its output. This is very useful and the majority of course material is in the form of jupyter notebooks.

The resources below are useful if jupyter is new to you.

* https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/
* https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook

Numpy
^^^^^

Numpy is a foundational package for data analysis in python. The key component it provides is a multi-dimensional array object. The vast majority of packages for scientific tasks in python expect numpy arrays. Numpy also provides many useful basic functions for operating on numerical data.

The resources below will help you develop a familiarity with array operations with numpy.

* https://www.datacamp.com/community/tutorials/python-numpy-tutorial
* https://cs231n.github.io/python-numpy-tutorial/ (more machine learning focused)
* https://docs.scipy.org/doc/numpy-dev/user/quickstart.html (official documentation)

Matplotlib
^^^^^^^^^^

Matplotlib is a plotting package. We will use this extensively for visualizing datasets and results.

Most of our use of matplotlib is basic but having made a plot or two will be useful

* http://matplotlib.org/users/pyplot_tutorial.html

Pandas
^^^^^^

Pandas provides data structures and data analysis tools that are intended to be easier to use. Pandas excels with tabular data.

We will use pandas mainly for loading datasets and preprocessing.

* http://pandas.pydata.org/pandas-docs/stable/10min.html
* http://pandas.pydata.org/pandas-docs/stable/tutorials.html


Files
-----

Please download the notebook below for use during the class.

 `Week 1 notebooks <../week1-notebooks.zip>`_
 

Solutions
---------

A set of example solutions and a screencast on their development are now available: :doc:`solutions`
 

