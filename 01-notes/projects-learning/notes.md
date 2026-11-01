# Project: Financial Sentiment Analysis
Date: 2026-10-31

## ==🔵Creating Virtual Environment==
```bash
python -m venv .venv # run built-in module called vinv and put it in .venv folder
.venv\Scripts\Activate.ps1 # ps1 stands for powershell

# If scripts being disabled
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
## ==🔵PowerShell vs Command Prompt==
Command prompt is the old and basic one, while PowerShell is newer and with more features one.

## ==🔵Getting Data from Hugging Face - Financial Phrase Bank==

#### Data Set Scripts Failure Reasons
1. Security - python programs means running someone's else code in your computer, which will cause risk, while CSV, Parquet can't run code, so it's safe to read time
2. Scripts break over time - script usually downloads file from other websites, and these websites might die already.
#### Hugging Face Loader vs Pandas
Using hugging face loader means depending on data set packaging and Hugging Face training tools, but it is the standard in modern AI work, while using pandas, you can inspect and clean with no dependencies, but it doesn't know about datasets.

## ==🔵Glob Method==
Finding files by matching pattern with wildcards
```python
file_names = file_path.glob("File_*.txt") # all files with File_ prefix

# * means any characters
# ? exactly one character
# [abd] one character from set
# ** any number of folders
```

## ==🔵How to Read Files==
```python
with open(path, encoding="utf-8") as f:
	for line in f:
		print(line)
```

## Utilize `Path()` Function
```python
path = Path(path_link)

path.stem.replace("File_", "") # path.stem only get the filename
```

## Utilize `Pandas`
```python
df = pd.DataFrame(list, columns=["key1", "key2"])

df["label"].value_counts() # count distinct value

df.sample(5, random_state=1) # give same result every time
```

## ==🔵Encoding Alternatives==
```python

encoding="utf-8" # bytes/char = 1-4, potential unicodedecode error
encoding="latin-1" # b/c = 1, never raise error
```