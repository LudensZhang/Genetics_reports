from  scipy.stats import chi2_contingency
import pandas as pd

def calculate(a,b):
    matrix = pd.DataFrame(list(zip(a,b)), columns=['实验值', '理论值'])
    print('将对如下数据进行卡方检验', '\n',matrix)
    kf = chi2_contingency(matrix)
    print('检验结果如下', '\n','chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)

if __name__ == '__main__':

    group1_exp = [int (i) for i in input('请输入红雄X白雌的实验数据').split()]
    group1_theo = [sum(group1_exp)/len(group1_exp) for i in range(len(group1_exp))]
    calculate(group1_exp, group1_theo)

    group2_exp = [int (i) for i in input('请输入红雌X白雄的实验数据').split()]
    group2_exp.sort(reverse=True)
    group2_theo = [2*sum(group2_exp)/(len(group2_exp)+1), sum(group2_exp)/(len(group2_exp)+1), sum(group2_exp)/(len(group2_exp)+1)]
    calculate(group2_exp, group2_theo)
    
    
