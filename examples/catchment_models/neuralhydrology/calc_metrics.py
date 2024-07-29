import os
import pandas as pd

def calc_metrics(model_dir, run_dir, epoch):
    path_to_csv = f'/groups/esm/achiang/Rivers/examples/catchment_models/{model_dir}/runs/{run_dir}/test/model_epoch0{epoch}/test_metrics.csv'

    df = pd.read_csv(path_to_csv)
    df = df.dropna()

    nse = df['NSE']
    nse_lt0 = nse[nse < 0]
    nse_gt0 = nse[nse > 0]

    pct_nse_lt0 = round(100 * len(nse_lt0)/len(nse), 2)
    mean_nse_gt0 = round(nse_gt0.mean(), 2)
    median_nse = round(nse.median(), 2)

    return pct_nse_lt0, mean_nse_gt0, median_nse

if __name__=="__main__":
    metric = 'NSE'
    run_dict = { 
                # 'lstm_training':
                #     ['usa_time_split_adj_0807_170652'],
                'neuralhydrology':
                    ['usa_time_split_nse_lr1_2807_223043',
                    'usa_time_split_nse_lr2_2807_223530',
                    'usa_time_split_nse_lr3_2807_224643',
                    'usa_time_split_nse_lr4_2807_224643',
                    'usa_time_split_nse_lr5_2807_224901']
                }

    for model_dir, run_dirs in run_dict.items():
        if model_dir == 'lstm_training':
            model = 'LSTM'
            epoch = '14'
        else:
            model = 'coRNN'
            epoch = '35'

        for run_dir in run_dirs:
            parts = run_dir.split('_')
            exp_name = f"{model}: {parts[3]} {parts[4]}"
            pct_nse_lt0, mean_nse_gt0, median_nse = calc_metrics(model_dir, run_dir, epoch)
            print(exp_name)
            print(f'%_{metric}<0 : {pct_nse_lt0}%')
            print(f'Mean_{metric}>0 : {mean_nse_gt0}')
            print(f'Median {metric}: {median_nse} \n')