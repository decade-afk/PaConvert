# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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
import textwrap

from apibase import APIBase

obj = APIBase("torch.argmin")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        result = torch.argmin(input)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        result = torch.argmin(input, dim = 1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        result = torch.argmin(input, dim = 1, keepdim=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        dim, keepdim = 1, True
        result = torch.argmin(input, dim, keepdim)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        dim, keepdim = 1, True
        result = torch.argmin(input=input, dim=dim, keepdim=keepdim)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1.3398, 0.2663, -0.2686, 0.2450],
                            [-0.7401, -0.8805, -0.3402, -1.1936],
                            [0.4907, -1.3948, -1.0691, -0.3132],
                            [-1.6092, 0.5419, -0.2993, 0.3195]])
        dim, keepdim = 1, True
        result = torch.argmin(dim=dim, input=input, keepdim=keepdim)
        """
    )
    obj.run(pytorch_code, ["result"])
