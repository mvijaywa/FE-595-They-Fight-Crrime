
# coding: utf-8

# #### Importing libraries

# In[1]:


from textblob import TextBlob
import pandas as pd


# In[45]:


###Creating an empty data frame for male and female characters
def second_script(file):
    df_male=pd.DataFrame()
    df_Female=pd.DataFrame()

    ###Opening the merged text file and splitting the he and she characters
    with open(file,'r') as f:
        for i in f:
            new_line=i.replace("They fight crime!"," ")
            if ("She's" in new_line):
                line_split=new_line.split("She's")[1]
    ###Appending the dataframe and find the polarity/Sentiment using TextBlob
                df_Female=df_Female.append({'Character':line_split,'Polarity':TextBlob(line_split).sentiment.polarity},ignore_index=True)
            if("He's" in new_line):
                line_split=new_line.split("He's")[1]
                df_male=df_male.append({'Character':line_split,'Polarity':TextBlob(line_split).sentiment.polarity},ignore_index=True)

                ###Sorting the dataframe by polarity
    df_male=df_male.sort_values(by=['Polarity'])
    df_Female=df_Female.sort_values(by=['Polarity'])

    ###getting the worst and the best characters and joining them
    Worst_char="He's "+df_male.head(1)['Character'].values[0].strip()+"She's "+df_Female.head(1)['Character'].values[0].strip()+"They fight crime!"
    Best_char="He's"+df_male.tail(1)['Character'].values[0].strip()+"She's"+df_Female.tail(1)['Character'].values[0].strip()+"They fight crime!"
    print(Worst_char)
    print(Best_char)

if __name__ == "__main__":
    second_script('merge.txt')

