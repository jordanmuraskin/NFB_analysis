################## second level
# import glob
from nipype.interfaces.fsl import Merge
from pandas import read_csv


dataType=['moral','msit']
t='cope'
for dt in dataType:
    #get files

    df=read_csv('%s_analysis.csv' % dt)
    x=[]
    for i in range(3,5):
            for subj in df['x']:
                filepath = '/home2/cfroehlich/nfb3_preprocessed/working/%sft/ftest/_subject_id_%s/modelestimate/mapflow/_modelestimate0/results/%s%d.nii.gz' % (dt,subj,t,i)
                x.append(filepath)
        subjs = len(x)
        merger = Merge()
        merger.inputs.in_files = x
        merger.inputs.dimension = 't'
        merger.inputs.output_type = 'NIFTI_GZ'
        merger.inputs.out_file = './%s%d_merged.nii.gz'
        merger.run()
