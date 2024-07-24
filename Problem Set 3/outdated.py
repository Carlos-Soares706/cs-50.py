months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    date = input('Date: ').strip()
    try:
        # Caso 1: formato MM/DD/YYYY
        month, day, year = date.split('/')
        if (int(day) >= 1 and int(day) <= 31 and int(month) >= 1 and int(month) <= 12):
            break
    except ValueError:
        try:
            # Caso 2: formato Month Day, Year
            o_month, o_day, year = date.split(" ")
            for i in range(len(months)):
                if o_month == months[i]:
                    month = i + 1
                    break
            else:
                continue  # O mês não foi encontrado na lista, continue para a próxima iteração

            day = o_day.replace(',', '')
            if not o_day.endswith(','):
                continue

            if (int(day) >= 1 and int(day) <= 31):
                break
        except ValueError:
            continue  # Se ocorrer um ValueError, continue para a próxima iteração

print(f'{year}-{int(month):02}-{int(day):02}')
