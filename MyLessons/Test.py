import pandas as pd
from deep_translator import GoogleTranslator
import ast
import os
from tqdm import tqdm

def translate_text(text, source_lang='auto', target_lang='az'):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text

# Məlumat faylını oxumaq
df = pd.read_parquet(r"D:\Downloads\train-00000-of-00001.parquet")

# Tərcümə ediləcək konversiyaları idarə edən funksiya
def translate_conversations(conversations):
    if isinstance(conversations, str):
        try:
            conversations_list = ast.literal_eval(conversations)  
        except (ValueError, SyntaxError):
            conversations_list = eval(conversations)
    else:
        conversations_list = conversations.tolist()  
    for conv in conversations_list:
        if 'value' in conv:
            conv['value'] = translate_text(conv['value'])

    return str(conversations_list)

# Tərcümə prosesini daha yaxşı izləmək üçün tqdm istifadə etmək
def translate_in_batches(df, batch_size=100):
    total_rows = len(df)
    num_batches = (total_rows // batch_size) + (1 if total_rows % batch_size != 0 else 0)
    
    # Hər bir hissəni tərcümə edib fayla yazmaq
    output_folder = r"C:\Users\ASUS\Desktop\Model Ucun Datalar"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_batches):
        start_index = i * batch_size
        end_index = start_index + batch_size
        batch_df = df.iloc[start_index:end_index]
        
        # Tərcümə tətbiq etmək
        batch_df['translated_conversations'] = batch_df['conversations'].apply(translate_conversations)

        # Hər bir hissəni fərdi olaraq saxlayın
        output_file_name = f'translated_data_{i+1}.parquet'
        output_file_path = os.path.join(output_folder, output_file_name)
        batch_df.to_parquet(output_file_path, index=False)

        print(f"{i+1}-ci hissə tərcümə olundu və '{output_file_path}' faylında saxlanıldı.")

# Tərcüməni icra et
print("Prosesə başlamaq üçün hazırlıq görülür...")
translate_in_batches(df)
print("Tərcümə prosesi tamamlandı.")
