# QSAR_KING
4D-QSAR modeling program

This program base on LQTA-QSAR method.It can be used in the LINUX operating system.

For LQTA-QSAR, please cite:

>J.P.A. Martins, E.G. Barbosa, K.F.M. Pasqualoto, M.M.C. Ferreira. J. Chem. Inf. Model. 2009, 49, 1428–1436.

>E.G. Barbosa, M.M.C. Ferreira, Mol. Inf. 2012, 31, 75–84.
## Requirements
python >= 3

Gaussian >= 09

GaussianView

dos2unix

Acpype

AmberTools >= 2017

Gromacs >= 2018

dos2unix

OpenBabel

VMD
## Installing QSAR_KING
Put the QSAR KING package in any directory you want to install

Open the terminal at the directory, type:

>$ sudo echo "(your path)/files" >> $HOME/.bashrc

>$ sudo chmod -R a+x files/

>$ python -m pip install --upgrade pip

>$ pip install --upgrade numpy sklearn matplotlib
## How to use QSAR_KING
### Draw the molecular structure and use Gaussian to optimize the structure
### Prepare the following 4 (or 5) *.txt files：
#### 1. names.txt
It contains all names of compounds,The text file will be:

>m01

>m02

>m03
#### 2. index.txt
Each line of this file must contain the atom indexes from Gaussian that will be aligned, separeted by "tab". For example, the Gaussian atoms indexes of m01 and m02 that will be aligned are 1,3,5,7. For m03 these atoms have different Gaussian indexes, that are 2,4,5,9. The "index.txt" file will be:

>1  3  5	7
   
>1	3	5	7
   
>2	4	5	9

If the "names.txt" file has a different order, the same order must beused in "index.txt" file
#### 3. act.txt
It contains the bioactive value (pIC<sub>50</sub> value) of all compounds, corresponding to the name.txt. The text file will be:

>3.2

>5.4

>6.1
#### 4. ref.txt
It contains the name of the reference compound used in the alignment step. For example, m02 was chosen as the alignment reference. The text file will be:

>m02

#### 5. test.txt (Optional)
Manually specify which compounds are used as test sets. If there is no such file, the program will randomly pick one-fifth of the compounds as a test set. For example, m02 is in the test set and m01,m03 are in the training set, The text file will be:

>m02

### Run the program
Put all *.log, *.gesp and *.txt files in a directory, open the terminal and navigate to that directory,type:

>$ QSAR_KING

Wait until it done, your 4D_QSAR model will be built automatically by QSAR_KING!
