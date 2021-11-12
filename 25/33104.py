for i in range(289123456, 389123456 + 1):  # 289123456, 389123456 + 1
    memory = [0, 0, 0]
    k = 0
    for divider in range(2, i):
        if i % divider == 0:
            k += 1
            if k > 3:
                print(f"Есть контакт: {i} и {max(memory)}")
                break
            memory[k - 1] = divider
    if k == 3:
        print(i, max(memory))
