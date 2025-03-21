# GaussNBO ⚛️

![GaussNBO](./statics/header.png)

![Downloads](https://img.shields.io/pypi/dm/GaussNBO) ![PyPI](https://img.shields.io/pypi/v/GaussNBO) ![License](https://img.shields.io/pypi/l/GaussNBO)

A Python package for parsing Natural Bond Orbital (NBO) data from Gaussian log files.

## What is NBO? 🤔

`Natural Bond Orbital` (NBO) analysis is a widely used computational chemistry method that offers detailed insights into molecular bonding and interactions. It converts the delocalized molecular orbitals (MOs) from quantum chemical calculations into localized orbitals that are more closely aligned with the Lewis structure representation of molecules. NBO analysis aids chemists in understanding:

- Chemical bonding and hybridization: It identifies the nature of chemical bonds and the hybridization of atoms.
- Charge distribution and polarization: NBO analysis provides information on the distribution of electronic charge within the molecule and the polarization of bonds.
- Donor-acceptor interactions: It helps in analyzing interactions such as electron donation from lone pairs or bonds and electron acceptance into empty orbitals.
- Resonance and hyperconjugation effects: NBO can describe resonance structures and the effects of hyperconjugation, both of which influence molecular stability and reactivity.
- Reaction mechanisms and transition states: It contributes to the understanding of reaction pathways, including insights into the electronic structure of transition states.

## About GaussNBO 📊

GaussNBO is a Python package designed to parse NBO data from Gaussian log files. It provides an easy-to-use interface for extracting and analyzing NBO results, including:

- Natural Bond Orbitals (NBOs)
- Natural Atomic Orbitals (NAOs)
- Natural Localized Molecular Orbitals (NLMOs)
- Second-order perturbation theory analysis
- and more...

## Features 🎉

- Parse NBO data from Gaussian log files
- Extract NBO results, including NBOs, NAOs, NLMOs, and second-order perturbation theory analysis
- Easy-to-use interface for analyzing NBO data
- Compatible with `Gaussian NBO Version 3.1`
- Visualization of NBO analysis results in browser

## Installation 📦

To install GaussNBO, run the following command:

```bash
pip install GaussNBO
```

## Usage 📝

Here's an example of how to use GaussNBO:

```python
import GaussNBO as gnbo

# Process a Gaussian log file and view results in browser
nbo_data = gnbo.launch('path/to/file.log', view_browser=True)

# Or just get the parsed data without opening browser
nbo_data = gnbo.launch('path/to/file.log', view_browser=False)
```

## Contributing 🤝

Contributions to GaussNBO are welcome! Please fork the repository, make your changes, and submit a pull request.


## License 📜

GaussNBO is released under the MIT License. This means you are free to use, modify, and distribute this software in your own projects, provided that you include proper attribution to the original author. Please ensure that my name is retained in any derivative works or distributions of this code.

## ❓ FAQ

For any question, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/)

## 👥 Authors

- [@sinagilassi](https://www.github.com/sinagilassi)