import argparse, yaml
from configs.build_config import configs

def parse_args():
    parser = argparse.ArgumentParser(description='MAC_Classification Args')
    parser.add_argument('--dataset', type=str, choices=['cifar10','cifar100','imagenet'], required=True, help='choose the dataset')
    parser.add_argument('--gpu', type=str, help="gpu choose, eg. '0,1,2,...' ")
    parser.add_argument('--run', type=str, dest='run_mode',choices=['train','test'])
    parser.add_argument('--seed', type=int, help='fix random seed')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    cfg_file = "configs/{}.yaml".format(args.dataset)
    with open(cfg_file, 'r') as f:
        yaml_dict = yaml.load(f)

    args_dict = configs.parse_to_dict(args)
    args_dict = {**yaml_dict, **args_dict}
    configs.add_args(args_dict)

    configs.training_init()
    configs.path_init()

    print("Hyper parameters:")
    print(configs)

    # net = resnet18()
    # get_optim(configs,net)