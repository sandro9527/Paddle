#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..meta_optimizers import RecomputeOptimizer
from ..meta_optimizers import GradientMergeOptimizer
from ..meta_optimizers import GraphExecutionOptimizer
from ..meta_optimizers import PipelineOptimizer
from ..meta_optimizers import LocalSGDOptimizer

__all__ = ["MetaOptimizerFactory"]

meta_optimizer_names = [
    "RecomputeOptimizer",
    "GradientMergeOptimizer",
    "GraphExecutionOptimizer",
    "PipelineOptimizer",
    "LocalSGDOptimizer",
]


class MetaOptimizerFactory(object):
    def __init__(self):
        pass

    def _get_valid_meta_optimizers(self, user_defined_optimizer):
        opt_list = []
        for opt_name in meta_optimizer_names:
            opt_list.append(globals()[opt_name](user_defined_optimizer))
        return opt_list
