"""
A library of functions for analyzing the output of the CF analysis pipeline.
"""

from .read_data import read_taxonomy, read_metadata, corrections, read_subsystems, sorted_presence_absence, read_the_data
from .metadata_data import metadata_definitions
from .clean_data import compatible_columns, categories_to_numeric, remove_highly_correlated_data
from .pathogens import BacterialPathogens
from .random_forests import random_forest_classifier, random_forest_regression, gb_classifier, gb_regressor, gb_classifier_model, gb_regressor_model
from .plot_figures import plot_pca, plot_feature_importance, plot_feature_abundance, plot_top_features
from .plot_figures import plot_abundance_stripplot, create_custom_labels, plot_one_top_feature
from .export_to_docx import pd2docx

__all__ = ['read_taxonomy', 'read_metadata', 'corrections', 'read_subsystems',
           'sorted_presence_absence', 'compatible_columns', 'categories_to_numeric', 'remove_highly_correlated_data',
           'metadata_definitions', 'read_the_data',
           'BacterialPathogens',
           'random_forest_classifier', 'random_forest_regression', 'gb_classifier', 'gb_regressor', 'plot_top_features',
           'gb_classifier_model', 'gb_regressor_model',
           'plot_pca', 'plot_feature_importance', 'plot_feature_abundance', 'plot_top_features', 'plot_abundance_stripplot',
           'plot_one_top_feature',
           'pd2docx', 'create_custom_labels'
        ]
