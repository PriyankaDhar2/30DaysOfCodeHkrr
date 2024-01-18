def create_phone_book(entries):
    phone_book = {}
    for entry in entries:
        name, phone_number = entry.split()
        phone_book[name] = phone_number
    return phone_book

def process_queries(phone_book, queries):
    for query in queries:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")

num_entries = int(input().strip())
entries = [input().strip() for _ in range(num_entries)]
queries = []
try:
    while True:
        query = input().strip()
        if not query:
            break
        queries.append(query)
except EOFError:
    pass

phone_book = create_phone_book(entries)
process_queries(phone_book, queries)
