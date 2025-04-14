# FastReID Demo

We provide a command line tool to run a simple demo of builtin models.

You can run this command to get cosine similarites between different images

```bash
python demo/visualize_result.py --config-file logs/dukemtmc/mgn_R50-ibn/config.yaml \
--parallel --vis-label --dataset-name DukeMTMC --output logs/mgn_duke_vis \
--opts MODEL.WEIGHTS logs/dukemtmc/mgn_R50-ibn/model_final.pth
```

重みとデータセットがないと実行できない
```bash
python demo/visualize_result.py --config-file logs/market1501/bagtroot@hma43:/sabo_ws/src/fast-reid# python demo/visualize_result.py --config-file logs/market1501/bagtricks_R50/config.yaml --parallel --vis-label --dataset-name Market1501 --output logs/ --opts MODEL.WEIGHTS logs/market1501/bagtricks_R50/model_best.pth 
```


docker cp 9dca8281a772:/sabo_ws/src/fast-reid/logs/ logs/

```bash
python demo/demo.py --config-file logs/market1501/bagtricks_R50/config.yaml --parallel --input datasets/Market-1501-v15.09.15/bounding_box_test/0511_c5s1_140795_01.jpg --output logs/ --opts MODEL.WEIGHTS logs/market1501/bagtricks_R50/model_best.pth 
```