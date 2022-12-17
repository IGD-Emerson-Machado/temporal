import pandas as pd
import math

class GenerateDatasets():

    def reference_dataset(w_n, w_traj_ds,sample_rate):
        #sample_rate = 0.15
        dataset={}
        numb_idx_w1 = int(((w_traj_ds['MD'].max()) / sample_rate)+1)
        idx=[0]
        for x in range(numb_idx_w1):
            if x == 0:#first value of depth have to be zero
                continue
            else:
                idx.append(idx[x-1] + sample_rate)
        dataset[w_n+'_wellpath'] = pd.DataFrame ({'Depth': idx}) 
        dataset[w_n+'_wellpath'] = dataset[w_n+'_wellpath'].set_index('Depth')
        dataset[w_n+'_wellpath'] = pd.concat([dataset[w_n+'_wellpath'], w_traj_ds.groupby(pd.Grouper('MD')).mean()], axis=1).interpolate('linear')
        print('Data set was created: ', w_n+'_wellpath')
        print(dataset['HOKCHI_11DES_wellpath'])
        return dataset['HOKCHI_11DES_wellpath']


    def well_path(master_ds,wh):
        d_x = [0]
        d_n = [0]
        d_e = [0]
        for x in range(len(master_ds)):
            if x == 0:
                continue
            else:
                d_xi = math.sin(master_ds.iloc[x,:]['INC'] * math.pi/180)*(master_ds.index[x]-master_ds.index[x-1])
                d_ni = (master_ds.index[x]-master_ds.index[x-1])*math.sin(master_ds.iloc[x,:]['INC'] * math.pi/180)*math.cos(master_ds.iloc[x,:]['AZ'] * math.pi/180)
                d_ei = (master_ds.index[x]-master_ds.index[x-1])*math.sin(master_ds.iloc[x,:]['INC'] * math.pi/180)*math.sin(master_ds.iloc[x,:]['AZ'] * math.pi/180)
                d_x.append(d_x[x-1] + d_xi)
                d_n.append(d_n[x-1] + d_ni)
                d_e.append(d_e[x-1] + d_ei)
        master_ds['THD'] = d_x
        master_ds['NOFFSET'] = d_n
        master_ds['EOFFSET'] = d_e
        master_ds['TVDBGL'] = master_ds[['TVD']]-float(wh['Elevation'])- float(wh['EGL'])
        master_ds['TVDSS'] = master_ds[['TVD']]-float(wh['Elevation'])
        master_ds['NLOC'] = (master_ds[['NOFFSET']]) + float(wh['Y'])
        master_ds['ELOC'] = (master_ds[['EOFFSET']])+ float(wh['X'])
        print('Well path was created succesfully' )
        print(master_ds)
        
        return master_ds
        


