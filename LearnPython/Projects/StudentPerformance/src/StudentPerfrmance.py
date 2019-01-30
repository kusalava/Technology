import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


input_data = pd.read_csv('../InputData/StudentsPerformance.csv')
#print(input_data)

def average_marks(input_data):
    print('Average  math score',np.mean(input_data['math_score']))
    print('Average  reading score',np.mean(input_data['reading_score']))
    print('Average  writing score',np.mean(input_data['writing_score']))
    print('math pass percentsge',(len(input_data[input_data['math_score']>35])/len(input_data['math_score'])) * 100)
    print('reading_score pass percentsge',(len(input_data[input_data['reading_score']>35])/len(input_data['reading_score'])) * 100)
    print('writing_score pass percentsge',(len(input_data[input_data['writing_score']>35])/len(input_data['writing_score'])) * 100)
    print('Total pass percentsge',(len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35)])/len(input_data['writing_score'])) * 100)
    print('A Section pass percentage',(len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='E')])/len(input_data['writing_score'])) * 100)
def pie_chart(input_data):
    
    print('Total A section passed',(len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='A')])))
    print('Total A section',(len(input_data[(input_data['section']=='A')])))
    A = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='A')])/len(input_data[input_data['section']=='A'])) * 100
    B = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='B')])/len(input_data[input_data['section']=='B'])) * 100
    C = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='C')])/len(input_data[input_data['section']=='C'])) * 100
    D = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='D')])/len(input_data[input_data['section']=='D'])) * 100
    E = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['section']=='E')])/len(input_data[input_data['section']=='E'])) * 100
    #print(input_data[input_data['reading_score']>35].head(1))
    labels = 'A', 'B', 'C', 'D','E'
    sizes = [A, B, C, D, E]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0.0, 0.0, 0.0, 0.0,0.0)  # explode 1st slice
# Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=180)
    plt.title('Pass % of each section')
    plt.axis('equal')
    plt.show()
   ######################### Pass % of Girls vs boys ##################################
    girls = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['gender']=='F')])/len(input_data[input_data['gender']=='F'])) * 100
    boys = (len(input_data[(input_data['reading_score']>35) & (input_data['writing_score']>35) & (input_data['math_score']>35) & (input_data['gender']=='M')])/len(input_data[input_data['gender']=='M'])) * 100
    print('boys passed',boys)
    print('girl passed',girls)
    names = 'Boys','Girls'
    new_sizes = [boys,girls]
    new_colors = ['lightcoral','pink']
    explode = (0.0, 0.0)  # explode 1st slice

    plt.pie(new_sizes,explode=explode,labels=names,colors = new_colors,autopct='%1.1f%%',shadow=True, startangle=40)
    plt.title('Pass % of boys and girls ')
    plt.show()
    
## Status - Completed -###########
average_marks(input_data)
pie_chart(input_data)