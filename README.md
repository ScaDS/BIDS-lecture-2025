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

* [Microscopy Image Processing](02_Image_Processing.pdf") (April 25th 2025)
  * Image visualization
  * Image filtering
  * Morphological operations
  * Exercises:
    * [Images are just arrays of numbers](02a_image_processing/01_images_as_arrays.ipynb)
    * [Opening images and applying colormaps](02a_image_processing/02_opening_visualizing_images.ipynb)
    * [Opening and handling proprietary file formats](02a_image_processing/03_opening_images_using_aicsimageio.ipynb)
    * [Image windowing](02a_image_processing/04_Brightness_and_Contrast.ipynb)
    * [Cropping images](02a_image_processing/05_Cropping_images.ipynb)
    * [Inspecting 3D images](02a_image_processing/06_inspecting_3d_images.ipynb)
    * [Image processing filters](02a_image_processing/07_image_processing_filters.ipynb)
    * [Basic thresholding](02a_image_processing/08_basic_thresholding.ipynb)
    * [Morphological operations](02a_image_processing/09_binary_mask_refinement.ipynb)

* [Image Segmentation & Napari](03_Image_segmentation.pdf) (May 2nd 2025)
  * Image Segmentation
  * Label Morphological operations
  * [Interactive Image Processing using Napari](03b_napari_notebooks/napari_intro.ipynb)
  * [Image Processing pitfalls in Python](03a_image_segmentation/pitfals.ipynb)
  * Exercises:
    * [Gauss-Otsu-Labeling](03a_image_segmentation/09_gauss_otsu_labeling.ipynb)
    * [Voronoi-Otsu-Labeling](03a_image_segmentation/11_voronoi_otsu_labeling.ipynb)
    * [3D Image Segmentation](03a_image_segmentation/12_Segmentation_3D.ipynb)
    * [Watershed-algorithm](03a_image_segmentation/13_watershed.ipynb)
    * [Designing Image Processing workflows interactively](03b_napari_notebooks/napari-assistant.md)
    * [Auto-generating Jupyter Notebooks](03b_napari_notebooks/notebook_export.md)

* [Surface Reconstruction and feature extraction](04_Surface_Reconstruction_Feature_Extraction.pdf) (May 9th 2025)
  * Surface Reconstruction, mesh simplification, mesh smoothing
  * Feature Extraction, visualization
  * Exercises:
    * [Update your environment installation](04a_surface_reconstruction/readme.md)
    * [Creating surface meshes](04a_surface_reconstruction/creating_surfaces.ipynb)
    * [Visualizing surface meshes](04a_surface_reconstruction/visualizing_surfaces.ipynb)
    * [Feature extraction with scikit-image](04b_feature_extraction/01_feature_extraction_with_scikit_image.ipynb)
    * [Feature extraction with SimpleITK](04b_feature_extraction/03_feature_extraction_with_simpleitk.ipynb)
    * [Parametric Maps](04b_feature_extraction/05_parametric_maps.ipynb)
    * [Interactive Plots](04b_feature_extraction/06_interactive_plots.ipynb)
    
* [GPU-Acceleration, Tiled image processing and Quality Assurance](05_GPUs_Tiles_QA.pdf) (May 16th 2025)
  * Grapics Processing Units for Image Analysis, OpenCL, Benchmarking
  * Processing images in tiles using zarr and dask
  * Measuring quality of segmentation results
  * Exercises:
    * [Benchmarking image processing filters using scikit-image, scipy, simple-itk and clesperanto](05a_gpu_acceleration/60_benchmark_gaussian.ipynb)
    * [Processing images in tiles with overlap](05b_tiled_image_processing/02_tiling_images_with_overlap.ipynb)
    * [Counting nuclei in tiles](05b_tiled_image_processing/04_tiled_nuclei_counting.ipynb)
    * [Measure quality of segmentation results](05c_quality_assurance/segmentation_quality_estimation.ipynb)
    * [Visual comparison of segmentation results](05c_quality_assurance/visual_comparison.ipynb)
   
* [Introduction to Machine Learning](06_Sup_Unsup_Machine_Learning.pdf) (May 23rd 2025)
  * Unsupervised ML
  * Supervised ML
  * Explainable ML
  * Exercises:
    * [Interactive parameter exploration](06a_hypothesis_generation/interactive_parameter_exploration.ipynb)
    * [Interactive Pixel Classification](06b_pixel_and_object_classification/interactive_pixel_classification/readme.md)
    * [Interactive Object Classification](06b_pixel_and_object_classification/interactive_object_classification/readme.md)
    * [Pixel classification using Scikit-Learn](06b_pixel_and_object_classification/01_scikit_learn_random_forest_pixel_classifier.ipynb)
    * [SHAP installation](06c_xai_shap/readme.md)
    * [Explaining Pixel Classification](06c_xai_shap/pixel_classifier.ipynb)
    * [Explaining Object Classification](06c_xai_shap/object_classification.ipynb)
    
 * [Deep Learning for Bio-image Analysis](07_Deep_Learning.pdf) (May 30th 2025)
   * Denoising
   * Segmentation
   * Exercises
     * [Noise2void](07a_dl_denoising/noise2void.ipynb)
     * [StarDist](07b_dl_segmentation/stardist.ipynb)
     * [CellPose](07b_dl_segmentation/cellpose.ipynb)
     * [Micro-SAM](07b_dl_segmentation/micro-sam.ipynb)
     * [CellPose-SAM](07b_dl_segmentation/cellpose-sam.ipynb)
     
* [Introduction to Large Language Models](08_LLMs_Intro.pdf) (June 6th 2025)
  * Intro to LLMs
  * Prompt Engineering
  * LLM service providers
  * Good Scientific Practice
  * Exercises
    * [Installation](08a_llm_endpoints/readme.md)
    * Endpoints (choose one): [ollama](08a_llm_endpoints/02_ollama_endpoint.ipynb), [blablador](08a_llm_endpoints/03_blablador_endpoint.ipynb), [kisski](08a_llm_endpoints/04_kisski_endpoint.ipynb), [github models](08a_llm_endpoints/05_github_models_endpoints.ipynb), [openrouter](08a_llm_endpoints/07_openrouter_endpoint.ipynb)
    * [Programming a Chatbot](08b_chatbot/gui.ipynb)
    * [LLMs guessing which image processing algorithm to use](08c_guess_library/guess_library.ipynb)

* [LLMs for code generation](09_Code_Generation.pdf) (June 20th 2025)
  * Prompt Engineering (continued)
  * Retrieval-augmented Generation
  * Function Calling
  * AI Agents
  * Exercises
    * [Extending Jupyter notebooks using AI](09a_code_generation/extending_jupyter_notebooks.ipynb)
    * [Long context prompting](09a_code_generation/long_context_prompting.ipynb)
    * [Text embeddings](09b_rag/10-text-embeddings.ipynb)
    * [RAG](09b_rag/20-simple-rag.ipynb)
    * [Function calling](09c_function_calling/10_function_calling.ipynb)


## Assignments

As explained in the lecture on May 9th, every enrolled student has to submit an image analysis workflow + documentation. The workflows are intended to process different datasets. Each student gets their own dataset. Download the zipfile corresponding to your MatNr and unzip it. The password was given to you in the lecture on May 9th.
[3795650](assignments/3795650.zip)
[3781296](assignments/3781296.zip)
[3799815](assignments/3799815.zip)
[3745356](assignments/3745356.zip)
[3711464](assignments/3711464.zip)
[3781088](assignments/3781088.zip)
[3782680](assignments/3782680.zip)
[3769826](assignments/3769826.zip)
[3790403](assignments/3790403.zip)
[3746612](assignments/3746612.zip)
[3787475](assignments/3787475.zip)
[3706879](assignments/3706879.zip)
[3792009](assignments/3792009.zip)
[3796977](assignments/3796977.zip)
[3796590](assignments/3796590.zip)
[3795611](assignments/3795611.zip)
[3795409](assignments/3795409.zip)
[3792423](assignments/3792423.zip)
[3771050](assignments/3771050.zip)
[2163012](assignments/2163012.zip)
[3777628](assignments/3777628.zip)
[3780527](assignments/3780527.zip)
[3765110](assignments/3765110.zip)
[3720384](assignments/3720384.zip)
[3781461](assignments/3781461.zip)
[3763803](assignments/3763803.zip)
[3795674](assignments/3795674.zip)
[3781887](assignments/3781887.zip)
[3733406](assignments/3733406.zip)
[3770023](assignments/3770023.zip)
[3750893](assignments/3750893.zip)
[3761687](assignments/3761687.zip)
[3784108](assignments/3784108.zip)

If you cannot find your MatNr in the list above, please reach out via Email. Also in case the dataset linked in the zip file is not available or not suitable, please reach out.


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
