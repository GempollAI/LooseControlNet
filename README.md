# LooseControlNet: Fused ControlNet Weights from LooseControl

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## How it works

In LooseControl, the authors trained a LoRA of `ControlNet-depth`, but now few libraries or frameworks support *LoRA of
ControlNet*, so they hacked through `ControlNetModel` of `diffusers` with `UNet2DConditionLoadersMixin`.

However, we can't run the code in frameworks like A1111's WebUI or ComfyUI, so we fused the weights
of `ControlNet-depth` and `LooseControl` to make it work in any frameworks. For details, please refer to [the script](./weight_fusion.py).

> *Important Note:*
> The authors of LooseControl did more than just training a LoRA. Let's not forget that. Please refer to the original paper and code for more
> details.

## Usage

Download the fused ControlNet weights from [huggingface](https://huggingface.co/AIRDGempoll/LooseControlNet) and used it
anywhere (e.g. A1111's WebUI or ComfyUI) you can use `ControlNet-depth` to loosely control image generation using depth
images.

[Example folder](./loose_controlnet_example) contains an simple workflow for using LooseControlNet in ComfyUI.

## Contributing

If you like it, you can contribute by:

* Upvote this [issue](https://github.com/huggingface/diffusers/issues/6354) in `diffusers` repo or possibly make a PR to
  resolve it.
* Bring consistency mechanisms devised in LooseControl to frameworks like A1111's WebUI or ComfyUI.
* Bring box editors to frameworks like A1111's WebUI or ComfyUI.
* Perhaps train a better LooseControlNet

## Licenses

The extra code we add is released under MIT License and the fused weights are released under Apache 2.0 License,
which follows the original license, MIT License, of LooseControl and Apache 2.0 License of ControlNet.

## References

### LooseControl

This is the official repository for LooseControl:
> #### [LooseControl: Lifting ControlNet for Generalized Depth Conditioning](#)
> ##### [Shariq Farooq Bhat](https://shariqfarooq123.github.io), [Niloy J. Mitra](http://www0.cs.ucl.ac.uk/staff/n.mitra/), [Peter Wonka](http://peterwonka.net/)
>

[[Project Page]](https://shariqfarooq123.github.io/loose-control/) [[Paper]](https://arxiv.org/abs/2312.03079) [[Demo 🤗]](https://huggingface.co/spaces/shariqfarooq/LooseControl) [[Weights (3D Box Control)]](https://huggingface.co/shariqfarooq/loose-control-3dbox)

![teaser](assets/looseControl_teaser.png)

#### Citation

```bibtex
@misc{bhat2023loosecontrol,
      title={LooseControl: Lifting ControlNet for Generalized Depth Conditioning}, 
      author={Shariq Farooq Bhat and Niloy J. Mitra and Peter Wonka},
      year={2023},
      eprint={2312.03079},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

### ControlNet

Please refer to its official [repository](https://github.com/lllyasviel/ControlNet) for more details.
