vue-lexer
=========

.. image:: https://travis-ci.org/testdrivenio/vue-lexer.svg?branch=master
    :target: https://travis-ci.org/testdrivenio/vue-lexer

A Vue lexer for Pygments (based on `jsx-lexer <https://github.com/fcurella/jsx-lexer>`_)

Installation
------------
.. code-block:: sh

    $ pip install vue-lexer

Usage with Sphinx
-----------------

To use within Sphinx, simply specify ``vue`` for your ``code-block``::

    .. code-block:: vue

        <template>
          <p>{{ greeting }} World!</p>
        </template>

        <script>
        module.exports = {
          data: function () {
            return {
              greeting: 'Hello'
            }
          }
        }
        </script>

        <style scoped>
        p {
          font-size: 2em;
          text-align: center;
        }
        </style>

Usage with mkdocs
-----------------

First, you need to create the ``CSS`` for the highlighting:

.. code-block:: bash

  $ pygmentize -S default -f html -a .codehilite > code/pygments.css

Then, add the following to your ``mkdocs.yml``:

.. code-block:: yaml

  markdown_extensions:
    - codehilite
  extra_css: [pygments.css]

Now, you can use ``vue`` in your code blocks::

    ```vue
    <template>
      <p>{{ greeting }} World!</p>
    </template>

    <script>
    module.exports = {
      data: function () {
        return {
          greeting: 'Hello'
        }
      }
    }
    </script>

    <style scoped>
    p {
      font-size: 2em;
      text-align: center;
    }
    </style>
    ```
