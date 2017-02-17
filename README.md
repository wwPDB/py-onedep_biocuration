## OneDep Validation Web Service Interface

### Introduction
The OneDep validation web service was developed as a
wwPDB effort to augment the stand alone [validation server](https://validate.wwpdb.org) by providing a programmatic remote
access to such services.

This service is provided as a Python package. Once installed, access is provided using a
command line client or pragmatically using a Python API.

### Installation

Installation is via the program [pip](https://pypi.python.org/pypi/pip).

```bash
pip install onedep_api
```

### Command Line Usage
A binary script is installed called ```onedep_validate_cli``` which is a front end that invokes the packages APIs.

Example scripts that utilize the client and API can be [found here](https://onedep-apiws.wwpdb.org/files/examples-installed.tar.gz).


#### Start a new session
You must start a new session. The system keeps track of the current working session in the file ```~/.onedep_current_session``` This can be changed with the *--session_file* argument.

```
onedep_validate_cli --new_session
```

##### Upload data
The validation API supports a limited number of file types and formats.
To upload a file, you need to specify the file type with the *filetype* from the following table.


|  Data file  |  Format  | filetype |
--- | --- | ---
model | PDBx/mmCIF | model
structure factor | mmCIF | structure-factors
NMR chemical shifts | NMRstar | nmr-chemical-shifts
NMR restraints  | any | nmr-restraints
EM map | CCP4 map | em-volume


PDBx/mmCIF formatted files are available from REFMAC and Phenix, or can be created by using [pdb_extract](http://pdb-extract.wwpdb.org). MTZ to mmCIF conversion can be performed with [sf-tool](http://sf-tool.wwpdb.org/) or in CCP4 with ```mtz2various```.

```
onedep_validate_cli --input_file <filename> --input_type <filetype>
```

Repeat until all files are uploaded.

#### Run validation

Initiate the validation with the command:

```
onedep_validate_cli --validate
```

You can periodically check if the validation is running or complete with the command:

```
onedep_validate_cli --status
```

or if you would like a value of 0 or 1:

```
onedep_validate_cli --test_complete
```

#### Retrieving results

When complete, you can retrieve the results of the validation

```
onedep_validate_cli --output_file <pdf file> --output_type validation-report-full
onedep_validate_cli --output_file <xml file> --output_type validation-data

```



### Python API

The Python API was developed to provide simple access to the web validation
services in a programmatic manner.


#### Validation
The Validate class provides access to all services, from session creation, file upload and download, calculation initiation and status retrieval.

```python
from onedep import __apiUrl__
from onedep.api.Validate import Validate

def displayStatus(sD, exitOnError=True):
    if 'onedep_error_flag' in sD and sD['onedep_error_flag']:
        print("OneDep error: %s\n" % sD['onedep_status_text'])
        if exitOnError:
            raise SystemExit()
    else:
        if 'status' in sD:
            print("OneDep status: %s\n" % sD['status'])

# Given:
# modelFilePath contains the path to the model file
# sfFilePath contains the path to the structure factor file
val = Validate(apiUrl=apiUrl)
rD = val.newSession()
displayStatus(rD)
rD = val.inputModelXyzFile(modelFilePath)
rD = val.inputStructureFactorFile(sfFilePath)
displayStatus(rD)
rD = val.run()
displayStatus(rD)
#
#   Poll for service completion -
#
it = 0
sl = 2
while (True):
   #    Pause -
   it += 1
   pause = it * it * sl
   time.sleep(pause)
   rD = val.getStatus()
   if rD['status'] in ['completed', 'failed']:
      break
   print("[%4d] Pausing for %4d (seconds)\n" % (it, pause))
   #
   #
lt = time.strftime("%Y%m%d%H%M%S", time.localtime())
fnR = "xray-report-%s.pdf" % lt
rD = val.getReport(fnR)
```
