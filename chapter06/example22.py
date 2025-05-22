tax_factors = [1.05, 1.08, 1.04, 0.00, 1.03]
price = 100.00
for factor in tax_factors:
    if factor == 0:
        continue
    else:
        original_price = price / factor
        tax_rate = int((factor - 1) * 100)
        print(f"The price less {tax_rate}% tax is ${original_price:.2f}")
