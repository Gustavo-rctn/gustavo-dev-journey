def visit_page(history, url):
    history.append(url)
    return history

history_list = ['google.com', 'github.com']

new_url = input('Enter the last visited website: ').strip()
updated_history = visit_page(history_list, new_url)

print(f'Browsing history: {updated_history}')
