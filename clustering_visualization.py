# this code is meant to facilitate visualization after applying clustering to a pandas data frame
# before using this code, make sure that the clusters are in the last column of your pandas data frame

df_for_visualization = many_songs_df.copy()

number_fig_columns = 2 # arbitrarily chosen

number_fig_rows = (df_for_visualization.shape[1] - 2) / number_fig_columns # -2 comes because we do not want the clusters column or the feature depicted on the y axis

# modifying number of rows for the figure if the division above results in a non-whole number
if number_fig_rows % 1 != 0:
    number_fig_rows = ceil(number_fig_rows)  # ceil comes from the math library

# this serves as container for dictionaries containing the group of plots generated for each feature that is depicted on the y axis
plot_holder = {}

for name_1 in df_for_visualization.columns[range(0, df_for_visualization.shape[1]-1)]:

    fig, axes = plt.subplots(int(number_fig_rows), number_fig_columns, figsize=(20, 18))
    
    plot_holder["plots_" + str(name_1)] = {}

    x = 0

    y = 0

    iter_no =0
    
    for name_2 in [name for name in df_for_visualization.columns if name not in [name_1, df_for_visualization.columns[-1]]]:

            if iter_no == 0:
                plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)] = sns.scatterplot(data = df_for_visualization, y = name_1, x = name_2, hue = df_for_visualization.columns[-1], palette='bright', s = 5, ax = axes[x, y])
                sns.move_legend(plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)], "upper left", bbox_to_anchor=(1, 1))       
                x = 0
                y = 1
                iter_no = 1
                
            elif iter_no % 2 != 0:
                plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)] = sns.scatterplot(data = df_for_visualization, y = name_1, x = name_2, hue = df_for_visualization.columns[-1], palette='bright', s = 5, ax = axes[x, y])
                sns.move_legend(plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)], "upper left", bbox_to_anchor=(1, 1))       
                x += 1
                y = 0
                iter_no += 1

            elif iter_no % 2 == 0:
                plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)] = sns.scatterplot(data = df_for_visualization, y = name_1, x = name_2, hue = df_for_visualization.columns[-1], palette='bright', s = 5, ax = axes[x, y])
                sns.move_legend(plot_holder["plots_" + str(name_1)]["subplot_" + str(name_2)], "upper left", bbox_to_anchor=(1, 1))       
                y = 1
                iter_no += 1
    
    plt.subplots_adjust(hspace=0.5, wspace=0.3) 
    plt.show()    
    #plt.savefig(f"plots_{str(name_1)}.pdf", dpi=300, bbox_inches='tight')
    plt.close()
