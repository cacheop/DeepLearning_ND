pip install -r floyd_requirements.txt
cp -r /code/* /output
cd /output
/run_jupyter.sh --no-browser --NotebookApp.base_url='/NZSYZLDdVJXHCeFE6b6nn4' --NotebookApp.token='' --NotebookApp.allow_origin='*'