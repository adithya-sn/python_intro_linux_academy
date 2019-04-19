import os

#stage = os.environ['STAGE'].upper()
stage = os.getenv('STAGE', 'dev').upper() ## set a default value
output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!!  -  " + output

print(output)

## It is possible to pass env vars when running the code: STAGE="Prod" python3 env_vars.py ##