import re

def extract_to_csv(text, csv_file_path):
    # Extract bandwidth value
    matrix_section = re.search(r'Numa node.*?(\s+\d.*)', text, re.DOTALL)
    if not matrix_section:
        return None

    matrix_lines = matrix_section.group(1).strip().split('\n')

    # Build CSV data
    csv_lines = []
    for line in matrix_lines:
        # Modify regular expression to match integers and decimals
        values = re.findall(r'\d+\.?\d*', line)
        csv_line = ','.join(values)
        csv_lines.append(csv_line)

    # Save to CSV file
    with open(csv_file_path, 'w') as csv_file:
        for line in csv_lines:
            csv_file.write(line + '\n')

# Sample text
text = """
Intel(R) Memory Latency Checker - v3.11
Command line parameters: --bandwidth_matrix 

Using buffer size of 100.000MiB/thread for reads and an additional 100.000MiB/thread for writes
*** Unable to modify prefetchers (try executing 'modprobe msr')
*** So, enabling random access for latency measurements
Measuring Memory Bandwidths between nodes within system 
Bandwidths are in MB/sec (1 MB/sec = 1,000,000 Bytes/sec)
Using all the threads from each core if Hyper-threading is enabled
Using Read-only traffic type
        Numa node
Numa node         0        1    
       0    58449.2  250000
       1      72340.5  184293
"""

# Call function and save CSV
csv_file_path = 'output.csv'
extract_to_csv(text, csv_file_path)

print(f"Data has been saved to {csv_file_path}.")
