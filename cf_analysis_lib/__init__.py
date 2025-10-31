"""
A library of functions for analyzing the output of the CF analysis pipeline.
"""

from .read_data import read_taxonomy, read_metadata, corrections, read_subsystems
from .read_data import sorted_presence_absence, read_the_data, read_mag_coverage
from .read_data import read_mag_metadata
from .metadata_data import metadata_definitions
from .clean_data import compatible_columns, categories_to_numeric, remove_highly_correlated_data
from .pathogens import BacterialPathogens
from .random_forests import random_forest_classifier, random_forest_regression, gb_classifier, gb_regressor, gb_classifier_model, gb_regressor_model
from .plot_figures import plot_pca, plot_feature_importance, plot_feature_abundance, plot_top_features
from .plot_figures import plot_abundance_stripplot, create_custom_labels, plot_one_top_feature, plot_roc_curves
from .plot_figures import plot_importance_abundance_roc
from .export_to_docx import pd2docx
from .worldwide_samples import worldwide_samples, read_worldwide_taxonomy, read_worldwide_subsystems, read_worldwide_metadata, read_worldwide_data
from .green_box import green_box, show_green
from .int_to_roman import int2roman

__all__ = ['read_taxonomy', 'read_metadata', 'corrections', 'read_subsystems',
           'sorted_presence_absence', 'compatible_columns', 'categories_to_numeric', 'remove_highly_correlated_data',
           'metadata_definitions', 'read_the_data', 'read_mag_coverage',
           'BacterialPathogens', 'read_mag_metadata',
           'random_forest_classifier', 'random_forest_regression', 'gb_classifier', 'gb_regressor', 'plot_top_features',
           'gb_classifier_model', 'gb_regressor_model',
           'plot_pca', 'plot_feature_importance', 'plot_feature_abundance', 'plot_top_features', 'plot_abundance_stripplot',
           'plot_one_top_feature', 'plot_roc_curves', 'plot_importance_abundance_roc',
           'pd2docx', 'create_custom_labels',
           'worldwide_samples', 'read_worldwide_taxonomy', 'read_worldwide_subsystems', 'read_worldwide_metadata', 'read_worldwide_data',
           'int2roman'
        ]
