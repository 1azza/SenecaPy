SenecaPy
--------
A python library to interact with the senecalearning.com API

.. image:: example.gif

Installing
----------

**Python 3.8 or higher is required**

To install the library run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U SenecaPy

    # Windows
    py -3 -m pip install -U SenecaPy


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/1azza/SenecaPy
    $ cd SenecaPy
    $ python3 -m pip install -U .



Quick Example
-------------

.. code:: py

    import seneca
    from pprint import pprint


    #This script will attempt to output answers from a seneca course

    url = input('Please enter url for seneca course')
    data = seneca.course.getanswers(url)
    pprint(data)
    






  
