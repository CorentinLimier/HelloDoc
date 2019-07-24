#!/bin/bash

sphinx-apidoc -f -o source/ ../foo_bar_lib/
sphinx-build . ../documentation_html
