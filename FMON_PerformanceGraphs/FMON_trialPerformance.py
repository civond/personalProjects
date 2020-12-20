import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def performanceGraph():
    df = pd.read_csv('goodMice.csv')
    df.drop(df.columns.difference(['mouse','experiment','trialnum','100-0 totalCorrect', '100-0 totalAttempts', '90-10 totalCorrect', '90-10 totalAttempts']), 1, inplace=True)
    List_Of_Categories_In_Column=list(df['experiment'].value_counts().index)

    #100-0
    df100 = df[df['experiment'] == '100-0']
    df100['100percentage'] = df100['100-0 totalCorrect'] / df100['100-0 totalAttempts']*100
    df100.drop(df100.columns.difference(['mouse','trialnum','100percentage']),1, inplace=True)

    #trainer2 (100-0)
    dftrainer = df[df['experiment'] == 'trainer2']
    dftrainer['trainerpercentage'] = dftrainer['100-0 totalCorrect'] / dftrainer['100-0 totalAttempts']*100
    dftrainer.drop(dftrainer.columns.difference(['mouse','trialnum','trainerpercentage']),1, inplace=True)

    #90-10
    df90 = df[df['experiment'] == '90-10']
    df90['90percentage'] = df90['90-10 totalCorrect'] / df90['90-10 totalAttempts']*100
    df90.drop(df90.columns.difference(['mouse','trialnum','90percentage']),1, inplace=True)
    fig, ax = plt.subplots()

    #graphing
    df90.groupby('mouse').plot(x='trialnum', y='90percentage', ax=ax, legend=False)
    plt.legend(['2131','2132','2135'])
    plt.xlabel("Session")
    plt.ylabel("Percentage Correct")
    plt.title("90-10 Performance Graph")

    ax.set_xlim(right=13)

    plt.show()
performanceGraph()
