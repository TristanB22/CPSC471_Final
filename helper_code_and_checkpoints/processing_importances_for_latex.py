# this file processes the importance reduction output from the 
# influence reweighting code that I wrote before. 

import re

influence_output = '''
torch.Size([64, 10])
RESULTS FOR REMOVING FEATURE 0 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.6363 seconds on average for
avg_train_loss: 1.4848 (0.67%)
avg_val_loss: 1.5313 (1.90%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.1858 seconds on average for
avg_train_loss: 1.4973 (1.55%)
avg_val_loss: 1.5212 (1.23%)
importance: 0.0273 (-65.93%)

Removing influence with inversion_fine_tuning
Took 3.2662 seconds on average for
avg_train_loss: 1.4832 (0.56%)
avg_val_loss: 1.5035 (0.05%)
importance: 0.0620 (-22.73%)

Removing influence with simple_retraining
Took 16.9821 seconds on average for
avg_train_loss: 1.4954 (1.43%)
avg_val_loss: 1.5177 (0.99%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 1 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.5472 seconds on average for
avg_train_loss: 1.4847 (0.67%)
avg_val_loss: 1.5306 (1.85%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.1915 seconds on average for
avg_train_loss: 1.4979 (1.57%)
avg_val_loss: 1.5208 (1.20%)
importance: 0.0262 (-67.40%)

Removing influence with inversion_fine_tuning
Took 3.1951 seconds on average for
avg_train_loss: 1.4832 (0.59%)
avg_val_loss: 1.5049 (0.14%)
importance: 0.0627 (-21.84%)

Removing influence with simple_retraining
Took 17.5760 seconds on average for
avg_train_loss: 1.4966 (1.49%)
avg_val_loss: 1.5220 (1.28%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 2 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.8185 seconds on average for
avg_train_loss: 1.4851 (0.69%)
avg_val_loss: 1.5307 (1.86%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.1479 seconds on average for
avg_train_loss: 1.4984 (1.62%)
avg_val_loss: 1.5213 (1.23%)
importance: 0.0252 (-68.57%)

Removing influence with inversion_fine_tuning
Took 3.1382 seconds on average for
avg_train_loss: 1.4832 (0.59%)
avg_val_loss: 1.5043 (0.10%)
importance: 0.0614 (-23.48%)

Removing influence with simple_retraining
Took 17.0895 seconds on average for
avg_train_loss: 1.4962 (1.45%)
avg_val_loss: 1.5175 (0.98%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 3 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.3888 seconds on average for
avg_train_loss: 1.4854 (0.75%)
avg_val_loss: 1.5298 (1.80%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.1253 seconds on average for
avg_train_loss: 1.4978 (1.56%)
avg_val_loss: 1.5221 (1.28%)
importance: 0.0254 (-68.39%)

Removing influence with inversion_fine_tuning
Took 3.1620 seconds on average for
avg_train_loss: 1.4837 (0.61%)
avg_val_loss: 1.5036 (0.05%)
importance: 0.0597 (-25.63%)

Removing influence with simple_retraining
Took 17.1359 seconds on average for
avg_train_loss: 1.4985 (1.63%)
avg_val_loss: 1.5246 (1.45%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 4 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.4444 seconds on average for
avg_train_loss: 1.4843 (0.67%)
avg_val_loss: 1.5325 (1.98%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.0481 seconds on average for
avg_train_loss: 1.4977 (1.55%)
avg_val_loss: 1.5223 (1.30%)
importance: 0.0251 (-68.70%)

Removing influence with inversion_fine_tuning
Took 3.1684 seconds on average for
avg_train_loss: 1.4830 (0.54%)
avg_val_loss: 1.5042 (0.09%)
importance: 0.0611 (-23.88%)

Removing influence with simple_retraining
Took 17.3292 seconds on average for
avg_train_loss: 1.4959 (1.43%)
avg_val_loss: 1.5250 (1.48%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 5 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.5040 seconds on average for
avg_train_loss: 1.4849 (0.67%)
avg_val_loss: 1.5308 (1.86%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.1389 seconds on average for
avg_train_loss: 1.4977 (1.58%)
avg_val_loss: 1.5216 (1.25%)
importance: 0.0211 (-73.66%)

Removing influence with inversion_fine_tuning
Took 3.1627 seconds on average for
avg_train_loss: 1.4834 (0.58%)
avg_val_loss: 1.5042 (0.09%)
importance: 0.0604 (-24.75%)

Removing influence with simple_retraining
Took 16.8710 seconds on average for
avg_train_loss: 1.4946 (1.36%)
avg_val_loss: 1.5172 (0.96%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 6 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.4048 seconds on average for
avg_train_loss: 1.4851 (0.74%)
avg_val_loss: 1.5308 (1.87%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.0967 seconds on average for
avg_train_loss: 1.4977 (1.58%)
avg_val_loss: 1.5223 (1.30%)
importance: 0.0274 (-65.87%)

Removing influence with inversion_fine_tuning
Took 3.3292 seconds on average for
avg_train_loss: 1.4840 (0.61%)
avg_val_loss: 1.5037 (0.06%)
importance: 0.0616 (-23.23%)

Removing influence with simple_retraining
Took 16.6251 seconds on average for
avg_train_loss: 1.4935 (1.29%)
avg_val_loss: 1.5199 (1.14%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 7 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.5884 seconds on average for
avg_train_loss: 1.4848 (0.65%)
avg_val_loss: 1.5307 (1.86%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.0420 seconds on average for
avg_train_loss: 1.4976 (1.57%)
avg_val_loss: 1.5239 (1.41%)
importance: 0.0267 (-66.78%)

Removing influence with inversion_fine_tuning
Took 3.1158 seconds on average for
avg_train_loss: 1.4831 (0.55%)
avg_val_loss: 1.5057 (0.19%)
importance: 0.0619 (-22.88%)

Removing influence with simple_retraining
Took 16.7170 seconds on average for
avg_train_loss: 1.4968 (1.50%)
avg_val_loss: 1.5216 (1.25%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 8 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.3773 seconds on average for
avg_train_loss: 1.4839 (0.63%)
avg_val_loss: 1.5306 (1.85%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.0177 seconds on average for
avg_train_loss: 1.4977 (1.52%)
avg_val_loss: 1.5223 (1.30%)
importance: 0.0266 (-66.80%)

Removing influence with inversion_fine_tuning
Took 3.0815 seconds on average for
avg_train_loss: 1.4837 (0.61%)
avg_val_loss: 1.5041 (0.09%)
importance: 0.0651 (-18.94%)

Removing influence with simple_retraining
Took 16.6749 seconds on average for
avg_train_loss: 1.4957 (1.41%)
avg_val_loss: 1.5209 (1.21%)
importance: 0.0000 (-100.00%)


RESULTS FOR REMOVING FEATURE 9 INFLUENCE:
Removing influence with greedy_amplitude_correlation_adjustment
Took 3.4817 seconds on average for
avg_train_loss: 1.4849 (0.70%)
avg_val_loss: 1.5311 (1.88%)
importance: 0.0000 (-100.00%)

Removing influence with stochastic_fine_tuning
Took 3.2288 seconds on average for
avg_train_loss: 1.4975 (1.54%)
avg_val_loss: 1.5222 (1.29%)
importance: 0.0278 (-65.39%)

Removing influence with inversion_fine_tuning
Took 3.1503 seconds on average for
avg_train_loss: 1.4829 (0.59%)
avg_val_loss: 1.5036 (0.05%)
importance: 0.0627 (-21.85%)

Removing influence with simple_retraining
Took 16.5667 seconds on average for
avg_train_loss: 1.4950 (1.33%)
avg_val_loss: 1.5202 (1.16%)
importance: 0.0000 (-100.00%)

'''

