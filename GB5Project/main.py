import csv
from sklearn.naive_bayes import GaussianNB


# Load data tu CSV file
def load_data(filename):
    lines = csv.reader(open(filename, "rt", encoding="utf8"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset


trainingSet = load_data('data_gb5.csv')
testSet = load_data('test_data.csv')


def get_data_label(dataset):
    data = []
    label = []
    for x in dataset:
        data.append(x[:5])
        label.append(x[-1])

    return data, label


# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        '[1.]': "->  The question in group Openness - O",
        '[2.]': "->  The question in group Conscientiousness - C",
        '[3.]': "-> The question in group Extraversion - E",
        '[4.]': "-> The question in group Agreeableness - A",
        '[5.]': "->  The question in group Neuroticism - N"
    }

    return switcher.get(argument, "nothing")


def convert_score(argument):
    switcher1 = {
        '[1.]': 1,
        '[2.]': 2,
        '[3.]': 3,
        '[4.]': 4,
        '[5.]': 5
    }

    return switcher1.get(argument, "nothing")


def convert_trait(argument):
    switcher2 = {
        1: "O",
        2: "C",
        3: "E",
        4: "A",
        5: "N"
    }

    return switcher2.get(argument, "nothing")


# Driver program

# Compare with sklearn
dataTrain, labelTrain = get_data_label(trainingSet)
dataTest, trait = get_data_label(testSet)
clf = GaussianNB()
clf.fit(dataTrain, labelTrain)

score = clf.predict(dataTest)
# print("1-O // 2-C // 3-E // 4-A // 5-N //")

if convert_score(str(score)) != int(trait[0]):
    print(numbers_to_strings(str(score)))
    print("===> The questions after the test must be in group {}".format(convert_trait(int(trait[0]))))
else:
    print(numbers_to_strings(str(score)))

