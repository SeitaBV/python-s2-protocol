# S2 Protocol Python Integration



## How to install it?

If you have Github account set up with ssh authentication, you can just pip install this package it from our private repo like this:


```
    pip install git+ssh://git@github.com/SeitaBV/python-s2-protocol.git
```

## How to regenerate the data models from JSONSchema?

We make use of datamodel-codegen tool which generates pydantic clases from the Schema descriptions in s2-ws-json/s2-asyncapi/s2-cem.yaml. To trigger a new generation, run the following command:

```
make generate-modes
```

Keep in mind that the timestamp of the generation time will be on top of the file, so you'll se always changes. 

## How to test it?

```
make test
```

## Production
For production envs, we can add deploy keys (only pull) from [here](https://github.com/SeitaBV/python-s2-protocol/settings/keys).