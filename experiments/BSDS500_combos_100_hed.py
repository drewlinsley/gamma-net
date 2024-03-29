import os


def experiment_params():
    """Specifification of experiment params and model hps."""
    exp = {}
    exp['repeat'] = 1  # Repeat each derived experiment this many times

    # Experiment params. All below this line need to be in lists.
    exp['experiment'] = [__file__.split(os.path.sep)[-1].split('.')[0]]
    exp['train_dataset'] = [
        'BSDS500_100_hed',
    ]
    exp['val_dataset'] = [
        'BSDS500_100',
    ]
    exp['model'] = [
    ]

    exp['validation_period'] = [20]
    exp['validation_steps'] = [200 / 1]
    exp['shuffle_val'] = [True]  # Shuffle val data.
    exp['shuffle_train'] = [True]
    exp['save_checkpoints'] = [1]
    exp['save_activities'] = [False]
    exp['save_weights'] = [False]
    exp['save_gradients'] = [False]
    exp['get_map'] = [False]  # Get mean average precisions

    # Model hyperparameters
    exp['lr'] = [1e-5]
    exp['exclusion_lr'] = 3e-4
    exp['exclusion_scope'] = 'fgru'
    # exp['lr'] = [1e-2]
    exp['train_loss_function'] = ['bi_bce_hed']  # ['pearson']  # ['hed_bce']  # ['bsds_bce']
    exp['val_loss_function'] = ['bi_bce_hed']  # ['pearson']  # ['hed_bce']  # ['bsds_bce']  # ['bsds_bce']
    # exp['train_loss_function'] = ['dice_bce']  # ['pearson']  # ['hed_bce']  # ['bsds_bce']
    # exp['val_loss_function'] = ['dice_bce']  # ['pearson']  # ['hed_bce']  # ['bsds_bce']  # ['bsds_bce']
    exp['score_function'] = ['pixel_error']  # ['bsds_f1']
    exp['optimizer'] = ['adam']  # ['momentum']
    # exp['optimizer'] = ['adam']  # ['momentum']
    # exp['lr_schedule'] = [{'bsds': [8, 1]}]
    # exp['optimizer'] = ['momentum']  # , 'adam']
    # exp['lr_schedule'] = [{'bsds': [2, 2]}]
    exp['early_stop'] = 200
    # exp['clip_gradients'] = 7
    exp['train_batch_size'] = [1]  # 10]
    exp['val_batch_size'] = [1]  # 10]
    exp['epochs'] = [2048 * 2]

    # Augmentations specified in lists of lists
    exp['train_augmentations'] = [[
        'rc_image_label',
        'pascal_normalize',
        'image_to_bgr',
    ]]
    exp['val_augmentations'] = [[
        'cc_image_label',
        'pascal_normalize',
        'image_to_bgr',
    ]]
    return exp

