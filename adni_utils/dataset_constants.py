"""
Constants used by the baseline models to load data when running experiments.
"""

# Data Vars:
source_path = '/projects/francisco/data/caffe/standardized/combined/'
# Sides to iterate over;
# ie: sides  = ['l', 'r', 'b']
sides = ['b']
structure = 'hc'

# Datasets to iterate over:
# ie. datasets = ['mci_cn', 'ad_cn', 'ad_mci_cn']
adni_datasets = ['ADNI_Cortical_Features']
omit_class = 2 # Set to NONE to do 3-way classification or when using two-class datasets

# Use Fused only (otherwise use candidate segmentations)
use_fused = True
balance = True

# List of fold filename extensions to iterate over:
# ie. folds = ['_T1', '_T2', '_T3']
folds = [''] # No folds.

# Change these when running Spearmint experiments which use only the main and don't iterate over datasets or sides:
default_side = 'l' # Valid values: l, r, b
default_dataset = 'ADNI_Cortical_Features' # Valid values: mci_cn, ad_cn

# How many trials to run per fold (useful in the case of randomly sampled subsets of data, or randomized algos):
n_trials = 10

class_name_map = {
    'ad_mci_cn': ['ad', 'cn', 'mci'],
    'ad_cn': ['ad', 'cn'],
    'mci_cn': ['cn', 'mci'],
    'ADNI_Cortical_Features': ['ad', 'cn', 'mci']
}