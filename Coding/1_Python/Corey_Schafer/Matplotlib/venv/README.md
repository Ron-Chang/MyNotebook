# Virtual Enviroment

```bash
pip list
```
Print out all global packages

```bash
python3 -m venv project/venv
```
`python3 -m venv`
'-m' stand for module, call the module `venv` through `python3`
`porject/venv`
`porject` project name
`/venv` package folder, a format name is not necessary.


```bash
source project/venv/bin/activate
```
To activate virtual enviroment.

```bash
pip install package_name
```
This package is only avalible in local.

Export enviroment
```bash
# pip freeze
pip freeze > requirements.txt
```
Create a `freeze list` and `export` it to a `txt` file
`requirements.txt` It's okay to replace with a different name.

```bash
python3 -m venv venv --system-site-packages
```
source the global packages, the benefit is you don't have to install the genernal packages again and it allow you install the new packages individually as well.

```bash
pip list --local
```
To print out the `local` packages.

```bash
pip freeze --local
```
To freeze the `local` packages.


```bash
deactivate
```
Extrac!




