"""В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
1. в каких магазинах нельзя приобрести сыр.
2. в каких магазинах можно приобрести одновременно молоко и сахар.
3. в каких магазинах можно приобрести соль."""
magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}
try:
    print("1. Магазины без сыра:")
    if "сыр" not in magnit:
        print("- Магнит")
    if "сыр" not in pyaterochka:
        print("- Пятерочка")
    if "сыр" not in perekrestok:
        print("- Перекресток")
    print()

    print("2. Магазины с молоком и сыром одновременно:")
    if "молоко" in magnit and "сыр" in magnit:
        print("- Магнит")
    if "молоко" in pyaterochka and "сыр" in pyaterochka:
        print("- Пятерочка")
    if "молоко" in perekrestok and "сыр" in perekrestok:
        print("- Перекресток")
    print()

    print("3. Магазины с солью:")
    if "соль" in magnit:
        print("- Магнит")
    if "соль" in pyaterochka:
        print("- Пятерочка")
    if "соль" in perekrestok:
        print("- Перекресток")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")