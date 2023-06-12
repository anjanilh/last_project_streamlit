import streamlit as st
import numpy as np
from scipy import stats

def calculate_variance_test(sample1, sample2, alpha):
    n1 = len(sample1)
    n2 = len(sample2)
    var1 = np.var(sample1, ddof=1)
    var2 = np.var(sample2, ddof=1)
    test_statistic = var1 / var2
    df1 = n1 - 1
    df2 = n2 - 1
    critical_value_lower = stats.f.ppf(alpha/2, df1, df2)
    critical_value_upper = stats.f.ppf(1 - alpha/2, df1, df2)
    p_value = 2 * (1 - stats.f.cdf(test_statistic, df1, df2))
    return test_statistic, critical_value_lower, critical_value_upper, p_value

st.title('Uji Hipotesis Varians Dua Populasi')

sample1 = st.text_input('Masukkan data sampel pertama (pisahkan dengan koma):')
sample1 = np.fromstring(sample1, sep=',')

sample2 = st.text_input('Masukkan data sampel kedua (pisahkan dengan koma):')
sample2 = np.fromstring(sample2, sep=',')

alpha = st.number_input('Masukkan tingkat signifikasi (alpha):', min_value=0.01, max_value=0.99, value=0.05, step=0.01)

if st.button('Hitung'):
    test_statistic, critical_value_lower, critical_value_upper, p_value = calculate_variance_test(sample1, sample2, alpha)
    st.write('Statistik Uji:', test_statistic)
    st.write('Confident Interval:', (1 / critical_value_upper, 1 / critical_value_lower))
    st.write('P-Value:', p_value)
    
    if test_statistic < critical_value_lower or test_statistic > critical_value_upper:
        st.write('Maka, dapat diputuskan gagal tolak hipotesis nol. Artinya, terdapat bukti yang cukup untuk menyatakan bahwa varians populasi pertama tidak sama dengan varians populasi kedua.')
    else:
        st.write('Maka, dapat diputuskan tolak hipotesis nol. Artinya, tidak terdapat bukti yang cukup untuk menyatakan bahwa varians populasi pertama tidak sama dengan varians populasi kedua.')
