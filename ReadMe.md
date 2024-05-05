# CPSC 471 Final Project

### Project Overview

This directory contains all of the code that is used for the final project for CPSC471. In this project, I aim to set a new standard for model security, fairness, and explainability in sensitive environments such as insurance and criminal justice with a 3-step framework for augmenting current implementations:

1) Node Explainability: Using custom loss functions along with concept-based reasoning and training, I can guarantee that certain nodes in the machine learning model represent certain concepts that, when mapped with the corresponding output of the model, can shed light into why certain decisions are made in the model. Contrary to before where models were considered black-boxes, the integration of this idea-based semantic reasoning into the later layers of the model takes the idea of [TCAV](https://arxiv.org/abs/1711.11279) to the extreme. Instead of training a linear classifier to try to find instances which might represent a certain concept, the most salient concepts to the output are defined by the training pipeline and utilized to explain the output. 

2) Feature Importance Limiting: By incorporating a series of tests to understand how different nodes and features in a machine learning model interact with one another, I am able to adjust the weights in the models that I generate so that harmful or banned inputs to the model are not utilized. Instead, other weights feeding into that node with inputs are greedily selected and up- or down-weighted to attempt to mimic the action of the original node. This efficiently places the model into the state it would converge to anyways without the banned input – where the banned input is roughly approximated and backed out in the model – in substantially less time than before while removing the harmful variance that the banned feature brings (that which cannot be approximated with high fidelity).

3) Weight Freezing with Fidelity: Using a hashing mechanism with model encryption, we can guarantee that when the machine learning model has been trained and deployed by a trusted entity that signs it with their key and keeps track of the model hash, any attempts to change or re-train the model will result in the hash changing thereby showing to everyone that the weights have changed. By introducing this hashing mechanism, the model can be deployed remotely while decreasing the computation power that is required to verify that the model is safe from an entire evaluation of the model using something like min-perturbation and counterfactual analyses to a simple hash and API call to a central, trusted authority. One can think of this as the signing authority for machine learning models. 



### Directory Breakdown 

Within this repository, we have the following directories that have the following functions:

| Folder Name | Purpose |
| ------------- | ------ |
| `helper_code_and_checkpoints` | This directory contains helper functions and model checkpoints for executing the program and turning it into something that can be processed by LaTeX. |
| `final_471_datasets` | This directory contains the health insurance dataset in its entirety along with a shorter version of the criminal justice dataset. |
| `notebooks` | This contains all of the code that is necessary to actually run the method that I have devised. There is a description of each of the notebooks located in the directory. |
| `generated_images` | This contains all of the images that are important to save and not re-generate every time that the notebook is run. It includes things like 3D graphs which are not possible to save and must be turned into a png. |
| `References` | This contains the consulted and cited sources that are used to create this project. It is directly used to create the citations that are found in the final report in this repository. |
| `Example Models` | This contains example models for a single runthrough of the notebook. They are saved pytorch, XGBoost, and KMeans models. |

It is important to note that running the training process and explanation processes is extremely time- and computation-intensive, so please be wary of where the note books are run and respectful of resources. 

### Running the Project
In order to run the project, please navigate to `notebooks` and run either the `concept_focused_training.ipynb` or `importance_reduction.ipynb` notebooks. Description of these notebooks and their functions exists in the directory. 