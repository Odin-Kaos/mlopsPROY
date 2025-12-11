# test_prediction.py
import pytest
import torch
from Lab1.mylib.model import predict, rescale


@pytest.fixture
def sample_tensor():
    # Create a simple 3x3 image with 3 channels (RGB)
    return torch.ones((3, 3, 3))


def test_predict_returns_valid_class(sample_tensor):
    result = predict(sample_tensor)
    assert result in ["cat", "dog", "pikachu"]


def test_rescale_changes_size(sample_tensor):
    resized = rescale(sample_tensor, 10)
    # After rescaling, tensor should have shape [C, H, W] = [3, 10, 10]
    assert resized.shape == (3, 10, 10)


def test_rescale_batch_dimension():
    # Create a batch of 2 images, each 3x5x5
    batch = torch.ones((2, 3, 5, 5))
    resized = rescale(batch, 8)
    # Should remain a batch of 2, resized to 8x8
    assert resized.shape == (2, 3, 8, 8)
