# model settings
img_scale = (640, 640)

model = dict(
    detector=dict(
        type='YOLOX',
        input_size=img_scale,
        random_size_range=(15, 25),
        random_size_interval=10,
        backbone=dict(
            type='CSPDarknet', 
            act_cfg=dict(type='LeakyReLU', negative_slope=0.1),
            deepen_factor=0.33, widen_factor=0.5),
        neck=dict(
            type='YOLOXPAFPN',
            in_channels=[128, 256, 512],
            out_channels=128,
            act_cfg=dict(type='LeakyReLU', negative_slope=0.1),
            num_csp_blocks=1),
        bbox_head=dict(
            type='YOLOXHead',
            num_classes=80,
            act_cfg=dict(type='LeakyReLU', negative_slope=0.1),
            in_channels=128, feat_channels=128),
        train_cfg=dict(
            assigner=dict(type='SimOTAAssigner', center_radius=2.5)),
        test_cfg=dict(
            score_thr=0.01, nms=dict(type='nms', iou_threshold=0.65))))
