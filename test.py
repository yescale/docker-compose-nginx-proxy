import subprocess
import json

# Run the docker compose ps command
result = subprocess.run(['docker', 'compose', 'ps', '--format', 'json'], stdout=subprocess.PIPE)

# Decode the output to a string
output = result.stdout.decode('utf-8')

# Load the JSON output into a list
services_list = json.loads(output)

# Print the list
print(services_list)
