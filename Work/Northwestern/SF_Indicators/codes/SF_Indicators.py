"""
 
    Created:      Wed/06/21/17 (Northwestern)
    Last update:  Wed/06/21/17 (Northwestern)
    Author:       Jose Flores

    Class that works with cllient: make_spectra.py
"""

#######################################################################

#...Import key external routines:

import numpy as np
import h5py
import matplotlib.pyplot as plt
import os, copy


#...Set up font size:
fontsize = 14

#######################################################################

class Spectrum:

    # __doc__:
    """This class extracts spectrum from FIRE galaxies."""

    #---Class initialization:
    def __init__(self, platform = 'stampede'):

        self.platform = platform

        #---Set up paths:
        self._setup_paths()

        #---Load data:
        self._load_data()
    
        #---Plot Spectra:
        self.plot_Lum_vs_Lambda()


################## INITIALIZATION PRIVATE FUNCTIONS ###################

#---Private Class Function: Set up paths for simulated data.
    def _setup_paths(self):
    
        #---On Stampede:
        if self.platform == 'stampede':
            
            pass
        
        #---On Local Computer:
        elif self.platform == 'local':
            
            #...Set up path to simulations:
            self.user_path = '/Users/Jose_Flores/'
            self.snap_path = self.user_path+'Work/Northwestern//martinsparre-fsps-fire-357676161dc3/Stuff/SSP_Library.hdf5'
#        print self.snap_path


#######################################################################

#---Private Class Function: Load data.
    def _load_data(self):
    
        #---On Stampede:
        if self.platform == 'stampede':
        
            #---Load data:
            pass
    
        #---On Local Computer:
        elif self.platform == 'local':
            
            #...Retrieve hdf5 data:
            data_hdf5 = h5py.File(str(self.snap_path),'r')
            
            #...Load data:
            self.Log_Met    = np.array(data_hdf5.get('logMetallicity'))
            self.Log_Age    = np.array(data_hdf5.get('DataGroup_0000/LogAge'))
            self.Lambda     = np.array(data_hdf5.get('DataGroup_0000/Lambda'))
            self.Lum_Lambda = np.array(data_hdf5.get('DataGroup_0000/Luminosity_Lambda'))

#            print "Log_Met",    self.Log_Met
#            print "Log_Age",    self.Log_Age
#            print "Lambda",     self.Lambda
#            print "Lum_Lambda", self.Lum_Lambda

#######################################################################

#---Creates a Total Luminosity vs Wavelength Plot

#    def plot_Lum_vs_Lambda(self, field = 'Total_Spectrum', save_frame=False, eps_tag=False,):
#
#        # ----Set up save tag:
#        plot_tag =  field + '_spect'
#        save_tag = plot_tag
#
#
#        # ----Plotting Axes
#        fig = plt.figure()
#        self.x_axis = self.Lambda
#        self.y_axis = self.Lum_Lambda[0]
#
#        plt.plot(np.log10(self.x_axis),np.log10(self.y_axis),'-')
#        plt.xlabel(r'$\log \lambda $ [${\rm \AA{}}$]',fontsize=16)
#        plt.ylabel(r'$\log L_\lambda $ [L$_\odot$  ${\rm \AA{}}^{-1}$]',fontsize=16)
#
#
#        # ----Makes Frames True/False
#        if save_frame == False:
#
#            #...If saved plots directory doesn't exit, make one.
#            if not os.path.exists('./plots'): os.mkdir('./plots')
#
#            #...Set up file type:
#            file_type = '.pdf'
#            if eps_tag == True: file_type = '.eps'
#
#            #...Save pdf:
#            plt.savefig('./plots/'+save_tag+'_'+file_type)
#
#        elif save_frame == True:
#
#            #...If saved frames directory doesn't exit, make one.
#            if not os.path.exists('./frames'): os.mkdir('./frames')
#
#            #...Set up file type:
#            file_type = '.png'
#
#            #...Save pngs:
#            for ifr in np.arange(6):
#                plt.savefig('./frames/frame_'+str((self.isnap)*6+ifr).zfill(4)+'.png')
#
#        #...Report and close
#        print "SAVE: ", save_tag
#        plt.close()

"This whole block commented works fine and saves a broadband spectrum vs wavelength plot onto a directory it creates."

#######################################################################




"I am working on a for loop (reason why I commented out the block above, once I know my for loop below works fine I will integrate it into the same fucntion and have it save both the Broadband vs Wavelength and Luv, Lha vs time in some directory) that will loop through everysingle array in Luminoisty_Lambda and then will give it some if statement to extract these values needed for UV or Ha. The limits on the if statement are arbitrary at the moment. I have set minor 'knobs' like field in the function to later just change it to Ha if we decide to examine it etc..."



#Need a for loop that will loop throgh every single group and print out and array with 94 entries.
#The loop will sum all of the lum_lamb in the UV wavelength and produce the array mentioned above.

    def plot_Lum_vs_Lambda(self, field = 'UV', save_frame=False, eps_tag=False,):

        # ----Set up save tag:
#        plot_tag =  field + '_spect'
#        save_tag = plot_tag

         self.NewL_Lambda = []
         for i in range(len(self.Log_Age)):
             for j in range(len(self.Lambda)):
        
                 self.sing_lum_lamb = self.Lum_Lambda[i][j]
                 self.NewL_Lambda.append(self.sing_lum_lamb)
         print len(self.NewL_Lambda)

#         if (self.sing_lum_lamb > 10.0) & (self.sing_lum_lamb < 4000.0):
#             self.sum_lum_lamb = np.sum(self.sing_lum_lamb)
#             print self.sum_lum_lamb












