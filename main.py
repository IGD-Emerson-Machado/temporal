import pandas as pd
import math
from Ing_library.loadfiles import LoadFiles
from Ing_library.databases import GenerateDatasets


## min 40  -> 46


if __name__ == "__main__":
    w_n='HOKCHI_11DES'

    sample_rate=10
    sep=','
    sample_rate = 5

    L=LoadFiles()
    G=GenerateDatasets

    file='./WH/WH_offset_wells.csv'
    fileWh=L.Load_File(file, sep)

    file='./Trajectory/HOKCHI_11DES.csv'
    fileTrj=L.Load_File(file, sep)

    print(fileWh)
    print(fileTrj)

    vars=L.wh_creation(fileWh)


    fileTrj=L.proces_Trajectory_file(fileTrj)

    dataset=G.reference_dataset(w_n, fileTrj, sample_rate)
    prsesFileHeader=L.proces_wh_file(fileWh)
    G.well_path(dataset,vars['well_wh'])


