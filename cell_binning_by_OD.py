import csv


def main():
    filename_list = "TranslateBio_filenames.csv"
    with open(filename_list, newline="") as csvfile:
        filename = csv.DictReader(csvfile)
        for cell in filename:
            obj_data = str(cell["File Name"])
            print (obj_data)
            with open(obj_data, newline="") as new_csvfile:
                reader = csv.DictReader(new_csvfile)
                bin0_count = 0
                bin1_count = 0
                bin2_count = 0
                bin3_count = 0
                bin4_count = 0
                for data in reader:
                    if float(data["Probe 1 Avg OD"]) == 0:
                        bin0_count += 1
                    elif 0 < float(data["Probe 1 Avg OD"]) <= 0.5:
                        bin1_count += 1
                    elif 0.5 < float(data["Probe 1 Avg OD"]) <= 1:
                        bin2_count += 1
                    elif 1 < float(data["Probe 1 Avg OD"]) <= 1.5:
                        bin3_count += 1
                    else:
                        bin4_count += 1
            total_count = bin0_count+bin1_count+bin2_count+bin3_count+bin4_count
            percent_bin0 = bin0_count / total_count * 100
            percent_bin1 = bin1_count / total_count * 100
            percent_bin2 = bin2_count / total_count * 100
            percent_bin3 = bin3_count / total_count * 100
            percent_bin4 = bin4_count / total_count * 100
            percent_positive = (bin1_count+bin2_count+bin3_count+bin4_count)/total_count*100

            print('% Cells Bin 0','\n','% Cells Bin 1', '\n','% Cells Bin 2','\n', '% Cells Bin 3','\n', '% Cells Bin 4','\n','% Positive Cells')
            print(percent_bin0, '\n', percent_bin1,'\n', percent_bin2,'\n', percent_bin3, '\n', percent_bin4, '\n', percent_positive)


if __name__ == '__main__':
    main()
