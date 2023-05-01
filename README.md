# S2 Protocol Python Integration



## How to install it?

To install the latest version of this project, you can just pip install it like this:


```
pip install git+ssh://git@github.com/SeitaBV/python-s2-protocol.git
```

## How to regenerate the data models from JSONSchema?

We make use of `datamodel-codegen` tool which generates pydantic classes from the Schema descriptions in s2-ws-json/s2-asyncapi/s2-cem.yaml. To trigger a new generation, run the following command:

```
make generate-models
```

This command creates a python `venv` with the required dependencies to run `datamodel-codegen`.

Keep in mind that the timestamp of the generation time will be on top of the file, so you'll always see changes. The results are located in the `raw` folder with the following file structure:

* common
  * messages
  * schemas
* DDBC
  * messages
  * schemas
* FRBC
  * messages
  * schemas
* PEBC
  * messages
  * schemas
* PPBC
  * messages
  * schemas

After the files are generated, we refactor the classes manually to concentrate all the common models (ID, NumberRange, ...) into the file `common.py`, and the schemas of each operation mode into different submodules.


## How to test it?

```
make test
```
