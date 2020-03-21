# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Helper methods for testing purpose"""


def build_template_model_dict_data(sample_index=0):
    """
    :param int sample_index: the index of the sample.
    :return dict: a sample data for Template model
    """
    return dict(
        full_name='test template model {}'.format(sample_index)
    )
