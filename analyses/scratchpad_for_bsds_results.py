# 001
CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_001_no_aux_2019_05_20_08_40_16_470144/model_240.ckpt-240 --placeholders --test --out_dir=bsds_portrait --train=BSDS500_test_portrait --val=BSDS500_test_portrait

CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_001_no_aux_2019_05_20_08_40_16_470144/model_240.ckpt-240 --placeholders --test --out_dir=bsds_landscape --train=BSDS500_test_landscape --val=BSDS500_test_landscape


# 010
CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_010_no_aux_2019_05_20_00_56_18_486429/model_280.ckpt-280 --placeholders --test --out_dir=bsds_portrait --train=BSDS500_test_portrait --val=BSDS500_test_portrait

CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_010_no_aux_2019_05_20_00_56_18_486429/model_280.ckpt-280 --placeholders --test --out_dir=bsds_landscape --train=BSDS500_test_landscape --val=BSDS500_test_landscape

# 100
CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_100_no_aux_2019_05_20_00_56_41_386546/model_1240.ckpt-1240 --placeholders --test --out_dir=bsds_portrait --train=BSDS500_test_portrait --val=BSDS500_test_portrait

CUDA_VISIBLE_DEVICES=0 python run_job.py --experiment=BSDS500_test --model=BSDS_vgg_cheap_deepest_final_simple --no_db --ckpt=/media/data_cifs/cluttered_nist_experiments/checkpoints/BSDS_vgg_cheap_deepest_final_simple_BSDS500_combos_100_no_aux_2019_05_20_00_56_41_386546/model_1240.ckpt-1240 --placeholders --test --out_dir=bsds_landscape --train=BSDS500_test_landscape --val=BSDS500_test_landscape


python utils/plot_bsds.py --f=bsds_portrait/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_25_56_950811.npz --tag=001
python utils/plot_bsds.py --f=bsds_landscape/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_34_38_836812.npz --tag=001

python utils/plot_bsds.py --f=bsds_portrait/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_37_58_289988.npz --tag=010
python utils/plot_bsds.py --f=bsds_landscape/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_44_05_939046.npz --tag=010


python utils/plot_bsds.py --f=bsds_portrait/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_42_30_933063.npz --tag=100
python utils/plot_bsds.py --f=bsds_landscape/BSDS_vgg_cheap_deepest_final_simple_BSDS500_test_2019_05_20_15_39_44_444407.npz --tag=100

