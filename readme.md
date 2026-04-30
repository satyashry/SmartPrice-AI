- Loaded raw scraped data (984 rows)
- Cleaned ₹ symbols from prices → converted to float
- Dropped rows where current_price > original_price (bad scrape)
- Calculated discount_pct
- Extracted features from product name using regex:
  - ram, storage, os, graphics, processor, brand
- Filled nulls → median for numbers, mode for text
- Final clean data: 614 rows × 9 columns


