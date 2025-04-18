[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed by [Robert Haase](https://haesleinhuepf.github.io), [ScaDS.AI Dresden/Leipzig](http://scads.ai/) under a
[Creative Commons Attribution 4.0 International License][cc-by] unless mentioned otherwise.

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# Bio-image Data Science

This repository contains training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. 
Corresponding PPTx files can be found [on zenodo](https://doi.org/10.5281/zenodo.15182562).

## Teaching Goal

Students learn the full workflow of common bio-image data
science projects to a degree that they can execute a scientific
data analysis project in this context on their own. They will be
familiar with common bio-image analysis algorithms and
workflows, how to choose them according to a scientific goal,
and how to measure quality of derived results. Attending the
lecture and executing the practicals qualifies the students to
work as bio-image data scientist in the pharmaceutical industry
or basic biological research.

## Course contents

* [Introduction to Bio-image Data Science](01_Introduction_BIDS_2025.pdf) (April 11th 2025)
  * Basics of microscopy
  * Introduction to Bio-image Analysis
  * Exercises:
    * [Setting up a local environment](01a_setting_up_local_environment/readme.md)
    * [Setting up Jupyter Hub at Scientific Computing / Leipzig University](01b_setting_up_sc_ulei_environment/readme.md)
    * [Execute the trailer notebook](01c_testing_environment/trailer.ipynb)


## Pre-requisites
* Basic Python programming skills are required

## Literature
* [Bioimage Data Analysis Workflows ‒ Advanced Components and Methods. Editors: Kota Miura, Nataša Sladoje. 2022](https://link.springer.com/book/10.1007/978-3-030-76394-7)
* [A Hitchhiker's guide through the bio-image analysis software universe. Haase et al. FEBS Letters. Volume 596, Issue 19 p. 2472-2485](https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451)
* [Bio Image Analysis Notebooks, Haase et al. 2024 DOI: 10.5281/zenodo.10465773](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/)

More literature might be added during the lecture.

## Covered Python libraries
In this course we will use the following Python libraries to analyse microscopy image data
* [numpy](https://numpy.org)
* [scipy](https://www.scipy.org/)
* [scikit-image](https://scikit-image.org/)
* [clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype).
* [napari](https://napari.org)
* [scikit-learn](https://scikit-learn.org/)
* [apoc](https://github.com/haesleinhuepf/apoc)
* [OpenAI API](https://openai.com/blog/openai-api)
* [stardist](https://github.com/stardist/stardist)
* [n2v](https://github.com/juglab/n2v)
* [cellpose](https://github.com/MouseLand/cellpose)
* [seaborn](https://seaborn.pydata.org/)

## See also

### Former lectures and related materials

Last year's lecture at Uni Leipzig
* [Bio Image Data Science](https://github.com/ScaDS/BIDS-lecture-2024)

A lecture covering similar contents was held in the past years at TU Dresden:
* [Bio-image Analysis, programming, bio-statistics and machine learning 2023](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/tree/51aabbeb269c9ad1a88fdef1ff9ff9cb69bf93e0)
* [Bio-image Analysis, programming, bio-statistics and machine learning 2022](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/tree/035bb75d90444f14ef21876bf3fdf9e53417f87b)
* [Bio-image Analysis, programming, bio-statistics and machine learning 2021](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/tree/a62070dee408814cee4258758f5187f135774519)
* [Bio-image Analysis, programming, bio-statistics and machine learning 2020](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [Bio-image Analysis, ImageJ Macro programming 2019](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis)
* [Bio-image Analysis Notebooks](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/)

### Image Analysis
* [Introduction to Bioimage Analysis](https://bioimagebook.github.io/)
* [Basics of Image Processing and Analysis by Kota Miura](https://github.com/miura/ij_textbook1/raw/76b51338e1f006c580b6f0f5cfc48fe02fba38d7/CMCIBasicCourse201102Bib.pdf)
* [Classic ImageJ training resources](https://imagej.nih.gov/ij/docs/examples/index.html)
* [Bioimage Data Analysis Workflows edited by Kota Miura and Nataša Sladoje](https://link.springer.com/book/10.1007%2F978-3-030-22386-1)

### Python
* [Python cheat sheet](https://github.com/gto76/python-cheatsheet)
* [Python/Conda environments](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments)
* [Scientific data analyis in Python, Biotec lecture](https://youtu.be/MOEPe9TGBK0)
* [Python for Microscopists, video series by Sreeni](https://www.youtube.com/channel/UC34rW-HtPJulxr5wp2Xa04w)
* [Managing Conda environments, online documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Bio-image Analysis using Scikit-Image in Python, Biotec lecture](https://youtu.be/FnvgepHDqRA)
* [Python for Bio-image Analysis by the Image Analysis Focused Interest Group of the Royal Microscopical Society](https://github.com/IAFIG-RMS/Python-for-Bioimage-Analysis)
* [Interactive Bioimage Analysis with Python and Jupyter, NEUBIAS academy webinar](https://youtu.be/2KF8vBrp3Zw), [Part 2](https://youtu.be/Y3pB3wnOivE)
* [Multi-dimensional image visualization in Python using napari, NEUBIAS Academy webinar](https://youtu.be/VgvDSq5aCDQ)

## Contributing
Contributions to this repository are welcome! If you see typos, bugs or have general feedback, please create a [github issue](https://github.com/ScaDS/BIDS-lecture-2024/issues) to let us know. 
If you would like to add additional lessons or want to suggest improvements to existing ones, [pull-requests](https://github.com/ScaDS/BIDS-lecture-2024/pulls) are very welcome!

## Acknowledgements
Deepest thanks goes to people who shared their training materials, preprints, figures and example data openly which became part of the materials used in this lecture series: Marcelo Leomil Zoccoler, Till Korten, Johannes Soltwedel, Daniela Vorkel, Laura Žigutytė, Ryan Savill, Mara Lampert, Lena Maier-Hein, Annika Reinke, Martin Schätz, Douglas G. Altman, J. Martin Bland, Constantin Pape, Benedict Diederich, Jennifer Waters, Tony Collins, Mike Kayser, Mauricio Rocha Martins, Kota Miura, Anna Pascual-Reguant, Peter Bankhead, Sreenivas Bhattiprolu, Henning Falk, Carsen Stringer, Marius Pachitariu, Alexander Krull, Uwe Schmidt, Martin Weigert, Dominic Waithe, Alex Bird, Dan White, Nasreddin Abolmaali, Alba Villaronga Luque, Jesse Veenvliet, Greg Kamradt, Josh Moore, Matthias Täschner, Ricardo Henriques, Anwai Archit, Jay Alammar, Loic A. Royer, Pranab Sahoo, Timo Kaufmann, Patrick Lewis, Noah Shinn, Xuezhi Wang, Jianing Wang, Jason Wei, Cheng Li, Yihe Deng, Robin Rombach, Aditya Ramesh, Akash Ghosh, Aditya Ramesh, Alec Radford, Alexey Dosovitskiy, Haotian Liu, Alexandr Khrapichev, Zishan Guo, Stephanie Lin, Mark Chen, Carlos E. Jimenez, Yuhang Lai, et al.


Some of the materials in this repository originate from the [BioImageAnalysis Notebooks](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html), were written by Robert Haase et al and were licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig“, project identification number: ScaDS.AI

[Imprint](https://www.uni-leipzig.de/impressum)
