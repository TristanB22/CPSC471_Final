

lat = '''
\\begin{figure}[htbp]
    \\centering
    \\begin{subfigure}{.33\\textwidth}
        \\centering
        \\includegraphics[width=\\linewidth]{full_plt_coeff_N_1_NUM_node.png}
        \\caption{}
        \\label{fig:FIG_1}
    \\end{subfigure}%
    \\begin{subfigure}{.33\\textwidth}
        \\centering
        \\includegraphics[width=\\linewidth]{full_plt_coeff_N_2_NUM_node.png}
        \\caption{}
        \\label{fig:FIG_2}
    \\end{subfigure}%
    \\begin{subfigure}{.33\\textwidth}
        \\centering
        \\includegraphics[width=\\linewidth]{full_plt_coeff_N_3_NUM_node.png}
        \\caption{}
        \\label{fig:FIG_3}
    \\end{subfigure}%
    \\caption{Full Input Regression Coefficients for Augmented Neurons N_1_NUM, N_2_NUM, and N_3_NUM}
\\end{figure}
'''

for i in range(0, 11):

	t_l = lat.replace('N_1_NUM', str(i * 3 ))
	t_l = t_l.replace('N_2_NUM', str(i * 3  + 1))
	t_l = t_l.replace('N_3_NUM', str(i * 3  + 2))
	t_l = t_l.replace('FIG_1', f'full_neuron_{i * 3 }')
	t_l = t_l.replace('FIG_2', f'full_neuron_{i * 3 +1}')
	t_l = t_l.replace('FIG_3', f'full_neuron_{i * 3 +2}')

	print(t_l)

