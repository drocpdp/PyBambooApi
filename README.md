PyBambooApi
======

Python client for the Atlassian Bamboo API

Setup
=====
Add environment variable via bash profile
~/.bash_profile
etc.
PY_BAMBOO_CONFIG=[directory of py_bamboo_config.properties]

Usage
=====
Specify build key and build number:

    build_key = "OXUI-ADEXCHANGESKIN"
    build_number = 540
    artifacts = get_build_artifacts(build_key, build_number)
    for i in artifacts:
    	print i
