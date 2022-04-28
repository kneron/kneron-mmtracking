# Kneron AI Training/Deployment Platform (mmTracking-based)


## Introduction

  [kneron-mmtracking](https://github.com/kneron/kneron-mmtracking) is a platform built upon the well-known [mmtracking](https://github.com/open-mmlab/mmtracking) for tracking. We encourage you to start with [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](docs_kneron/bytetrack_step_by_step.md) to build basic knowledge of Kneron-Edition mmtracking, and read [mmtracking docs](https://mmtracking.readthedocs.io/en/latest/) for detailed mmtracking usage.

  In this repository, we provide an end-to-end training/deployment flow to realize on Kneron's AI accelerators: 

  1. **Training/Evalulation:**
      - Modified model configuration file and verified for Kneron hardware platform 
      - Please see [Overview of Benchmark and Model Zoo](#Overview-of-Benchmark-and-Model-Zoo) for Kneron-Verified model list
  2. **Converting to ONNX:** 
      - pytorch2onnx_kneron.py (beta)
      - Export *optimized* and *Kneron-toolchain supported* onnx
          - Automatically modify model for arbitrary data normalization preprocess
  3. **Evaluation**
      - test_kneron.py (beta)
      - Evaluate the model with *pytorch checkpoint, onnx, and kneron-nef*
  4. **Testing**
      - inference_kn (beta)
      - Verify the converted [NEF](http://doc.kneron.com/docs/#toolchain/manual/#5-nef-workflow) model on Kneron USB accelerator with this API
  5. **Converting Kneron-NEF:** (toolchain feature)
     - Convert the trained pytorch model to [Kneron-NEF](http://doc.kneron.com/docs/#toolchain/manual/#5-nef-workflow) model, which could be used on Kneron hardware platform.

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Changelog
N/A

## Overview of Benchmark and Kneron Model Zoo
| Model | size   | Mem (GB) |   box AP | Config | Download |
|:---------:|:-------:|:-------:|:-------:|:--------:|:------:|
| ByteTrack(YOLOX-s) | (448, 800) |   7.6      |   82.4  | [config](http://59.125.118.185:8088/eric_wu/mmtracking/-/blob/bytetrack_leaky/configs/mot/bytetrack/bytetrack_yolox_s_crowdhuman_mot17-private-half_kn-train.py)       |[model](https://github.com/kneron/Model_Zoo/blob/main/mmtracking/ByteTrack/latest.zip)



## Installation
- Please refer to [ByteTrack: Multi-Object Tracking by Associating Every Detection Box, Step 0. Environment](docs_kneron/bytetrack_step_by_step.md) for installation.
- Please refer to [Kneron PLUS - Python: Installation](http://doc.kneron.com/docs/#plus_python/introduction/install_dependency/) for the environment setup for Kneron USB accelerator.

## Getting Started
### Tutorial - Kneron Edition
- [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](docs_kneron/bytetrack_step_by_step.md): A tutorial for users to get started easily. To see detailed documents, please see below.

### Documents - Kneron Edition
- [Kneron ONNX Export] (under development)
- [Kneron Inference] (under development)
- [Kneron Toolchain Step-By-Step (YOLOv3)](http://doc.kneron.com/docs/#toolchain/yolo_example/)
- [Kneron Toolchain Manual](http://doc.kneron.com/docs/#toolchain/manual/#0-overview)

### Original mmtracking Documents
- [Original mmtracking getting started](https://github.com/open-mmlab/mmtracking#getting-started): It is recommended to read the original mmtracking getting started documents for other mmtracking operations.
- [Original mmtracking readthedoc](https://mmtracking.readthedocs.io/en/latest/): Original mmtracking documents.

## Contributing
[kneron-mmtracking](https://github.com/kneron/kneron-mmtracking) a platform built upon [OpenMMLab-mmtracking](https://github.com/open-mmlab/mmtracking)

- For issues regarding to the original [mmtracking](https://github.com/open-mmlab/mmtracking):
We appreciate all contributions to improve [OpenMMLab-mmtracking](https://github.com/open-mmlab/mmtracking). Ongoing projects can be found in out [GitHub Projects](https://github.com/open-mmlab/mmtracking/projects). Welcome community users to participate in these projects. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.

- For issues regarding to this repository [kneron-mmtracking](https://github.com/kneron/kneron-mmtracking): Welcome to leave the comment or submit pull requests here to improve kneron-mmtracking


## Related Projects
- kneron-mmdetection: Kneron training/deployment platform on [OpenMMLab - mmDetection](https://github.com/open-mmlab/kneron-mmdetection) detection toolbox
- kneron-mmsegmentation: Kneron training/deployment platform on [OpenMMLab - mmSegmentation](https://github.com/open-mmlab/kneron-mmsegmentation) semantic segmentation toolbox
