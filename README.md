# test-py-cookie

## Introduction

for exploring github actions

Very brief overview of the tool. If possible use some illustrations.

## Installation

Brief description of installation, in a step-by-step fashion.

example:

1. git clone ../project_name
0. cd /path/to/project_name
0. pip install -r requirements.txt .

### A note on installation of Libraries vs Applications

Any Python project is either an application or a library. It could be both,
then it should be considered as a library. Shortly put, a library is designed
to be imported by other projects; an application is used as it is. Further
reading: https://iscinumpy.dev/post/app-vs-library/

Since an application is a standalone package, to ensure its proper operation
we should completely specify its dependencies. In our projects, `requirements.txt` provides the
full dependencies and users can install with `pip install -r requirements.txt`
or `pip-sync` or `pipx`.

However, a library is different since it has to be used with other libraries,
we want to specify the minimal dependencies to avoid conflicts with other libraries.
In our projects, `pyproject.toml` specifies the minimal/direct dependencies and
users can install with `pip install .`

Both `pyproject.toml` and (an auto-generated) `requirements.txt` is available in our
projects. The developers should guide users to proper installation method. Having
both minimal (pyproject.toml) and constrained (requirements.txt) installations available
is helpful: users can use the minimal installation to get it to work with other packages.
Or they can fallback to fully tested software with the constrained installation.

## Get Started

Show some main functionality. Keep it short.

Example, for a library:

```py
from project_name import BaseClass
from project_name import base_function

BaseClass().base_method()
base_function()
```

If it is not a library, but a CLI app, again demonstrate the important commands.
An imperfect but sufficient way is to copy-paste the app's output of `--help`.


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) in the project root.

## Contact

* Developer: Berk Tosun, test@test.com
