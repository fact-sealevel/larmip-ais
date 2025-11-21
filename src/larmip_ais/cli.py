from larmip_ais.larmip_icesheet_preprocess import larmip_preprocess_icesheet
from larmip_ais.larmip_icesheet_fit import larmip_fit_icesheet, larmip_fit_smb 
from larmip_ais.larmip_icesheet_project import larmip_project_icesheet
from larmip_ais.larmip_icesheet_postprocess import larmip_postprocess_icesheet
import numpy as np

import click 

@click.command()
@click.option('--scenario', 
              type=str, 
              required=True, 
              help="Emission scenario for ice sheet projections",
              envvar="LARMIP_AIS_SCENARIO")
@click.option('--pipeline-id', 
              type=str, 
              default="mypipelineid",
              required=True, 
              help="Unique identifier for this instance of the module",
              envvar="LARMIP_AIS_PIPELINE_ID")
@click.option('--climate-data-file', 
              type=str, 
              required=True, 
              help="NetCDF4/HDF5 file containing surface temperature data",
              envvar="LARMIP_AIS_CLIMATE_DATA_FILE")
@click.option('--refyear-start',
              type=int,
              default=1850,
              show_default=True,
              help="Start year for reference period",
              envvar="LARMIP_AIS_REFYEAR_START"
              )
@click.option('--refyear-end',
              type=int,
              default=1900,
              show_default=True,
              help="End year for reference period",
              envvar="LARMIP_AIS_REFYEAR_END"
              )
@click.option('--year-start',
              type=int,
              default=1900,
              show_default=True,
              help="Start year for temperature series",
                envvar="LARMIP_AIS_YEAR_START"
                )   
@click.option('--year-end',
              type=int,
              default=2300,
              show_default=True,
              help="End year for temperature series",
                envvar="LARMIP_AIS_YEAR_END"
                )
@click.option('--scaling-coefficients-dir',
              type=str,
              default=None,
              required=True)
@click.option('--r-functions-dir',
              type=str,
              default=None,
              required=True,
            )
@click.option('--nsamps',
                type=int,
                required=True,
)
@click.option('--seed',
                type=int,
)
@click.option('--pyear-start',
                type=int,
                default=2000,
                show_default=True,
)
@click.option('--pyear-end',
                type=int,
                default=2300,
                show_default=True,
)
@click.option('--pyear-step',
                type=int,
                default=10,
                show_default=True,
)
@click.option('--baseyear',
                type=int,
                default=2005,
                show_default=True,
)
@click.option('--cyear-start',
                type=int,
)
@click.option('--cyear-end',
                type=int,
)
@click.option('--ais-global-output-file',
                type=str,
                help="File path to save AIS-wide sea-level projections",
)
@click.option('--eais-global-output-file',
                type=str,
                help="File path to save East Antarctic Ice Sheet sea-level projections",
)
@click.option('--pen-global-output-file',
                type=str,
                help="File path to save Peninsular Antarctica sea-level projections",
)
@click.option('--wais-global-output-file',
                type=str,
                help="File path to save West Antarctic Ice Sheet sea-level projections",
)
@click.option('--smb-global-output-file',
                type=str,
                help="File path to save Antarctic SMB sea-level projections",
)
@click.option('--location-file',
                type=str,
                help="File that contains name, id, lat, and lon of points for localization",
)
@click.option('--chunksize',
                type=int,
                default=50,
                show_default=True,
                help="Number of locations to process at a time",
)
@click.option('--fingerprint-dir',
                type=str,
                default=None,
                help="Directory containing ice sheet fingerprints",
)
@click.option('--wais-local-output-file',
                type=str,
                help="File path to save localized West Antarctic Ice Sheet sea-level projections",
)
@click.option('--eais-local-output-file',
                type=str,
                help="File path to save localized East Antarctic Ice Sheet sea-level projections",
)
@click.option('--ais-local-output-file',
                type=str,
                help="File path to save localized total Antarctic sea-level projections",
)
def main(scenario,
         pipeline_id,
         climate_data_file,
         refyear_start,
         refyear_end,
         year_start,
         year_end,
         scaling_coefficients_dir,
         r_functions_dir,
         nsamps,
         seed,
         pyear_start,
         pyear_end,
         pyear_step,
         baseyear,
         cyear_start,
         cyear_end,
         ais_global_output_file,
         eais_global_output_file,
         pen_global_output_file,
         wais_global_output_file,
         smb_global_output_file,
         location_file,
         chunksize,
         fingerprint_dir,
         wais_local_output_file,
         eais_local_output_file,
         ais_local_output_file
         ):
    
    click.echo("Hello from larmip-ais!")
    #preprocess
    preprocess_dict = larmip_preprocess_icesheet(
        scenario=scenario, 
        pipeline_id=pipeline_id, 
        fname=climate_data_file,
        refyear_start=refyear_start,
        refyear_end=refyear_end,
        year_start=year_start,
        year_end=year_end
    )

    #fit - 2 different commands here
    fit_icesheets_dict = larmip_fit_icesheet(pipeline_id=pipeline_id,
                                       scaling_coefficients_dir=scaling_coefficients_dir,
    )

    fit_smb_dict = larmip_fit_smb(pipeline_id=pipeline_id,
                                   preprocess_dict=preprocess_dict)
    
    #make targyears
    targyears = np.arange(pyear_start, pyear_end+1, pyear_step)
    #project
    project_dict = larmip_project_icesheet(
        pipeline_id=pipeline_id,
        preprocess_data=preprocess_dict,
        fit_icesheets_data=fit_icesheets_dict,
        fit_smb_data=fit_smb_dict,
        nsamps=nsamps,
        targyears=targyears,
        baseyear=baseyear,
        seed=seed,
        cyear_start=cyear_start,
        cyear_end=cyear_end,
        rfunctions_dir=r_functions_dir,
        ais_fpath=ais_global_output_file,
        eis_fpath=eais_global_output_file,
        pen_fpath=pen_global_output_file,
        wais_fpath=wais_global_output_file,
        smb_fpath=smb_global_output_file
    )

    #postprocess
    larmip_postprocess_icesheet(
        project_dict = project_dict,
        location_file = location_file,
        chunksize = chunksize,
        pipeline_id = pipeline_id,
        fingerprint_dir = fingerprint_dir,
        wais_local_output_file = wais_local_output_file,
        eais_local_output_file = eais_local_output_file,
        ais_local_output_file = ais_local_output_file
    )