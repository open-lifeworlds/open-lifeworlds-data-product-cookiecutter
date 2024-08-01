import os
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

import yaml
from dacite import from_dict
from lib.tracking_decorator import TrackingDecorator


@dataclass
class Metadata:
    name: str
    owner: str
    description: Optional[str]
    url: Optional[str]
    license: Optional[str]
    updated: Optional[date]
    schema: Optional[List[str]]


@dataclass
class Port:
    id: str
    metadata: Metadata
    files: Optional[List[str]]


@dataclass
class TransformationStep:
    name: str
    path: str
    description: Optional[str]


@dataclass
class Observability:
    quality: Optional[List[str]] = field(default_factory=list)
    operational: Optional[List[str]] = field(default_factory=list)
    slas: Optional[List[str]] = field(default_factory=list)
    security: Optional[List[str]] = field(default_factory=list)


@dataclass
class Term:
    name: str
    description: Optional[str]


@dataclass
class DataProductManifest:
    id: str
    metadata: Metadata
    input_ports: Optional[List[Port]] = field(default_factory=list)
    transformation_steps: Optional[List[TransformationStep]] = field(default_factory=list)
    output_ports: Optional[List[Port]] = field(default_factory=list)
    observability: Optional[Observability] = None
    consumers: Optional[List[str]] = field(default_factory=list)
    use_cases: Optional[List[str]] = field(default_factory=list)
    classification: Optional[str] = None
    ubiquitous_language: Optional[List[Term]] = field(default_factory=list)
    tags: Optional[List[str]] = field(default_factory=list)


@TrackingDecorator.track_time
def load_data_product_manifest(config_path) -> DataProductManifest:
    data_product_manifest_path = os.path.join(config_path, "data-product.yml")

    if os.path.exists(data_product_manifest_path):
        with open(data_product_manifest_path, "r") as file:
            data = yaml.safe_load(file)
        return from_dict(data_class=DataProductManifest, data=data)
    else:
        print(f"✗️ Config file {data_product_manifest_path} does not exist")
