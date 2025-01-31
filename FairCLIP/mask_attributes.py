
import pandas as pd
import numpy as np
import os
import re

if __name__ == "__main__":
    
    data_dir = 'summaries'
    file_name = 'gpt4_summarized_notes.csv'
    df = pd.read_csv(os.path.join(data_dir, file_name))

    num_points = df.shape[0]
    samples = np.random.choice(num_points, size=50, replace=False)
    print(samples)
    df_samples = df.iloc[samples]

    words_to_mask = ['asian', 'black', 'white', 'male', 'female', 'non-hispanic', 'hispanic', 'english', 'spanish',
                     'female', 'male', 'his', 'her', 'woman', 'man', 'he', 'she']
    
    # identifying_words = ['female', 'male', 'his', 'she', 'woman', 'man']
    # False negatives: She'd

    # counts = {w:0 for w in words_to_mask}
    # total_count = 0
    
    # for index, row in df.iterrows():
    #     label = row.iloc[0].strip()
    #     summary = row.iloc[2].strip()

    #     # print(f"Label: {label}:")
    #     # print(summary, "\n")
        
    #     words = summary.lower().split()
    #     for w in words:
    #         for attribute in words_to_mask:
    #             if w == attribute:
    #                 counts[w] += 1
    #                 total_count += 1
                        
    # print(total_count)
    # print(counts)



    #####    Mask words    ######
    # regex = re.compile(r"|".join(words_to_mask), re.IGNORECASE)
    regex = re.compile(r"\b(" + r"|".join(re.escape(word) for word in words_to_mask) + r")\b", re.IGNORECASE)
    print(regex)
    
    masked_summaries = {"label": [], "original summary": [], "masked summary": []}
    
    for index, row in df.iterrows():
        label = row.iloc[0].strip()
        summary = row.iloc[2].strip()
        
        masked_summary = re.sub(regex, "[REDACTED]", summary)

        masked_summaries['label'].append(label)
        masked_summaries['original summary'].append(summary)
        masked_summaries['masked summary'].append(masked_summary)

    masked_df = pd.DataFrame(masked_summaries)
    masked_df.to_csv(os.path.join(data_dir, 'masked_summarized_notes.csv'), index=False)

        
        
        
            


            




        





