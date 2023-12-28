from loosecontrol import LooseControlNet

FUSION_SCALE = 1.0
USE_CUDA = True
USE_HUGGINGFACE_WEIGHTS = True

if __name__ == "__main__":
    print(f"""
Fusing weights with configs:
    FUSION_SCALE: {FUSION_SCALE}
    USE_CUDA: {USE_CUDA}
    USE_HUGGINGFACE_WEIGHTS: {USE_HUGGINGFACE_WEIGHTS}

You can modify these in this script.
""")

    if USE_HUGGINGFACE_WEIGHTS:
        lcn = LooseControlNet("shariqfarooq/loose-control-3dbox")
    else:
        # Modify below to use your pre-downloaded weights
        lcn = LooseControlNet(loose_control_weights="..", cn_checkpoint="..", sd_checkpoint="..")

    if USE_CUDA:
        lcn = lcn.to("cuda")

    lcn.pipe.controlnet.fuse_lora(lora_scale=FUSION_SCALE)
    lcn.pipe.controlnet.save_pretrained("./fused_weights")
    print("Done! Saved to ./fused_weights")