latex_table_format = """
\\begin{table}[htbp]
\\centering
\\caption{Results for Removing Feature Influence by Different Methods}
\\begin{tabularx}{\\textwidth}{|c|X|X|X|X|}
\\hline
\\textbf{ } & \\textbf{Method} & \\textbf{Validation Loss} & \\textbf{Loss \% Change} & \\textbf{Importance Reduction \%} \\\\
\\hline
"""

# the pattern that we are looking for in the text
pattern = r"RESULTS FOR REMOVING FEATURE (\d+) INFLUENCE:(.*?)(?=\nRESULTS FOR REMOVING FEATURE|\Z)"

# sub pattern that we are looking for after the first pattern
method_pattern = r"Removing influence with (.*?)\nTook .*?\navg_train_loss: .*? \((.*?)%\)\navg_val_loss: (.*?) \((.*?)%\)\nimportance: .*? \((.*?)%\)"

# get the matches
matches = re.findall(pattern, influence_output, re.DOTALL)

# iterate through the matches
for f_num, f_dat in matches:
    
	# append the information
	latex_table_format += "\\multicolumn{5}{|c|}{Feature " + f_num + "} \\\\\n\\hline\n"

	# get the sub matches
	method_matches = re.findall(method_pattern, f_dat, re.DOTALL)

	# append the extra data
	for method in method_matches:

		# add the information that regex found
		method_name, _, val_loss, val_loss_change, importance_reduction = method

		method_name = method_name.replace("_", "\_")

		# to the latex output
		latex_table_format += "& {} & {} & {} & {} \\\\\n".format(method_name, val_loss, val_loss_change, importance_reduction)
	
	# add to the table
	latex_table_format += "\\hline\n"

# close the table
latex_table_format += """
\\end{tabularx}
\\end{table}
"""

# print the latex
print(latex_table_format)