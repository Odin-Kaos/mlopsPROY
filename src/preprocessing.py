import math
import random
import re
import numpy as np

# 1. Removal of missing values
def remove_missing(values):
    return [v for v in values if v not in (None, "", float("nan")) and not (isinstance(v, float) and math.isnan(v))]

# 2. Filling missing values
def fill_missing(values, fill_value=0):
    return [fill_value if v in (None, "") or (isinstance(v, float) and math.isnan(v)) else v for v in values]

# 3. Removal of duplicated values
def remove_duplicates(values):
    return list(dict.fromkeys(values))  # preserves order

# 4. Min-Max Normalization
def normalize_minmax(values, new_min=0.0, new_max=1.0):
    arr = np.array(values, dtype=float)
    old_min, old_max = arr.min(), arr.max()
    return ((arr - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

# 5. Z-score Standardization
def standardize_zscore(values):
    arr = np.array(values, dtype=float)
    mean, std = arr.mean(), arr.std()
    return (arr - mean) / std

# 6. Clipping values
def clip_values(values, min_val, max_val):
    return [min(max(v, min_val), max_val) for v in values]

# 7. Conversion to integers
def convert_to_int(values):
    result = []
    for v in values:
        try:
            result.append(int(v))
        except (ValueError, TypeError):
            continue
    return result

# 8. Logarithmic scale transformation
def log_transform(values):
    return [math.log(v) for v in values if isinstance(v, (int, float)) and v > 0]

# 9. Tokenization (alphanumeric, lowercase)
def tokenize_text(text):
    return re.findall(r"[a-z0-9]+", text.lower())

# 10. Keep only alphanumeric + spaces
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9 ]", "", text)

# 11. Remove stopwords
def remove_stopwords(text, stopwords):
    tokens = tokenize_text(text)
    return " ".join([t for t in tokens if t not in stopwords])

# 12. Flatten list of lists
def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# 13. Random shuffle with seed
def shuffle_list(values, seed=None):
    if seed is not None:
        random.seed(seed)
    shuffled = values[:]
    random.shuffle(shuffled)
    return shuffled
