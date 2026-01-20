"""Извлеките ключи ["name", "salary"] из sample_dict.
sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
new_dict = {
    "name": sample_dict.get("name"),
    "salary": sample_dict.get("salary")
}
print(new_dict)