inputs = [0, 1, 0, 0]  # teg of jingle
weights = [0, 0, 0, 0]  # weights of neur
desired_result = 1  # desired user eval of jingle
learning_rate = 0.2  # learning_rate huly tyt skazat
trials = 6  # numbers of try
prodmarketfit = 0  # what the fuck


def evaluate_neural_network(input_array, weight_array):
    result = 0
    for i in range(len(input_array)):
        layer_value = input_array[i] * weight_array[i]
        result += layer_value
        prodmarketfit = int(result)
        print(prodmarketfit)
    print("Оценка ProdMarkFit(а) джингла: " + str(result))
    print("Показатели соотвествия разным запросам клиента: " + str(weights))
    return result


def evaluate_error(desired, actual):
    error = desired - actual
    print("Оценка дифицита product market fit(а) нейронки: " + str(error))
    return error


def learn(input_array, weight_array):
    print("Я учусь!...")
    for i in range(len(input_array)):
        if input_array[i] > 0:
            weight_array[i] += learning_rate


def train(trials):
    for i in range(trials):
        neural_net_result = evaluate_neural_network(inputs, weights)
        learn(inputs, weights)


train(trials)