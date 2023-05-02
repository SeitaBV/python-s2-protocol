#!/bin/bash

# create venv
python3 -m venv venv-datagen
source venv-datagen/bin/activate

# delete content if the path exists
[ -d "raw/" ] && rm -rf raw/*

# create folder if it doesn't exist
if [ ! -d "raw/" ]
then
    mkdir raw/
fi


# install code generator
pip install datamodel-code-generator

basename="s2-ws-json/s2-json-schema"


# run code generator

mkdir -p raw/common

# common types
for schema_type in 'schemas' 'messages'
do
    mkdir -p "raw/common/$schema_type"

    for entry in "s2-ws-json/s2-json-schema/$schema_type/"*
    do

        if [[ $entry == *+(FRBC|PPBC|PEBC|DDBC|OMBC)* ]]; then
            continue
        fi

        echo "$entry"
        filename=$(basename ${entry})
        filename=${filename/.schema.json/.py}

        datamodel-codegen --use-title-as-name --input-file-type jsonschema --input $entry --output raw/common/$schema_type/$filename
    done
done

# operation modes messages and schemas
for mode in "FRBC" "PPBC" "PEBC" "DDBC" "OMBC"
do
    mkdir -p "raw/$mode"

    for schema_type in 'schemas' 'messages'
    do
        mkdir -p "raw/$mode/$schema_type"

        for entry in "s2-ws-json/s2-json-schema/$schema_type/$mode."*
        do
            echo "$entry"
            filename=$(basename ${entry})
            filename=${filename/schema.json/py}
            filename=${filename/$mode./}

            datamodel-codegen --use-title-as-name   --input-file-type jsonschema  --input $entry --output raw/$mode/$schema_type/$filename
        done
    done
done


# clean
rm -rf venv-datagen/
