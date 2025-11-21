# larmip-ais

This module ports into the FACTS framework the Antatctic dynamic contribution emulation of the Linear response of the Antarctic ice sheet to future warming Model Intercomparision Project (LARMIP) 2020. It augments it with a surface mass balance term following IPCC AR5.

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
