import csv
# 待转换的csv文件
csvfile = "../resource/sqlResult_1.csv"
# 输出文件地址
outCsvfile = "../resource/sqlResult_2.csv"
#错误输出文件地址
errorCsvfile = "../resource/sqlResult_1_error.csv"
if __name__ == '__main__':
    list = []
    error_list = []
    head = "vin,battery_pack_code,battery_pack_sys_code,batteryModuleCode,cellAmount,batteryCell"
    list.append(head)
    with open(csvfile, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        index = 0;
        for row in reader:
            if index % 1000 == 0:
                print("正在读取第: %d 行" % index)
            try:
                if index == 0:
                    index = index + 1
                    continue
                index = index + 1
                # print(row)
                vin = row[0]
                # print(vin)

                battery_pack_code = row[1]
                # print(battery_pack_code)

                battery_pack_sys_code = row[2]
                # print(battery_pack_sys_code)

                battery_module_cell_json = row[3]
                user_dict = eval(battery_module_cell_json)
                # print(user_dict)

                for cell in user_dict:
                    val = user_dict[cell]
                    # print(str(cell) + ": " + str(val))

                    batteryModuleCode = val['batteryModuleCode']
                    # print(batteryModuleCode)

                    cellAmount = val['cellAmount']
                    # print(cellAmount)

                    batteryCells = val['batteryCells']
                    for batteryCell in batteryCells:
                        v = batteryCells[batteryCell]
                        # print(batteryCell + ": " + v)
                        csv = vin + "," + str(battery_pack_code) + "," + str(battery_pack_sys_code) + "," + str(
                            batteryModuleCode) + "," + str(cellAmount) + "," + str(v)
                        list.append(csv)
            except Exception as e:
                # print(e)
                # print(row)
                error_list.append(row)
        f.close()

    with open(outCsvfile, 'a', encoding='utf8') as f:
        print("\n\n##########cell开始写入: ")
        for row in list:
            # print(row)
            f.write("{}\n".format(row))
        f.close()
        print("\n\n##########cell写入完毕: ")

    with open(errorCsvfile, 'a', encoding='utf8') as f:
        print("\n\n##########错误开始写入: ")
        for row in error_list:
            # print(row)
            f.write("{}\n".format(row))
        f.close()
        print("\n\n##########错误写入完毕: ")
