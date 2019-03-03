# vue-lexer


[![Build Status](https://travis-ci.org/testdrivenio/vue-lexer.svg?branch=master)](https://travis-ci.org/testdrivenio/vue-lexer)

[![PyPI version](https://badge.fury.io/py/vue-lexer.svg)](https://badge.fury.io/py/vue-lexer)

A Vue lexer for [Pygments](http://pygments.org/) (based on [jsx-lexer](https://github.com/fcurella/jsx-lexer))

## Installation

```sh
$ pip install vue-lexer
```

## Usage with Sphinx

To use within Sphinx, simply specify `vue` for your `code-block`:

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

## Usage with mkdocs

First, you need to create the CSS for the highlighting:

```sh
$ pygmentize -S default -f html -a .codehilite > code/pygments.css
```

Then, add the following to your `mkdocs.yml`:

```yaml
markdown_extensions:
  - codehilite
extra_css: [pygments.css]
```

Now, you can use `vue` in your code blocks:

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

## Examples

Example 1:

<img src="https://raw.githubusercontent.com/testdrivenio/vue-lexer/master/examples/example1.png" width="25%">

Example 2:

<img src="https://raw.githubusercontent.com/testdrivenio/vue-lexer/master/examples/example2.png" width="50%">

Example 3:

<img src="https://raw.githubusercontent.com/testdrivenio/vue-lexer/master/examples/example3.png" width="35%">
