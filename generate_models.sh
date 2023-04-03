#!/bin/bash

# create venv
#python3 -m venv venv-datagen
source venv-datagen/bin/activate

rm -rf src/python_s2_protocol/raw*

# install code generator
# pip install datamodel-code-generator

basename="s2-ws-json/s2-json-schema"


# run code generator


mkdir -p src/python_s2_protocol/raw/common

# common types
for schema_type in 'schemas' 'messages'
do
    mkdir -p "src/python_s2_protocol/raw/common/$schema_type"

    for entry in "s2-ws-json/s2-json-schema/$schema_type/"*
    do

        if [[ $entry == *+(FRBC|PPBC|PEBC|DDBC|OMBC)* ]]; then
            continue
        fi

        echo "$entry"
        filename=$(basename ${entry})
        filename=${filename/.schema.json/.py}
        
        datamodel-codegen --use-title-as-name  --input $entry --output src/python_s2_protocol/raw/common/$schema_type/$filename
    done
done

# operation modes messages and schemas

for mode in "FRBC" 
do
    mkdir -p "src/python_s2_protocol/raw/$mode"

    for schema_type in 'schemas' 'messages'
    do
        mkdir -p "src/python_s2_protocol/raw/$mode/$schema_type"

        for entry in "s2-ws-json/s2-json-schema/$schema_type/$mode."*
        do
            echo "$entry"
            filename=$(basename ${entry})
            filename=${filename/schema.json/py}
            filename=${filename/$mode./}
            
            datamodel-codegen --use-title-as-name  --input $entry --output src/python_s2_protocol/raw/$mode/$schema_type/$filename
        done
    done
done



# clean
rm -rf venv-datagen/

