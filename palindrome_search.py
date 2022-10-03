def palindrome_search(words):
	palinroms_counter = 0
	for word in words:
		word_check = word.lower()
		list_letter = []
		len_word = len(word_check)
		for letter in word_check:
			list_letter.append(letter)
		for check_palindrom in range(0, len_word//2): # при делении на 2 находим середину
			change_letter = list_letter[check_palindrom] # т.к меняем буквы местами до середины(2 раза)
			list_letter[check_palindrom] = list_letter[len_word - check_palindrom - 1]
			list_letter[len_word - check_palindrom - 1] = change_letter
		new_word = ""
		for join_letters in list_letter:
			new_word += join_letters
		if word_check == new_word:
			print(f"[{word_check}] является палиндромом")
			palinroms_counter += 1
	print()
	print(f"Найдено {palinroms_counter} палиндромов | APSN4")


words = ["машина", "хакер", "мадам", "Лаунч", "казак", "Потоп", "radar"]
palindrome_search(words)