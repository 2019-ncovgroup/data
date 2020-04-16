---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

# The nCov-Group Data Repository
{: .fs-9 .no_toc }

## AI- and HPC-enabled Generated Leads for SARS-CoV-2 Drugs
{: .no_toc }

This repository is for sharing data used and models produced to generate leads for potential SARS-CoV-2 drugs. These data will be updated regularly as the collaboration produces new results. Shared data are located on the ALCF Petrel data store ([here](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2F)), from where they can be retrieved via Globus. To access the data, users can register for a free Globus account ([here](<https://www.globus.org>)).


## Table of contents
{: .no_toc }

* TOC
{:toc}

Note:
{: .label .label-green }
A manuscript describing these data and the associated methodology and processing pipelines in detail is under preparation. A link will be posted here when it is available.

## Data Processing Pipeline
The data processing pipeline is used to compute different types of features and representations of billions of small molecules.  The pipeline first converts the SMILES representation for each molecule to the canonical SMILES form and removes duplicates. It then creates three different types of features: 1) molecular descriptors (using [Mordred](<https://github.com/mordred-descriptor/mordred));  2) molecular fingerprints that encode the structure of molecules; and 3) 2D images of the molecular structure.  These features are used as input to various machine learning and deep learning models that predict important characteristics including docking scores, toxicity, and more.

![Data processing pipeline](./assets/images/pipeline.png)

---

## Dataset Catalog
Below is a list of the collected datasets, along with links to the original work and the number of molecules included in the dataset.

Key | Full name | # Molecules
----- | --- | --- | --- 
BDB | [The Binding Database]((https://www.bindingdb.org/bind/index.jsp)) | 1,813,538 
CAS | [CAS COVID-19 Antiviral Candidate Compounds](https://www.cas.org/covid-19-antiviral-compounds-dataset) | 49,437
DCL | [DrugCentral Online Drug Compendium](http://drugcentral.org) | 3,981 
DBK | [Drugbank](https://www.drugbank.ca) | 9,678 
DUD | [DUDE database of useful decoys](http://dude.docking.org) | 99,782 
E15 | 15.5M-molecule subset of ENA | 15,547,091 
EDB | Enamine REAL subset | 310,782
EMO | [eMolecules](https://www.emolecules.com/info/products-data-downloads.html) | 25,946,988
ENA | [Enamine REAL Database](https://enamine.net/library-synthesis/real-compounds/real-database) | 1,211,723,723
FFI | [CureFFI](https://www.cureffi.org/2013/10/04/list-of-fda-approved-drugs-and-cns-drugs-with-smiles/) | 1,497 
G13 | [GDB-13](http://gdb.unibe.ch/downloads/)| 977,468,301
G17 | [GDB-17-Set](http://gdb.unibe.ch/downloads/)| 50,000,000
HOP | [Harvard Organic Photovoltaic Dataset](https://www.nature.com/articles/sdata201686) | 350
L1K | [L1000](http://www.lincsproject.org) | 10,141 |
MOS | [Molecular Sets (MOSES)](https://github.com/molecularsets/moses) | 1,936,962
PCH | [PubChem](https://www.ncbi.nlm.nih.gov/guide/data-software/) | 97,545,266
QM9 | [QM9 subset of GDB-17](http://quantum-machine.org/datasets/) | 133,885
REP | REP | 6,244
SAV | [Synthetically Accessible Virtual Inventory (SAVI)](https://cactus.nci.nih.gov/download/savi_download/) | 265,047,097
SUR | [SureChEML](https://surechembl.org/) | 17,915,384
ZIN | [ZINC15](http://zinc15.docking.org) | 1,225,804,829
    |        | **3,891,374,956** 

Notes:
{: .label .label-blue }
* The key for each dataset may be used in filenames in place of the full name in downloads elsewhere. 
* The numbers above may be less than what can be found at the source, due to conversion failures and/or version differences.
* These numbers do not account for de-duplication, within or between datasets.
* We may want to look at [MoleculeNet](http://moleculenet.ai/datasets-1)
* EDB needs a better description

## Dataset Downloads
Follow the links below to access canonical SMILES, molecular fingerprints, descriptors, and images (png format) for each dataset.

Key | Canonical SMILES | Fingerprints | Descriptors | Images
----- | --- | --- | ---  | ---
E15 | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline } | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline }
G13 | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
G17 | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
HOP | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
L1K | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
MOS | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
PCH | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
QM9 | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
REP | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
SAV | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
SUR | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}
ZIN | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline} | [Link](https://app.globus.org/file-manager?origin_id=a386b552-6086-11ea-9688-0e56c063f437&origin_path=%2Fdata%2Fdescriptors%2FDrunkBank_descriptors%2F){: .btn .btn-outline}

##  Data Extraction from Literature to Identify Antiviral Molecules
The data extraction team is working to extract a set of known antiviral molecules that have been previously tested against coronaviruses. 
This set of molecules will inform future efforts to screen candidates using simulated docking and more. There are two efforts current underway, a manual extraction effort, and an effort to build a named-entity recognition model that aims to automatically from a much larger literature corpus. 

### Manual Extraction of Antivirals from Literature
{: .no_toc }
Coming Soon
{: .label .label-yellow }

### Named-Entity Recognition Models for Identification of Antivirals
{: .no_toc }
Coming Soon
{: .label .label-yellow }





## Methodology and Data Formats

### Converting SMILES Canonical Form
{: .no_toc }


### Generating Fingerprints
{: .no_toc }


### Calculating Descriptors
{: .no_toc }


<!-- ## Contributing
Information on how to contribute to this project will be added shortly. -->

## Acknowledgements

Data storage and computational support for this research project has been generously supported by the following resources. The data generated have been prepared as part of the nCov-Group Collaboration, a group of over 200 researchers working to use computational techniques to address various challenges associated with COVID-19.

### Petrel Data Service at the Argonne Leadership Computing Facility (ALCF)
{: .no_toc }
This research used resources of the Argonne Leadership Computing Facility, which is a DOE Office of Science User Facility supported under Contract DE-AC02-06CH11357.

[Petrel](https://press3.mcs.anl.gov/petrel/){: .btn .btn-outline}

### Theta at the Argonne Leadership Computing Facility (ALCF)
{: .no_toc }
This research used resources of the Argonne Leadership Computing Facility, which is a DOE Office of Science User Facility supported under Contract DE-AC02-06CH11357.

[ALCF](https://www.alcf.anl.gov){: .btn .btn-outline}


### Frontera at the Texas Advanced Computing Center (TACC)
{: .no_toc }
[TACC](https://www.tacc.utexas.edu){: .btn .btn-outline}


### Comet at the San Diego Supercomputing Center (SDSC)
{: .no_toc }
[SDSC](https://www.sdsc.edu){: .btn .btn-outline}

