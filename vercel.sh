#!/bin/bash



# Install Python dependencies
pip install -r requirements.txt

# Check if the environment is production or preview
if [[ $VERCEL_ENV == "production"  ]] ; then 
  npm run build:production
else 
  npm run build:preview
fi
