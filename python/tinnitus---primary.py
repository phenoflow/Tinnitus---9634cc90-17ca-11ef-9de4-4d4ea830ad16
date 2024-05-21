# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"ZEB..00","system":"readv2"},{"code":"Z911200","system":"readv2"},{"code":"F583200","system":"readv2"},{"code":"F583000","system":"readv2"},{"code":"F583z00","system":"readv2"},{"code":"1C2..00","system":"readv2"},{"code":"1C2Z.00","system":"readv2"},{"code":"1C24.00","system":"readv2"},{"code":"F583.00","system":"readv2"},{"code":"F583100","system":"readv2"},{"code":"1C23.00","system":"readv2"},{"code":"33737.0","system":"readv2"},{"code":"9927.0","system":"readv2"},{"code":"338.0","system":"readv2"},{"code":"12809.0","system":"readv2"},{"code":"59173.0","system":"readv2"},{"code":"46011.0","system":"readv2"},{"code":"17555.0","system":"readv2"},{"code":"44714.0","system":"readv2"},{"code":"45977.0","system":"readv2"},{"code":"44519.0","system":"readv2"},{"code":"36213.0","system":"readv2"},{"code":"H93.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('tinnitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["tinnitus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["tinnitus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["tinnitus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
