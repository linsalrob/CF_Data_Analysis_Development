"""
Plot a PCA and a read abundance plot for the interesting clusters
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.metrics import mean_squared_error, roc_curve, auc

from itertools import cycle
from sklearn.decomposition import PCA
from adjustText import adjust_text

__author__ = 'Rob Edwards'


def plot_feature_importance(ax, feature_importances_sorted, title):
    # Create dotted lines and circles for each feature
    for feature in feature_importances_sorted.index[::-1]:
        importance = feature_importances_sorted.loc[feature, 'importance']
        ax.plot([importance], [feature], linestyle='dotted', marker='o', markersize=5, c='blue')
        ax.plot([0, importance], [feature, feature], linestyle='dotted', marker='None', markersize=5, c='lightblue')

    ax.set_xlabel("Importance")
    ax.set_ylabel("")
    ax.set_title(title)


def plot_feature_abundance(ax, feature_df, intcol, title):
    """
    Plot the top n important features.

    use something like this:
    top20 = list(feature_importances_sorted[:20].index)+[intcol]
    plot_feature_abundance(ax, merged_df[top20], intcol, f"Plot of normalised measures that are important to distinguish '{intcol}' usage")
    """

    # before we plot the data we scale the data to make the mean 0 and the variance 1.
    # you can compare the values before and after by looking at merged_df[top20].max() and  scaled_df.max()
    # scaler = StandardScaler()
    scaler = MinMaxScaler()
    tmpdf = feature_df.drop(intcol, axis=1)
    scaled_df = pd.DataFrame(scaler.fit_transform(tmpdf), columns=tmpdf.columns)
    scaled_df[intcol] = feature_df[intcol].values

    melted_df = pd.melt(scaled_df, id_vars=[intcol], var_name='Feature', value_name='Value')

    sns.boxplot(data=melted_df, x='Value', y='Feature', hue=intcol, fill=False, legend=False, color='k', fliersize=0,
                ax=ax)
    sns.stripplot(data=melted_df, x='Value', y='Feature', hue=intcol, jitter=True, alpha=0.5, dodge=True, ax=ax)

    ax.set_title(title)
    ax.set_xlabel('Normalised Abundance')
    ax.set_ylabel('')


def plot_top_features(merged_df, top_features, top_feature_counts, intcol, intcol_title, custom_labels=None):
    sorted_top_feats = sorted(top_features, key=lambda x: top_features[x], reverse=True)
    for x in sorted_top_feats[:10]:
        print(f"{x}: {top_features[x] / 5:.4f} ({top_feature_counts[x]} times)")

    n = 20
    tfdf = pd.DataFrame.from_dict(top_features, orient="index", columns=["importance"]).sort_values(by='importance',
                                                                                                    ascending=False)
    topN = list(tfdf[:n].index) + [intcol]
    fig, axes = plt.subplots(figsize=(10, 6), nrows=1, ncols=2, sharey='row', sharex='col')
    plot_feature_importance(axes[0], tfdf[:n][::-1], "")
    plot_feature_abundance(axes[1], merged_df[topN][::-1], intcol, intcol_title)

    if not custom_labels:
        custom_labels = {0: 'No', 1: 'Yes'}

    handles, labels = axes[1].get_legend_handles_labels()  # Get one set of handles and labels
    updated_labels = [custom_labels[float(label)] for label in labels]

    for ax in axes.flat:
        if ax.get_legend() is not None:  # Check if legend exists
            ax.get_legend().remove()

    plt.xticks(rotation=90)
    fig.legend(handles, updated_labels, loc='upper center', ncol=2, title=intcol_title)
    plt.tight_layout(rect=[0, 0, 1, 0.9])
    plt.show()

def plot_one_top_feature(merged_df, tfdf, intcol, intcol_title, custom_labels=None, savepng=None, plot_legend=True):

    n = 20
    topN = list(tfdf[:n].index) + [intcol]
    fig, axes = plt.subplots(figsize=(10, 6), nrows=1, ncols=2, sharey='row', sharex='col')
    plot_feature_importance(axes[0], tfdf[:n][::-1], "")
    plot_feature_abundance(axes[1], merged_df[topN][::-1], intcol, intcol_title)

    if not custom_labels:
        custom_labels = {0: 'No', 1: 'Yes'}

    handles, labels = axes[1].get_legend_handles_labels()  # Get one set of handles and labels
    updated_labels = [custom_labels[float(label)] for label in labels]

    for ax in axes.flat:
        if ax.get_legend() is not None:  # Check if legend exists
            ax.get_legend().remove()

    plt.xticks(rotation=90)
    if plot_legend:
        fig.legend(handles, updated_labels, loc='upper center', ncol=2, title=intcol_title)
    plt.tight_layout(rect=[0, 0, 1, 0.9])
    if savepng:
        plt.savefig(savepng)
    plt.show()


def plot_pca(ax, df, metadata, cluster_assignments, interesting_cluster, intcol):
    pca = PCA(n_components=2)

    df_clust = df[cluster_assignments.loc[cluster_assignments["Cluster"] == interesting_cluster, "Feature"]]
    merged_df_clust = df_clust.join(metadata[[intcol]])

    pca_result = pca.fit_transform(df_clust)
    pca_df = pd.DataFrame(data=pca_result, index=df.index, columns=['PC1', 'PC2'])

    # Get loadings
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    loadings_df = pd.DataFrame(loadings, index=df_clust.columns, columns=['PC1', 'PC2'])

    # Create a DataFrame for top loadings
    top_loadings_df = loadings_df.loc[loadings_df['PC1'].abs().sort_values(ascending=False).index]
    top_loadings_df.head()

    explained_variance = pca.explained_variance_ratio_ * 100
    pc1_variance = explained_variance[0]
    pc2_variance = explained_variance[1]

    sns.scatterplot(data=pca_df, x='PC1', y='PC2', alpha=0.2, ax=ax)
    ax.set_title(f"Cluster {interesting_cluster}")
    ax.set_xlabel(f'Principal Component 1 ({pc1_variance:.3f}%)')
    ax.set_ylabel(f'Principal Component 2 ({pc2_variance:.3f}%)')

    # add the loadings ... we only plot maxloadings here
    maxloadings = 5
    if len(loadings) < maxloadings:
        maxloadings = len(loadings)

    plotscaler = 2
    texts = []
    colour_cycle = cycle(mcolors.TABLEAU_COLORS)
    found_pseudomonas = False
    for i in range(maxloadings):
        c = next(colour_cycle)
        xpos = top_loadings_df.iloc[i, 0] * plotscaler
        ypos = top_loadings_df.iloc[i, 1] * plotscaler
        ax.arrow(0, 0, xpos, ypos,
                 color=c, alpha=0.5, width=0.05)
        loading_text = top_loadings_df.index[i]
        if len(loading_text) > 15:
            loading_text = loading_text[:15] + "..."
        texts.append(ax.text(xpos, ypos, loading_text, color=c))

    adjust_text(texts, ax=ax)


def plot_abundance_stripplot(ax, df, metadata, cluster_assignments, interesting_cluster, intcol):
    df_clust = df[cluster_assignments.loc[cluster_assignments["Cluster"] == interesting_cluster, "Feature"]]
    merged_df_clust = df_clust.join(metadata[[intcol]])
    df_clust_m = merged_df_clust.melt(id_vars=intcol, var_name='Features', value_name='Normalised read abundance')
    sns.stripplot(data=df_clust_m, x='Features', y='Normalised read abundance',
                  hue=intcol, dodge=True, jitter=True, ax=ax)
    ax.tick_params(axis='x', rotation=45)
    for label in ax.get_xticklabels():
        label.set_horizontalalignment('right')
    ax.set_title(f"Read abundance for {intcol} cluster {interesting_cluster}")


def create_custom_labels(metadata, intcol, merged_df, custom_labels=None):
    # do we need to encode this column
    categorical_data = False
    if custom_labels is None:
        custom_labels = {0: 'No', 1: 'Yes'}
    if intcol not in metadata.columns:
        return False, custom_labels
    if pd.api.types.is_numeric_dtype(metadata[intcol]):
        # this is an numeric column, so we can just continue
        categorical_data = False
    elif isinstance(metadata[intcol].dtype, pd.CategoricalDtype) and pd.api.types.is_numeric_dtype(
            metadata[intcol].cat.categories.dtype):
        # this is a categorical column with numeric categories so we can also continue
        categorical_data = True
    elif isinstance(merged_df[intcol].dtype, pd.CategoricalDtype):
        # this is a categorical column with string categories so we need to encode it
        enc = OrdinalEncoder()
        metadata_encoder = enc.fit(merged_df[[intcol]])
        categories = metadata_encoder.categories_[0]
        custom_labels = {code: cat for code, cat in enumerate(categories)}
        merged_df[intcol] = metadata_encoder.transform(merged_df[[intcol]])
        categorical_data = True
    else:
        # we don't know what this is, so we skip it for now
        print(f"Skipping {intcol} as it is not numeric or categorical")
        return None, None

    if len(metadata[intcol].unique()) != len(custom_labels.keys()):
        custom_labels = {x:x for x in metadata[intcol].unique()}
    return categorical_data, custom_labels


def old_plot_roc_curves(model, X, y, importances, met='classifier', intcol_title=""):
    """
    Plot the ROC curves for the model
    :param model: The machine learning model, hopefully a classifier
    :param X: The merged dataframe, X = merged_df.drop(intcol, axis=1)
    :param y: The truth, y = merged_df[intcol]
    :param importances: The feature importances, feature_importances_sorted
    :param met: classifier or regressor
    :param intcol_title: the display title of the interesting column
    :return: A matplotlib plot
    """

    plt.figure()

    y_proba = model.predict_proba(X)[:, 1]

    fpr, tpr, thresholds = roc_curve(y, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, lw=2, label=f'Overall {met} (all data)\n(area = {roc_auc:.2f})')

    n = 5
    for clust in importances[:n].index:
        y_scores = X[clust]

        # Compute ROC curve and AUC
        fpr, tpr, thresholds = roc_curve(y, y_scores)
        roc_auc = auc(fpr, tpr)
        if roc_auc < 0.5:
            y_scores = -y_scores
            fpr, tpr, thresholds = roc_curve(y, y_scores)
            roc_auc = auc(fpr, tpr)

        plt.plot(fpr, tpr, lw=1, label=f'{clust} (area = {roc_auc:.2f})', linestyle='-.')

    plt.plot([0, 1], [0, 1], color='grey', lw=0.5, linestyle='--', alpha=0.5)
    plt.xlabel('False Positive Rate')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.ylabel('True Positive Rate')
    plt.title(f'Predicting {intcol_title}')
    plt.legend(loc="lower right")
    return plt

def plot_roc_curves(model, X, y, importances, met='classifier', intcol_title="", ax=None, cmap='mako', verbose=False):
    """
    Plot the ROC curves for the model
    :param model: The machine learning model, hopefully a classifier
    :param X: The merged dataframe, X = merged_df.drop(intcol, axis=1)
    :param y: The truth, y = merged_df[intcol]
    :param importances: The feature importances, feature_importances_sorted
    :param met: classifier or regressor. Note we don't use this parameter currently
    :param intcol_title: the display title of the interesting column
    :return: A matplotlib plot
    """

    if not ax:
       fig, ax = plt.subplots(figsize=(10, 8))

    y_proba = model.predict_proba(X)[:, 1]

    fpr, tpr, thresholds = roc_curve(y, y_proba)
    roc_auc = auc(fpr, tpr)

    ax.plot(fpr, tpr, lw=2, label=f'Overall\n(area = {roc_auc:.2f})')
    colors = sns.color_palette("mako", n_colors=5)

    n = 5
    for i, clust in enumerate(importances[:n].index):
        y_scores = X[clust]
        color = colors[i]

        # Compute ROC curve and AUC
        fpr, tpr, thresholds = roc_curve(y, y_scores)
        roc_auc = auc(fpr, tpr)
        if roc_auc < 0.5:
            y_scores = -y_scores
            fpr, tpr, thresholds = roc_curve(y, y_scores)
            roc_auc = auc(fpr, tpr)

        # ax.plot(fpr, tpr, lw=1, label=f'{clust} (area = {roc_auc:.2f})', color=color)
        ax.plot(fpr, tpr, lw=1, label=f'{clust} (area = {roc_auc:.2f})', linestyle='-.', color=color)
        if verbose:
            print(f"{clust} (area = {roc_auc:.2f})", file=sys.stderr)

    ax.plot([0, 1], [0, 1], color='grey', lw=0.5, linestyle='--', alpha=0.5)
    ax.set_xlabel('False Positive Rate')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_ylabel('True Positive Rate')
    ax.set_title(f'{intcol_title}')
    ax.legend(loc="lower right")
    return ax


def plot_importance_abundance_roc(merged_df, tfdf, intcol, intcol_title, model, custom_labels=None, savepng=None, plot_legend=True):
    
    n = 20
    topN = list(tfdf[:n].index) + [intcol]
    # create the figure
    fig, axes = plt.subplots(figsize=(10, 6), nrows=1, ncols=3)

    # Share the y-axis between the first two columns only
    axes[1].sharey(axes[0])
        
    plot_feature_importance(axes[0], tfdf[:n][::-1], "")
    plot_feature_abundance(axes[1], merged_df[topN][::-1], intcol, intcol_title)

    if not custom_labels:
        custom_labels = {0: 'No', 1: 'Yes'}

    handles, labels = axes[1].get_legend_handles_labels()  # Get one set of handles and labels
    updated_labels = [custom_labels[float(label)] for label in labels]

    # Hide redundant y-axis labels/ticks on the second column
    plt.setp(axes[1].get_yticklabels(), visible=False)
    axes[1].yaxis.label.set_visible(False)

    for ax in axes.flat:
        if ax.get_legend() is not None:  # Check if legend exists
            ax.get_legend().remove()

    plt.xticks(rotation=90)
    if plot_legend:
        fig.legend(handles, updated_labels, loc='upper center', ncol=2, title=intcol_title)

    X = merged_df.drop(intcol, axis=1)
    y = merged_df[intcol]

    ax = plot_roc_curves(model, X, y, tfdf, None, "", ax=axes[2])
    legend = axes[2].get_legend()
    legend.set_bbox_to_anchor((0.4, 0))   # x=1.05 moves it to the right, y=1 aligns to top
    legend.set_loc('lower left')           # anchor the top-left corner of the legend box
    legend.set_frame_on(True)              # ensure the legend box is visible 
    legend.get_frame().set_facecolor('white') # white background
    legend.get_frame().set_edgecolor('black') # black border
    legend.get_frame().set_alpha(1.0)         # opaque

    plt.tight_layout(rect=[0, 0, 1, 0.9])

    return fig, axes
