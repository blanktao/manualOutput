import openai
import json

client = openai.Client(
  #openai.api

    )

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formatted_text = ""
    for line in lines:
        line = line.strip()
        if line:  # 确保这一行不是空的
            try:
                data = json.loads(line)
                for key, value in data.items():
                    formatted_text += f"{key}: {value}\n"
                formatted_text += "\n"  # 每个对象之间添加一个空行
            except json.JSONDecodeError as e:
                print(f"JSON解码错误: {e} - 行内容: {line}")
                
    return formatted_text



prompt = read_file('prompt.jsonl')
print(prompt)

response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helperful assistant."},
                {"role": "user", "content": prompt},
                 {"role": "user", "content": "mmm"}
            ],
        )

print( response.choices[0].message.content)
