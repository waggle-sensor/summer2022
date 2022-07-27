#!/usr/bin/env python

from training_utility import optimize

import tensorflow as tf
gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

n_trials=20
optimize("2022 summer argonne/jupyter/!data/pre-loaded/04all_data_16in_4out/", n_steps_in=16, n_steps_out=4, n_trials=n_trials)
# optimize("2022 summer argonne/jupyter/!data/pre-loaded/03all_data_57*6in_57out/", n_steps_in=57*6, n_steps_out=57, n_trials=n_trials)


# Remember to configure the early stopping requirements and number of epochs. They may be set to epochs=1 for debugging
