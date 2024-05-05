This directory contains all of the code that is required to run the explainability and importance reduction aspects of the framework proposed.


### Explainability
The `concept_focused_training.ipynb` has all of the code required to create an explainable machine learning model using either the criminal justice or health insurance dataset. In order to run the program, the user should configure the program options to reflect the version of the program that you would like to run. This includes options for the dataset that you would like to use, the hyperparameters of the model, and other optimizations.

In order to run the code with the criminal justice dataset, please go to download the sentencing data from the (Cook County Courts website)[https://datacatalog.cookcountyil.gov/Courts/Sentencing/tg8v-tm6u/data] and add the data to the `final_471_datasets` directory with the updated name of `short_sentencing.csv`. However, this dataset can take 48+ hours to run in the notebook so please do be careful with and respectful of computation resources.

The `importance_reduction-ipynb` notebook is self contained and can run once the required packages are installed on the machine that the code is being run on. 

Please be wary that the package list for required imports for the two programs is rather extensive.

Please make sure to adjust the directories to reflect your local machine. Additionally, the code is optimized for Mac so optimizations may be needed to run the notebook on other platforms. 



