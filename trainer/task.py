"""A simple main file to showcase the template."""

import argparse
import logging.config

from tensorflow.keras import datasets
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import activations
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from tensorflow.keras import utils


def _download_data():
    train, test = datasets.mnist.load_data()
    x_train, y_train = train
    x_test, y_test = test
    return x_train, y_train, x_test, y_test


def _preprocess_data(x, y):
    x = x / 255.0
    y = utils.to_categorical(y)
    return x,y


def _build_model():
    m = models.Sequential()

    m.add(layers.Input((28,28), name='my_input_layer'))
    m.add(layers.Flatten())
    m.add(layers.Dense(128, activation=activations.relu))
    m.add(layers.Dense(64, activation=activations.relu))
    m.add(layers.Dense(32, activation=activations.relu))
    m.add(layers.Dense(10, activation=activations.softmax))

    return m


def train_and_evaluate(batch_size, epochs, job_dir, output_path):

    # Download the data
    x_train, y_train, x_test, y_test = _download_data()

    # Preprocess the data
    x_train, y_train = _preprocess_data(x_train, y_train)
    x_test, y_test = _preprocess_data(x_test, y_test)

    # Build the model
    model = _build_model()

    # Train the model

    # Evaluate the model

    pass


def main():
    """Entry point for your module."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch-size', type=int, help='Batch size for the training')
    parser.add_argument('--epochs', type=int, help='Number of epochs for the training')
    parser.add_argument('--job-dir', default=None, required=False, help='Option for AI Platform')
    parser.add_argument('--model-output-path', help='Path to write the SaveModel format')

    args = parser.parse_args()

    batch_size = args.batch_size
    epochs = args.epochs
    job_dir = args.job_dir
    output_path = args.model_output_path

    train_and_evaluate(batch_size, epochs, job_dir, output_path)

if __name__ == "__main__":
    main()
    