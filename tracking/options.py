from collections import OrderedDict

opts = OrderedDict()
opts['use_gpu'] = True  # if you change to False ,it will use CPU to run,but is very slow
#opts['model_path1'] = "../models/MANet-2IC-ori.pth"

opts['img_size'] = 107
opts['padding'] = 16

opts['batch_pos'] = 32
opts['batch_neg'] = 96
opts['batch_neg_cand'] = 1024
opts['batch_test'] = 256

opts['n_samples'] = 256
opts['n_samples_after'] = 64


opts['trans_f'] = 0.73  #0.6  # arcface+attention 0.7
opts['scale_f'] = 1.12 #1.05  # arcface+attention 1.1
opts['trans_f_expand'] = 1.5

opts['n_bbreg'] = 1000
opts['overlap_bbreg'] = [0.6, 1]
opts['scale_bbreg'] = [1, 2]

opts['lr_init'] = 0.0006 #0.001
opts['maxiter_init'] = 30
opts['n_pos_init'] = 500
opts['n_neg_init'] = 5000
opts['overlap_pos_init'] = [0.7, 1]
opts['overlap_neg_init'] = [0, 0.5]

opts['lr_update'] = 0.0018 #0.002
opts['maxiter_update'] = 15
opts['n_pos_update'] = 50
opts['n_neg_update'] = 200
opts['overlap_pos_update'] = [0.7, 1]
opts['overlap_neg_update'] = [0, 0.3]

opts['success_thr'] = [-0.2,1]   #arcface+attention [-0.2,1]
opts['n_frames_short'] = 20
opts['n_frames_long'] = 100  # init 100
opts['long_interval'] = 10

opts['w_decay'] = 0.0005
opts['momentum'] = 0.9
opts['grad_clip'] = 10
opts['lr_mult'] = {'w':0.5, 'fc4':5, 'fc5': 5}  # test gtot use {'fc6':10,'fc4':5,'fc5':5} # rgbt234 use {'fc6':10}
#opts['ft_layers'] = ['fc']
opts['ft_layers'] = ['fc','w']
