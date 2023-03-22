# **04.GitOps**
## **yaml github action**
```bash
name: tabs
on:
  push:
  pull_request:
jobs:
  Checkingfiles:
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@v3
      with:
        fetch-depth: 0
    - name: Get changed files
      id: changed-files
      uses: tj-actions/changed-files@v35
    - name: count tabs
      run: |
        for file in ${{ steps.changed-files.outputs.all_changed_files }}; do
        echo "$file was changed" >> tabs.log
        echo "This file have `grep -P '\t' $file | wc -l` tabs." >> tabs.log
        done
    - name: tabs artifact
      uses: actions/upload-artifact@v3
      with:
        path: tabs.log
```