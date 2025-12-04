# larmip-ais

This module ports into the FACTS framework the Antarctic dynamic contribution emulation of the Linear response of the Antarctic ice sheet to future warming Model Intercomparision Project (LARMIP) 2020. It augments it with a surface mass balance term following IPCC AR5.

See [https://github.com/ALevermann/larmip2020](https://github.com/ALevermann/larmip2020) for the original LARMIP2020 code.

Cite as:

Projecting Antarctica's contribution to future sea level rise from basal ice-shelf melt using linear response functions of 16 ice sheet models (LARMIP-2)

A. Levermann, R. Winkelmann, T. Albrecht, H. Goelzer, N.R. Golledge, R. Greve, P. Huybrechts, J. Jordan, G. Leguy, D. Martin, M. Morlighem, F. Pattyn, D. Pollard, A. Quiquet, C. Rodehacke, H. Seroussi, J. Sutter, T. Zhang, J. Van Breedan, R. Calov, R. DeConto, Ch. Dumas, J. Garbe, G.H. Gudmundsson, M.J. Hoffman, A. Humbert, T. Kleiner, W. Lipscomb, M. Meinshausen, E. Ng, S.M.J. Nowicki, M. Perego, S.F. Price, F. Saito, N.J. Schlegel, S. Sun, R.S.W. van de Wal

Earth System Dynamics 11 (2020) 35-76, doi 10.5194/esd-11-35-2020.

(copied from larmip/AIS readme in FACTS 1)

## Example

This application can run on emissions-projected climate data. 

### Setup

Clone the repository and create directories to hold input and output data. 

```shell
mkdir -p ./data/input
# larmip fit data
curl -sL https://zenodo.org/record/7478192/files/larmip_icesheet_fit_data.tgz | tar -zx -C ./data/input

# larmip project data
curl -sL https://zenodo.org/record/7478192/files/larmip_icesheet_project_data.tgz | tar -zx -C ./data/input

# fingerprint data
curl -sL https://zenodo.org/record/7478192/files/grd_fingerprints_data.tgz | tar -zx -C ./data/input

#Make directory for inputs
mkdir -p ./data/output
# Add location file to input dir 
echo "New_York	12	40.70	-74.01" > ./data/input/location.lst
```

>[!IMPORTANT]
> This module **requires** a `climate.nc` file that is the output of the FACTS FAIR module, which is created outside of this prototype. Before running the example, manually move the file into `./data/input` and ensure that the filename matches that passed to `climate-file`. The number of samples (`--nsamps`) drawn in the FAIR run must pass the number of samples specified in this run. 


Run the application:
```shell
docker run --rm \ 
-v /path/to/data/input:/mnt/larmip_data_in \
-v /path/to/data/output:/mnt/larmip_data_out \
larmip-ais \
--scenario 'ssp245' \
--pipeline-id 'my_pipeline_id' \
--climate-data-file /mnt/larmip_data_in/climate.nc \
--refyear-start 1850 \
--refyear-end 1900 \
--year-start 1900 \
--year-end 2300 \
--scaling-coefficients-dir /mnt/larmip_data_in/ScalingCoefficients \
--r-functions-dir /mnt/larmip_data_in/RFunctions \
--nsamps 2000 \
--seed 1234 \
--pyear-start 2020 \
--pyear-end 2150 \
--pyear-step 10 \
--baseyear 2005 \
--ais-global-output-file /mnt/larmip_data_out/ais_gslr.nc \
--eais-global-output-file /mnt/larmip_data_out/eais_gslr.nc \
--wais-global-output-file /mnt/larmip_data_out/wais_gslr.nc \
--pen-global-output-file /mnt/larmip_data_out/pen_gslr.nc \
--smb-global-output-file /mnt/larmip_data_out/smb_gslr.nc \
--location-file /mnt/larmip_data_in/location.lst \
--chunksize 50 \
--fingerprint-dir /mnt/larmip_data_in/FPRINT/ \
--wais-local-output-file /mnt/larmip_data_out/wais_lslr.nc \
--eais-local-output-file /mnt/larmip_data_out/eais_lslr.nc \
--ais-local-output-file /mnt/larmip_data_out/ais_lslr.nc

```

## Features
```shell
Usage: larmip-ais [OPTIONS]

Options:
  --scenario TEXT                 Emission scenario for ice sheet projections
                                  [required]
  --pipeline-id TEXT              Unique identifier for this instance of the
                                  module  [required]
  --climate-data-file TEXT        NetCDF4/HDF5 file containing surface
                                  temperature data  [required]
  --refyear-start INTEGER         Start year for reference period  [default:
                                  1850]
  --refyear-end INTEGER           End year for reference period  [default:
                                  1900]
  --year-start INTEGER            Start year for temperature series  [default:
                                  1900]
  --year-end INTEGER              End year for temperature series  [default:
                                  2300]
  --scaling-coefficients-dir TEXT
                                  [required]
  --r-functions-dir TEXT          [required]
  --nsamps INTEGER                [required]
  --seed INTEGER
  --pyear-start INTEGER           [default: 2000]
  --pyear-end INTEGER             [default: 2300]
  --pyear-step INTEGER            [default: 10]
  --baseyear INTEGER              [default: 2005]
  --cyear-start INTEGER
  --cyear-end INTEGER
  --ais-global-output-file TEXT   File path to save AIS-wide sea-level
                                  projections
  --eais-global-output-file TEXT  File path to save East Antarctic Ice Sheet
                                  sea-level projections
  --pen-global-output-file TEXT   File path to save Peninsular Antarctica sea-
                                  level projections
  --wais-global-output-file TEXT  File path to save West Antarctic Ice Sheet
                                  sea-level projections
  --smb-global-output-file TEXT   File path to save Antarctic SMB sea-level
                                  projections
  --location-file TEXT            File that contains name, id, lat, and lon of
                                  points for localization
  --chunksize INTEGER             Number of locations to process at a time
                                  [default: 50]
  --fingerprint-dir TEXT          Directory containing ice sheet fingerprints
  --wais-local-output-file TEXT   File path to save localized West Antarctic
                                  Ice Sheet sea-level projections
  --eais-local-output-file TEXT   File path to save localized East Antarctic
                                  Ice Sheet sea-level projections
  --ais-local-output-file TEXT    File path to save localized total Antarctic
                                  sea-level projections
  --help                          Show this message and exit.
```
See this help documentation by passing the `--help` flag when running the application, for example:
```shell
docker run --rm larmip-ais --help
```

## Build the container locally
You can build the container with Docker by running the following command from the repository root:

```shell
docker build -t larmip-ais .
```

## Results
This module writes local and global SLR contribution projection NetCDF files for AIS, EAIS, WAIS and global for Antarctic peninsula and Antarctic surface mass balance. 

## Support 
Source code is available online at https://github.com/fact-sealevel/larmip-ais. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/fact-sealevel/larmip-ais/issues.