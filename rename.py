import os
import yaml
from datetime import datetime, date
import shutil

def rename_markdown_files(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for root, _, files in os.walk(source_directory):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                print(f"Processing file: {filepath}")  # 调试信息
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                # 检查文件是否包含YAML前言
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end != -1:
                        yaml_content = content[3:yaml_end].strip()
                        try:
                            # 解析YAML内容
                            yaml_data = yaml.safe_load(yaml_content)
                            if yaml_data is None:
                                print(f"YAML front matter in {filename} is empty or invalid.")
                                continue

                            if 'date' in yaml_data:
                                # 提取日期并格式化
                                date_value = yaml_data['date']
                                if isinstance(date_value, (datetime, date)):
                                    formatted_date = date_value.strftime('%Y-%m-%d')
                                else:
                                    formatted_date = datetime.strptime(date_value, '%Y-%m-%d').strftime('%Y-%m-%d')

                                # 生成新的文件名
                                new_filename = f"{formatted_date}-{filename}"
                                new_filepath = os.path.join(target_directory, new_filename)

                                # 复制并重命名文件
                                shutil.copy(filepath, new_filepath)
                                print(f"Copied and renamed {filename} to {new_filename}")
                            else:
                                print(f"No date field in YAML front matter of {filename}")
                        except yaml.YAMLError as e:
                            print(f"Error parsing YAML in {filename}: {e}")
                else:
                    print(f"No YAML front matter in {filename}")

# 指定要处理的源文件夹路径和目标文件夹路径
source_directory = 'my_posts'  # 替换为你的源文件夹路径
target_directory = '_posts'  # 替换为你的目标文件夹路径
rename_markdown_files(source_directory, target_directory)