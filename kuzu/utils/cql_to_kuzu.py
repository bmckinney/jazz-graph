import os
import re

def process_cql_files(cql_directory='../cql', import_directory='import'):
    # Define the text to add at the beginning and end of each file
    text_to_add_beginning = """
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
\"\"\"

"""
    text_to_add_end = "\n\n\"\"\"\n)"

    # Iterate over each file in the directory
    for filename in os.listdir(cql_directory):
        if filename.endswith('.cql'):
            filepath = os.path.join(cql_directory, filename)

            # Read the existing content of the file
            with open(filepath, 'r') as file:
                content = file.read()

            # Modify the content
            content = re.sub(r'\.begin = ', '.begin_date = ', content)
            content = re.sub(r'\.end = ', '.end_date = ', content)
            content = re.sub(r' end: ', ' end_date: ', content)
            content = re.sub(r' begin: ', ' begin_date: ', content)
            content = re.sub(r'SET \w+\.timestamp = timestamp\(\)', '', content)
            content = re.sub(r"\\'", "\\\\\\'", content)
            content = text_to_add_beginning + content + text_to_add_end

            # Create a new file path with the .sql extension
            new_filename = os.path.splitext(filename)[0] + '.py'
            new_filepath = os.path.join(import_directory, new_filename)

            # Write the new content to the file with the new extension
            with open(new_filepath, 'w') as file:
                file.write(content)

            # Optionally remove the original .cql file
            # os.remove(filepath)

            print(f"Processed {filename} -> {new_filename}")


process_cql_files('../cql', 'import')
process_cql_files('../cql/annotations', 'import/annotations')
process_cql_files('../cql/videos', 'import/videos')