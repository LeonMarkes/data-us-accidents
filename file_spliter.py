# File spliter
import os

def file_input_handler():
    # while True:
    #     try:
    #         file_name = input('On how many files do you want to split your data?: ')
    #         return file_name
    #     except TypeError:
    #         print('Please enter a number.')
    file_name = input('Enter csv name (exl. dataset.csv): ')
    return file_name



def file_number_handler():
    # while True:
    #     try:
    #         file_number = int(input('On how many files do you want to split your data?: '))
    #         break
    #     except TypeError:
    #         print('Please enter a number.')
    file_number = int(input('On how many files do you want to split your data?: '))
    return file_number


def main():
    csv_document = file_input_handler()
    file_number = file_number_handler()
    document_name = csv_document.split('.')[0]
    os.makedirs(document_name)
    with open(csv_document, mode='r') as data:
        data = data.read()
        for number in range(file_number):
            file = open(document_name + '/' + document_name + '_' + str(number) + '.csv', mode='a')
            counter = 0

            for _ in data: #
                if counter == 0:
                    data_row = str(data[0])
                    file.write(data_row)
                    data = data[1:]
                    counter += 1
                elif counter < file_number:
                    counter += 1
                else:
                    counter = 0

                # presporo je O(n^2), ubrzaj O(n)

    print('Done!')






if __name__ == '__main__':
    main()
