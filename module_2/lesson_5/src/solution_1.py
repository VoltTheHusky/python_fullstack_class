company = input ("Название компании (первоначальное): ")
len_company = len(company) //2
new_company = company[len_company:] + company[:len_company]
print("Название компании (новое): ", new_company)