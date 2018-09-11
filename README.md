<!--
{% comment %}
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to you under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
{% endcomment %}
-->

# Python WSI Preprocessing

This project contains a variety of files for investigating image preprocessing using Python
with the aim of using deep learning to perform histopathology image classification of
whole slide images.

See main tutorial [here](./docs/wsi-preprocessing-in-python/index.md).

See main project at [https://github.com/CODAIT/deep-histopath](https://github.com/CODAIT/deep-histopath)
for more information.

# Mingrui's customization

1. file naming convention is changed to 'filename-filenumber-*'

requirements:
jupyterlab `pip install jupyterlab`
matplotlib `pip install matplotlib`
PIL `pip install Pillow`
openslide `pip install openslide-python`
py_wsi: pull repo then `python setup.py install`
scipy: `pip install scipy`
scikit-image: `pip install scikit-image`
pandas: `pip install pandas`
