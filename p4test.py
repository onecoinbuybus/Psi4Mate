import numpy as np
import psi4

import qm
import utils
from collections import Counter
from collections import defaultdict

from rdkit import Chem
from rdkit.Chem import AllChem



smiles = "*C(C*)c1ccccc1"
ter_smiles = "*C"

# 计算条件
omp_psi4 = 2
mpi = 2
omp = 2
gpu = 0
mem = 1000
chain_length = 30

smiles = '*C(C*)c1ccccc1'

mol = utils.mol_from_smiles(smiles)



work_dir = './work_dir'
ter_smiles = "*C"
ter = utils.mol_from_smiles(ter_smiles)
qm.assign_charges(
    ter,
    charge="RESP",
    opt=True,
    work_dir=work_dir,
    omp=omp_psi4,
    memory=mem,
    log_name="ter",
)

print('test ok')
