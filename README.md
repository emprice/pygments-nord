_pygments-nord_: Pygments style plugin with Nord colors
=======================================================

This is a simple implementation of two [Pygments](https://pygments.org) plugins
appropriate for light and dark colorschemes
(see [`pynordlight`](pynordlight/__init__.py) and
[`pynorddark`](pynorddark/__init__.py), respectively) using the
[Nord colorscheme](https://www.nordtheme.com). If you have suggestions
for improving the schemes, feel free to open an issue or pull request.

To build the plugin, you can run

```sh
python -m build -o build
```

in the project root directory and install with

```sh
pip install [--user] [--force-reinstall] build/pygments_nord-1.0-py3-none-any.whl
```

where `--user` is useful for a local install (no root privileges) and
`--force-reinstall` can be used to reinstall for testing during development,
since pip will not normally reinstall a package with the same version as
one already installed.

<!-- vim: set ft=markdown: -->
