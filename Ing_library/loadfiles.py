import pandas as pd

class LoadFiles():

        # load file to dataseet
    def Load_File(self,file,sp):
        #Code above call the Well Head data, capture the units and delate de units row
        return pd.read_csv(file, sep=sp) 

        # header WH
    def get_header_file(self,file):
        return file.iloc[[1]]


    def proces_wh_file(self,file):
        procesfile = file.drop([0], axis=0).reset_index(drop=True)
        procesfile[['X', 'Y', 'Elevation', 'EGL', 'Total_depth']] = procesfile[['X', 'Y', 'Elevation', 'EGL', 'Total_depth']].astype('float')
        print(procesfile)
        return procesfile


        # header trajectory
    def proces_Trajectory_file(self,file):
        file = file.drop([0], axis=0).astype('float').reset_index(drop=True)
        print(file)
        return file


    def wh_creation(self, file):
        # w_i = str(input('Enter well number(ej: w1): '))
        # well_name = str(input('Enter well name (as Excel): '))

        print("""
                
            Pozos disponibles
                
                """)

        for x in range(len(file)):
            if x == 0:
                continue
            else:       
                print(str(x)+' - '+file['Well'][x])
                print('')
         
        x=int(input('inserte numero del pozo: '))

        # index=file['Well'][x]
        # well_wh = file.loc[file['Well']==file].reset_index(drop=True)
        # well_EGL = file.loc[file['Well']==file]['EGL']
        # well_ERT = file.loc[file['Well']==file]['Elevation']

        well_wh = file.iloc[x]
        well_EGL = file['EGL'][x]
        well_ERT = file['Elevation'][x]
        well_ERT = well_EGL + well_ERT      

        return {
            'well_wh':well_wh,
            'well_EGL':well_EGL,
            'well_ERT':well_ERT
        }     
        