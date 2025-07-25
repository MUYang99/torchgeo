# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from pathlib import Path

import matplotlib.pyplot as plt
import pytest
import torch
import torch.nn as nn
from _pytest.fixtures import SubRequest
from pytest import MonkeyPatch

from torchgeo.datasets import LEVIRCD, DatasetNotFoundError, LEVIRCDPlus


class TestLEVIRCD:
    @pytest.fixture(params=['train', 'val', 'test'])
    def dataset(
        self, monkeypatch: MonkeyPatch, tmp_path: Path, request: SubRequest
    ) -> LEVIRCD:
        directory = os.path.join('tests', 'data', 'levircd', 'levircd')
        splits = {
            'train': {
                'url': os.path.join(directory, 'train.zip'),
                'filename': 'train.zip',
            },
            'val': {'url': os.path.join(directory, 'val.zip'), 'filename': 'val.zip'},
            'test': {
                'url': os.path.join(directory, 'test.zip'),
                'filename': 'test.zip',
            },
        }
        monkeypatch.setattr(LEVIRCD, 'splits', splits)
        root = tmp_path
        split = request.param
        transforms = nn.Identity()
        return LEVIRCD(root, split, transforms, download=True)

    def test_getitem(self, dataset: LEVIRCD) -> None:
        x = dataset[0]
        assert isinstance(x, dict)
        assert isinstance(x['image'], torch.Tensor)
        assert isinstance(x['mask'], torch.Tensor)
        assert x['image'].shape[1] == 3

    def test_len(self, dataset: LEVIRCD) -> None:
        assert len(dataset) == 2

    def test_already_downloaded(self, dataset: LEVIRCD) -> None:
        LEVIRCD(root=dataset.root, download=True)

    def test_invalid_split(self) -> None:
        with pytest.raises(AssertionError):
            LEVIRCD(split='foo')

    def test_not_downloaded(self, tmp_path: Path) -> None:
        with pytest.raises(DatasetNotFoundError, match='Dataset not found'):
            LEVIRCD(tmp_path)

    def test_plot(self, dataset: LEVIRCD) -> None:
        dataset.plot(dataset[0], suptitle='Test')
        plt.close()

        sample = dataset[0]
        sample['prediction'] = sample['mask'].clone()
        dataset.plot(sample, suptitle='Prediction')
        plt.close()


class TestLEVIRCDPlus:
    @pytest.fixture(params=['train', 'test'])
    def dataset(
        self, monkeypatch: MonkeyPatch, tmp_path: Path, request: SubRequest
    ) -> LEVIRCDPlus:
        url = os.path.join('tests', 'data', 'levircd', 'levircdplus', 'LEVIR-CD+.zip')
        monkeypatch.setattr(LEVIRCDPlus, 'url', url)
        root = tmp_path
        split = request.param
        transforms = nn.Identity()
        return LEVIRCDPlus(root, split, transforms, download=True)

    def test_getitem(self, dataset: LEVIRCDPlus) -> None:
        x = dataset[0]
        assert isinstance(x, dict)
        assert isinstance(x['image'], torch.Tensor)
        assert isinstance(x['mask'], torch.Tensor)
        assert x['image'].shape[1] == 3

    def test_len(self, dataset: LEVIRCDPlus) -> None:
        assert len(dataset) == 2

    def test_already_downloaded(self, dataset: LEVIRCDPlus) -> None:
        LEVIRCDPlus(root=dataset.root, download=True)

    def test_invalid_split(self) -> None:
        with pytest.raises(AssertionError):
            LEVIRCDPlus(split='foo')

    def test_not_downloaded(self, tmp_path: Path) -> None:
        with pytest.raises(DatasetNotFoundError, match='Dataset not found'):
            LEVIRCDPlus(tmp_path)

    def test_plot(self, dataset: LEVIRCDPlus) -> None:
        dataset.plot(dataset[0], suptitle='Test')
        plt.close()

        sample = dataset[0]
        sample['prediction'] = sample['mask'].clone()
        dataset.plot(sample, suptitle='Prediction')
        plt.close()
